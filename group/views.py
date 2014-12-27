# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from account.models import UserProfile
import models

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
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        if not validate_user(request):
            return redirect('/group/purchase_info/')
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = {}
        context['group'] = models.Group.objects.get(pk=kwargs['group_id'])
        context['members'] = models.GroupMembers.objects.filter(group_id=kwargs['group_id'])
        
        return context
    
    
    
    
    
    
    
    
    