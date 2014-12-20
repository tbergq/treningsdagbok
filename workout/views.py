# -*- coding: utf-8 -*-
from programs import models as program_models, BO
from account import models as account_models
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from programs import viewmodels
from django.utils.decorators import method_decorator
from treningsdagbok import DTOs
from django.views.generic.edit import FormView
from workout import forms, models as workout_models, WorkoutServie
import datetime
from django.template.context import RequestContext
from django.http.response import HttpResponse
import json
from django.core import serializers

# Create your views here.

workout_service = WorkoutServie

def get_user(request):
    return account_models.UserProfile.objects.get(user=request.user)

@login_required
def index(request):
    programs = program_models.Program.objects.filter(user=get_user(request))
    return render(request, 'Workout/index.html', {'programs' : programs}) 


class LoadExercise(TemplateView):
    
    template_name = 'Workout/select.html'
    #model = program_models.Program
    
    def get_context_data(self, **kwargs):
        return {'object' : viewmodels.MyProgramsViewModel(kwargs['program_id'])}
    
    @method_decorator(login_required(redirect_field_name='/workout/select/', login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
class RegisterWorkout(TemplateView):
    
    template_name = 'Workout/register.html'
    
    def get_context_data(self, **kwargs):
        day_id = kwargs['day_id']
        program_id = kwargs['program_id']        
        day_register = workout_models.DayRegister.objects.filter(day_program_id=day_id)
        
        if len(day_register) == 0:
            date = ''
        else:
            date = day_register[0].start_time
        return {
                'model' : DTOs.DTODayProgram(day_id),
                'day_register' : day_register,
                'started_register' : day_register != [],
                'date' : date,
                'program_id' : program_id,
                }
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    
    
    
    
class RegisterPartial(FormView):
    
    template_name = 'Workout/register_partial.html'
    form_class = forms.ExcerciseRegisterForm
    succsess_url = '/workout/register_partial/'
    initial = {}
    
    
    def get(self, request, *args, **kwargs):
        self.initial['day_id'] = kwargs['day_id']#day program id
        self.initial['exercise_id'] = kwargs['exercise_id']#day exercise id
        return FormView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        day_id = kwargs['day_id']
        exercise_id = kwargs['exercise_id']
        self.success_url = '/workout/register_partial/%s/%s/' % (day_id,exercise_id)
        print "success_url: %s" % self.success_url
        return FormView.post(self, request, *args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return FormView.dispatch(self, request, *args, **kwargs)
    
    
    def get_initial(self):
        day_register = workout_models.DayRegister.objects.get(day_program_id=self.initial['day_id'])
        previous_sets = workout_models.ExcerciseRegister.objects.filter(day_excersice_id=self.initial['exercise_id']).order_by('set_number')
        
        set_number = len(previous_sets) + 1
        
        
        return {
                'day_excersice' : self.initial['exercise_id'], 
                'day_register' : day_register ,
                'set_number' : set_number,
                'reps' : '',
                'weight' : '',
                'note' : '' ,
                'day_id' : self.initial['day_id'],
                'previous_sets' : previous_sets,
                
        }
    

def finish_register(request, program_id):
    register = workout_models.DayRegister.objects.get(day_program_id=program_id)
    if not register.end_time:
        register.end_time = datetime.datetime.now()
        register.save()
        print register.end_time
    else:
        print "pala"
    return redirect('/workout/')
    
    
class ShowRegisteredExercises(TemplateView):
    
    template_name = 'Workout/registered_workouts.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        context = {'model' : workout_models.DayRegister.objects.filter(user=get_user(request)).exclude(end_time=None) }
        return self.render_to_response(context)
    
    
class ShowWorkout(TemplateView):
    
    template_name = 'Workout/show_workout.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        dayRegisterId = kwargs['day_register_id']
        context = {'model' : workout_models.ExcerciseRegister.objects.filter(day_register_id=dayRegisterId)}
        context['name'] = context['model'][0].day_register.day_program.name
        print len(context)
        return self.render_to_response(context)


class StartDayRegister(RedirectView):
    
    url = '/workout/register/'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)
    
   
    def post(self, request, *args, **kwargs):
        
        day_exercise_id = kwargs['id']
        program = program_models.DayProgram.objects.get(pk=day_exercise_id)#BO.DayProgramService().get_from_day_exercise_id(day_exercise_id)
        entity = workout_models.DayRegister(user=get_user(request),day_program=program, start_time=datetime.datetime.now())
        entity.save()
        return RedirectView.post(self, request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        
        return "%s%s/%s" % (self.url, kwargs['id'], kwargs['program_id'])
    
@login_required
def get_previous_register_data(request, exercise_id):
    
    exercises = workout_models.ExcerciseRegister.objects.filter(day_excersice_id=exercise_id).order_by('set_number')
    previous_set_weight = ""
    for i in range(len(exercises)):
        previous_set_weight += "%s x %skg, " % (exercises[i].reps, exercises[i].weight)
    
    return render_to_response('Workout/previous_register_data.html', {'text' : previous_set_weight}, RequestContext(request))

@login_required
def get_most_recent_exercise_data(request, day_exercise_id):
    day_exercise = program_models.DayExcersice.objects.get(pk=day_exercise_id)
    my_day_registers = workout_models.DayRegister.objects.filter(user=get_user(request)).order_by('start_time')
    previous_info = u"Siste registrerte av samme øvelse:"
    ready_for_return = False
    for register in my_day_registers:
        my_excercise_registers = workout_models.ExcerciseRegister.objects.filter(day_register=register)
        for excercise in my_excercise_registers:
            check_this_exercise = program_models.DayExcersice.objects.get(pk=excercise.day_excersice_id)
            if check_this_exercise.base_excersice_id == day_exercise.base_excersice_id and check_this_exercise.id != day_exercise.id:
                previous_info += " %s x %skg," %(excercise.reps, excercise.weight)
                ready_for_return = True
        if ready_for_return:
            return render_to_response('Workout/previous_lifted.html', {'text' : previous_info}, RequestContext(request))
    
    return render_to_response('Workout/previous_lifted.html', {'text' : 'Ingen registrerte tidligere for denne øvelsen'}, RequestContext(request))



class CalendarOverview(TemplateView):
    template_name = 'Workout/calendar.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
   
@login_required 
def get_calendar_events(request):
    start_list = request.GET['start'].split("-")
    start_date = datetime.datetime(int(start_list[0]), int(start_list[1]), int(start_list[2]))
    end_list = request.GET['end'].split("-")
    end_date = datetime.datetime(int(end_list[0]), int(end_list[1]), int(end_list[2]))    
    my_registers = workout_models.DayRegister.objects.filter(user_id=get_user(request).id,start_time__gte=start_date, start_time__lte=end_date).exclude(end_time=None)
    json_list = []
    

    for register in my_registers:
        register_id = register.id
        allDay = True
        name = get_name(register_id)
        start = register.start_time.strftime("%Y-%m-%dT%H:%M:%S")
        json_entry = {'id':register_id, 'start':start, 'allDay':allDay, 'title' : name}
        json_list.append(json_entry)
    return HttpResponse(json.dumps(json_list), content_type='application/json')


def get_name(reg_id):
        day_register_object = workout_models.DayRegister.objects.get(pk=reg_id)
        day_program_object = program_models.DayProgram.objects.get(pk=day_register_object.day_program_id)
        week_object = program_models.Week.objects.get(pk=day_program_object.week_id)
        program_object = program_models.Program.objects.get(pk=week_object.program_id)
        return "%s \n %s/%s" % (program_object.name, week_object.name, day_program_object.name) 
    