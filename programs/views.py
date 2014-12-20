# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from programs import forms
from account.models import UserProfile
from programs.models import BaseExercise, Program, Week, DayProgram, DayExcersice
import datetime
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, View
from django.views.generic.base import TemplateView, RedirectView
from BO import WeekService, BaseExerciseService, DayExerciseService
from viewmodels import MyProgramsViewModel, ShowDayViewModel
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.http.response import HttpResponse
from forms import DayExerciseForm
from django.forms.formsets import formset_factory

weekService = WeekService()
base_exercise_service = BaseExerciseService()
day_exercise_service = DayExerciseService()
def get_user(request):
    return UserProfile.objects.get(user=request.user)

@login_required
def new_program(request):
    view = 'Programs/new_program.html'
    context = RequestContext(request)
    dictonary = {}
    if request.method == 'GET':
        return render_to_response(view, dictonary, context)
    else:
        program = Program()
        program.user = UserProfile.objects.get(user=request.user)
        program.name = request.POST.get('name', False)
        program.date = datetime.datetime.now()
        number_of_weeks = request.POST.get('weeks', False)
        days_pr_week = request.POST.get('days_pr_week', False)
        try:
            int(number_of_weeks)
            int(days_pr_week)
        except:
            dictonary['error'] = 'Antall uker/Dager pr uke må være et nummer'
            dictonary['name'] = request.POST.get('name', False)
            return render_to_response(view, dictonary, context)
        if not program.name:
            dictonary['error'] = 'Navn må fylles inn'
            dictonary['name'] = request.POST.get('name', False)
            return render_to_response(view, dictonary, context)
        elif not number_of_weeks:
            dictonary['error'] = 'Antall uker må fylles inn'
            dictonary['name'] = request.POST.get('name', False)
            return render_to_response(view, dictonary, context)
        else:            
            program.save()
            for i in range(int(number_of_weeks)):
                week = Week()
                week.program = program
                week.name = 'Uke %s' % (i + 1)
                week.save()
                for j in range(int(days_pr_week)):
                    day = DayProgram()
                    day.name = "Dag %s" % (j + 1)
                    day.week = week
                    day.save()
                
            return redirect('/programs/')

def get_base_exercises(request):
   return JsonResponse(base_exercise_service.get_all(), safe=False)

@login_required
def index(request):
    view = 'Programs/index.html'
    context = RequestContext(request)
    dictionary = {}
    if request.method == 'GET':
        dictionary['programs'] = Program.objects.filter(user=get_user(request))
        programs = []
        for program in dictionary["programs"]:
            programs.append(MyProgramsViewModel(program.id))
        dictionary['program_list'] = programs
        
        return render_to_response(view, dictionary, context)

@login_required
def create_exercise(request):
    view = 'Programs/create_exercise.html'
    context = RequestContext(request)
    dictionary = {}
    dictionary['form'] = forms.ExcersiceForm()
    if request.method == 'GET':
        return render_to_response(view, dictionary, context)
    elif request.method == 'POST':
        excercise_form = forms.ExcersiceForm(data=request.POST)
        #excercise_form.user = UserProfile.objects.get(user=request.user)
        dictionary['form'] = excercise_form
        if excercise_form.is_valid():
            excercise = excercise_form.save(commit=False)
            excercise.user = UserProfile.objects.get(user=request.user)
            try:
                excercise.save()
            except:
                dictionary['error'] = "Øvelsen eksisterer allerede"
                return  render_to_response(view, dictionary,context)
            add_another = request.POST.get('other', False)
            if add_another:
                return render_to_response(view, {'form' : forms.ExcersiceForm()}, context)
            else:
                return redirect('/programs/')
        else:

            return render_to_response(view, dictionary,context)
        return  render_to_response(view, dictionary,context)

@login_required
def show_excercises(request):
    view = 'Programs/show_excercises.html'
    context = RequestContext(request)
    dictionary = {}
    excercises = BaseExercise.objects.all().order_by('muscle_group')
    dictionary['excercises'] = excercises
    return render_to_response(view, dictionary, context)


class ProgramWeeks(TemplateView):
    template_name = 'Programs/program_week.html'
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        model = MyProgramsViewModel(kwargs['program_id'])
        context = {'model' : model
                   }
        return render(request, self.template_name, context)
   
    
        
class AddWeek(RedirectView):
    url = '/programs/program_week/'
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        selected_program = Program.objects.get(pk=request.POST.get('program_id'))
        week_number = len(Week.objects.filter(program=selected_program)) + 1
        
        week = Week(name="Uke %s" % (week_number),program=selected_program)
        week.save()
        self.url = "%s%s/" % (self.url, selected_program.id)
        return RedirectView.post(self, request, *args, **kwargs)
    
    
    
class AddDayProgram(TemplateView):
    template_name = 'Programs/add_day.html'
    
    @method_decorator(login_required(login_url='account/login/'))
    def get(self,request, *args, **kwargs):    
        return render(request, self.template_name, {'week' : kwargs['week_id']})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        day = DayProgram(name=request.POST["name"], week = Week.objects.get(pk=kwargs['week_id']))
        day.save()
        return redirect('/programs/')


class DeleteDayProgram(TemplateView):
    template_name = 'Programs/delete_confirmation.html'
    
    def get_context_data(self, **kwargs):
        day_program_id = kwargs['day_id']
        return {
                'model' : DayProgram.objects.get(pk=day_program_id),
                'url' : '/programs/delete_day_program/%s/' % day_program_id,
                }
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)

