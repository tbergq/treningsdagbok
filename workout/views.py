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
from django.views.generic.edit import FormView, UpdateView
from workout import forms, models as workout_models, WorkoutServie
import datetime
from django.template.context import RequestContext
from django.http.response import HttpResponse
import json
from django.core import serializers
from workout.models import ExcerciseRegister

# Create your views here.

workout_service = WorkoutServie
workout_manager = WorkoutServie.WorkoutManager()
program_service = BO.ProgramService()
program_manager = BO.ProgramManager()

def get_user(request):
    return account_models.UserProfile.objects.get(user=request.user)

@login_required
def index(request):
    current_user = get_user(request)
    programs = program_manager.get_programs_for_register(current_user.id) #program_models.Program.objects.filter(user=current_user)
    #group_programs = program_service.get_group_programs(current_user)
    
    return render(request, 'Workout/index.html', {'programs' : programs}) 


class LoadExercise(TemplateView):
    
    template_name = 'Workout/select.html'
    #model = program_models.Program
    
    def get(self, request, *args, **kwargs):
        context = {'object' : viewmodels.MyProgramsViewModel(kwargs['program_id'], get_user(request).id)}
        return self.render_to_response(context)
    
     
    
    @method_decorator(login_required(redirect_field_name='/workout/select/', login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
class RegisterWorkout(TemplateView):
    
    template_name = 'Workout/register.html'
    
    def get(self, request, *args, **kwargs):
        self.user = get_user(request)
        return TemplateView.get(self, request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        day_id = kwargs['day_id']
        program_id = kwargs['program_id']        
        day_register = workout_models.DayRegister.objects.filter(day_program_id=day_id, user=self.user)
        
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
    additional_data = {}
    
    
    def get(self, request, *args, **kwargs):
        
        self.user = get_user(request)
        self.initial['day_id'] = kwargs['day_id']#day program id
        self.initial['exercise_id'] = kwargs['exercise_id']#day exercise id
        self.additional_data['registered_this_workout'] = get_previous_register_data(kwargs['exercise_id'])
        self.additional_data['previous_lifted'] = get_most_recent_exercise_data(self.user, kwargs['exercise_id'])
        return FormView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        day_id = kwargs['day_id']
        exercise_id = kwargs['exercise_id']
        self.success_url = '/workout/register_partial/%s/%s/' % (day_id,exercise_id)
        form_class = self.get_form_class()        
        form = form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    
    def form_valid(self, form):
        form_object = form.save(commit=False)
        exists_register_with_same_set = workout_manager.exists_day_register(form_object)
        if not exists_register_with_same_set:
            form.save()
        return FormView.form_valid(self, form)
    
    def get_context_data(self, **kwargs):
        kwargs['registered_this_workout'] = self.additional_data['registered_this_workout']
        kwargs['previous_lifted'] = self.additional_data['previous_lifted']
        if 'spam_error' in self.additional_data:
            kwargs['spam_error'] = self.additional_data['spam_error']
        return FormView.get_context_data(self, **kwargs)
    
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return FormView.dispatch(self, request, *args, **kwargs)
    
    
    def get_initial(self):
        day_register = workout_models.DayRegister.objects.get(day_program_id=self.initial['day_id'], user=self.user)
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
    register = workout_models.DayRegister.objects.get(day_program_id=program_id, user=get_user(request))
    if not register.end_time:
        register.end_time = datetime.datetime.now()
        register.save()
        
    return redirect('/workout/')
    
    
class ShowRegisteredExercises(TemplateView):
    
    template_name = 'Workout/registered_workouts.html'
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        requested_program = request.GET.get('program_id', None)
        context = {}
        
        if requested_program:
            context['model'] =  workout_manager.get_day_registers_for_program(requested_program)
            context['select_list_items'] = workout_manager.get_selectlistitems_for_registered_workout(get_user(request).id, requested_program)
        else:
            context['model'] =  workout_models.DayRegister.objects.filter(user=get_user(request)).exclude(end_time=None).order_by('-start_time')
            context['select_list_items'] = workout_manager.get_selectlistitems_for_registered_workout(get_user(request).id, 0) 
        
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
    

def get_previous_register_data(exercise_id):
    
    exercises = workout_models.ExcerciseRegister.objects.filter(day_excersice_id=exercise_id).order_by('set_number')
    previous_set_weight = u"Registrert denne økt: "
    for i in range(len(exercises)):
        previous_set_weight += "%s x %skg, " % (exercises[i].reps, exercises[i].weight)
    
    return previous_set_weight


def get_most_recent_exercise_data(current_user, day_exercise_id):
    day_exercise = program_models.DayExcersice.objects.get(pk=day_exercise_id)
    my_day_registers = workout_models.DayRegister.objects.filter(user=current_user).order_by('start_time')
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
            return previous_info
    
    return u'Ingen registrerte tidligere for denne øvelsen'



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
    
    
class EditExerciseRegister(UpdateView):
    form_class = forms.ExcerciseRegisterForm
    model = ExcerciseRegister
    template_name = 'Workout/update_exercise.html'
    
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return UpdateView.dispatch(self, request, *args, **kwargs)    
    
    def get(self, request, *args, **kwargs):
        register_id = request.GET.get('id')
        self.object = self.model.objects.get(pk=register_id)
        form = self.get_form(self.form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        self.success_url = '/workout/show_workout/%s/' % request.POST.get('day_register')
        register_id = request.POST.get('object_id')
        self.object = self.model.objects.get(pk=register_id)

        return UpdateView.post(self, request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        return self.object
    

    