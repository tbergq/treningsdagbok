# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, RedirectView
from django.utils.decorators import method_decorator
from account.models import UserProfile
import models
from programs import models as program_models
from django.contrib.auth.models import User
import json
from workout.views import workout_service

# Create your views here.

def get_user(request):
    return UserProfile.objects.get(user=request.user)

def validate_user(request):
    return get_user(request).is_group_admin()

class PurchaseInfo(TemplateView):
    template_name = 'Group/purchase_info.html'

class MyGroups(TemplateView):
    template_name = 'Group/index.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        if not validate_user(request):
            return redirect('/group/purchase_info/')
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        context = {'model' : models.Group.objects.filter(group_admin=get_user(request))}
        return self.render_to_response(context)
    
    
class ShowRequestedGroup(TemplateView):
    template_name = 'Group/group.html'
    context = {}
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        if not validate_user(request):
            return redirect('/group/purchase_info/')
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        self.context['error'] = request.GET.get('error', None)
        return TemplateView.get(self, request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        #context = {}
        self.context['group'] = models.Group.objects.get(pk=kwargs['group_id'])
        self.context['members'] = models.GroupMembers.objects.filter(group_id=kwargs['group_id'])
        self.context['programs'] = models.GroupPrograms.objects.filter(group_id=kwargs['group_id']).exclude(is_active=False)
        return self.context
    
    
def invite_member(request):
    template = 'Group/invite_member.html'
    context = RequestContext(request)
    dic = {}
    if not validate_user(request):
        return redirect('/group/purchase_info/')
    if request.method == "GET":
        dic['group_id'] = request.GET.get('group_id')
        
        return render_to_response(template, dic, context)
    if request.method == "POST":
        mail = request.POST.get('e_mail', None)
        dic['group_id'] = request.POST.get('group_id')
        error = 'Fant ikke epost adressen'
        if mail:
            try:
                auth_user = User.objects.get(email=mail)
                user_profile = UserProfile.objects.get(user=auth_user)
                current_group = models.Group.objects.get(pk=request.POST.get('group_id'))
                new_member = models.GroupMembers(group=current_group, member=user_profile)
                new_member.save()
                return redirect('/group/group_info/%s/' % current_group.id)
            except:
                return redirect('/group/group_info/%s/?error=%s' % (dic['group_id'], error))
        return redirect('/group/group_info/%s/?error=%s' % (dic['group_id'], error))
        
        
    
    
class ShowProgramsAvailableForGroupAdd(TemplateView):
    template_name = 'Group/available_programs.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        if not validate_user(request):
            return redirect('/group/purchase_info/')
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        context = {
                   'programs' : program_models.Program.objects.filter(user=get_user(request)),
                   'group_id' : request.GET.get('group_id')
                   }
        return self.render_to_response(context)
    
class AddProgramToGroup(RedirectView):
    
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        
        if not validate_user(request):
            return redirect('/group/purchase_info/')
        return RedirectView.dispatch(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        group_id = request.POST['group_id']
        program_id = request.POST['program_id']
        new_group_program = models.GroupPrograms()
        new_group_program.program = program_models.Program.objects.get(pk=program_id)
        new_group_program.group = models.Group.objects.get(pk=group_id)
        new_group_program.is_active = True
        new_group_program.save()
        self.url = '/group/group_info/%s/' % group_id
        
        return RedirectView.post(self, request, *args, **kwargs)
    
    
    
    
class ShowGroupUserWorkouts(TemplateView):
    template_name = 'Workout/registered_workouts.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        if not validate_user(request):
            return redirect('/group/purchase_info/')
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        requested_program = request.GET.get('program_id', None)
        user_id = kwargs['user_id']
        group_id = kwargs['group_id']
        context = {}
        if requested_program:
            print 'req'
        else:
            context['model'] = workout_service.WorkoutManager().get_day_program_list_from_user_and_group(user_id, group_id)
            context['select_list_items'] = workout_service.WorkoutManager().get_selectlistitems_for_registered_workout(get_user(request).id, 0) 
        return self.render_to_response(context)
    
    
    
    