class DeleteDayProgramRedirect(RedirectView):
    
    def __init__(self):
        self.program_id = 0
    
    def post(self, request, *args, **kwargs):
        
        day_program_id = kwargs['day_id']
        day_program = DayProgram.objects.get(pk=day_program_id)
        self.program_id = day_program.week.program.id
        DayExcersice.objects.filter(day_program=day_program).delete()
        day_program.delete()
        return RedirectView.post(self, request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        url = '/programs/program_week/%s/' % self.program_id
        return url
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)
    
class AddExerciseToDay(TemplateView):
    template_name = 'Programs/add_exercise_to_day.html'
    
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        DayExerciseFormSet = formset_factory(DayExerciseForm)
        formset = DayExerciseFormSet()
        context = self.get_context_data(**kwargs)
        context["formset"] = formset
        return render(request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        selected_day_id = kwargs['day_id']
        program_object_id = DayProgram.objects.get(pk=selected_day_id).week.program_id
        
        
        return {
                'day_id' : selected_day_id,
                'program_id' : program_object_id,
                
        }
        
def save_exercises_to_day(request, program_id, day_id):
    context = {'program_id' : program_id, 'day_id' : day_id}
    DayExerciseFormSet = formset_factory(DayExerciseForm)
    if request.method == 'POST':
        
        formset = DayExerciseFormSet(request.POST, request.FILES)
        context["formset"] = formset
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('/programs/program_week/%s/' % program_id)
        else:
            return render(request, 'Programs/add_exercise_to_day.html', context)
        
        return redirect('/programs/add_exercise_to_day/%s/' % day_id)
    else:
        return redirect('/account/')
        
class AddExerciseFormPartial(FormView):
    
    form_class = DayExerciseForm
    initial = {}
    template_name = 'Programs/exercisePartial.html'
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return FormView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        #form = DayExerciseForm()
        #form.day_program = request.GET['program_id']
        count = request.GET['count']
        exercises = BaseExercise.objects.all()
        next = int(count) + 1
        return render (request, self.template_name, {'count' : count, 'exercises' : exercises, 'next' : next, 'program_id' : request.GET['program_id']})
        #return self.render_to_response(self.get_context_data(form=form))

class ShowDayPartialView(TemplateView):
    template_name = 'Programs/show_day.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        day_id = kwargs['day_id']
        model = ShowDayViewModel(day_id)
        
        return render(request, self.template_name, {'model' : model})


def add_day(request, week_id):
    selected_week = Week.objects.get(pk=week_id)
    number_of_days = len(DayProgram.objects.filter(week=selected_week)) + 1
    day_name = "Dag %s" % number_of_days
    day = DayProgram(name=day_name,week=selected_week)
    day.save()
    return redirect('/programs/program_week/%s' % selected_week.program.id)
    
class AddDays(RedirectView):
    url = '/programs/program_week'
   
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)
        
        
    def post(self, request, *args, **kwargs):
        program = Week.objects.get(pk=request.POST.get('[0].week_id')).program
        self.url = "%s/%s/" % (self.url, program.id)
        number_of_weeks = (len(request.POST) - 1) / 2
        day_objects = []
        for i in range(number_of_weeks):
            week_query_helper = "[%s].week_id" % i
            number_of_days_helper = "[%s].day_number" % i
            number_of_days = request.POST.get(number_of_days_helper, 0)
            week_object = Week.objects.get(pk=request.POST.get(week_query_helper))
            for j in range(int(number_of_days)):
                day_name = 'Dag %s' % (j + 1)
                day_objects.append(DayProgram(name=day_name, week=week_object))
        for element in day_objects:
            element.save() 
        return RedirectView.post(self, request, *args, **kwargs)
        
    def get_redirect_url(self, *args, **kwargs):
        return self.url


class DeleteWeekConfirmation(TemplateView):
    
    template_name = 'Programs/delete_confirmation.html'
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = {
                   'model' : Week.objects.get(pk=kwargs['week_id']),
                   'url' : '/programs/delete_week/%s/' % kwargs['week_id'],
                   }
        return context
    
class DeleteWeek(RedirectView):
    
    def __init__(self):
        self.program_id = 0
    
    def get_redirect_url(self, *args, **kwargs):
        return '/programs/program_week/%s/' % self.program_id
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        week = Week.objects.get(pk=kwargs['week_id'])
        self.program_id = week.program_id
        week.delete()
        weekService.rename_weeks(self.program_id)
        return RedirectView.post(self, request, *args, **kwargs)

class CopyWeek(RedirectView):
    
    @method_decorator(login_required(login_url='account/login/'))
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        return '/programs/program_week/%s/' % Week.objects.get(pk=kwargs['week_id']).program_id
    
    def post(self, request, *args, **kwargs):
        weekService.copy_week_from_week_id(kwargs['week_id'])
        return RedirectView.post(self, request, *args, **kwargs)
    
    
@login_required(login_url='/account/')
def get_muscle_groups(request):
    names = base_exercise_service.get_distinct_muscle_groups()
    return JsonResponse(names, safe=False)
    
class DeleteDayExercise(DeleteView):
    template_name = 'Programs/delete_day_exercise_confirmation.html'
    model = DayExcersice
    
    def get_success_url(self):
        return '/programs/add_exercise_to_day/%s/' % self.object.day_program_id
    
    