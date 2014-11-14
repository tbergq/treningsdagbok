from programs import models as program_models, BO
from account import models as account_models
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from programs import viewmodels
from django.utils.decorators import method_decorator
from treningsdagbok import DTOs
from django.views.generic.edit import FormView
from workout import forms, models as workout_models

# Create your views here.

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
        return {'object' : viewmodels.MyProgramsViewModel(kwargs['pk'])}
    
    @method_decorator(login_required(redirect_field_name='/workout/select/', login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
class RegisterWorkout(TemplateView):
    
    template_name = 'Workout/register.html'
    
    def get_context_data(self, **kwargs):
        return {'model' : DTOs.DTODayProgram(kwargs['day_id'])}
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)
    
    
    
    
    
class RegisterPartial(FormView):
    
    template_name = 'Workout/register_partial.html'
    form_class = forms.ExcerciseRegisterForm
    succsess_url = '/workout/partial/'
    initial = {}
    
    
    def get(self, request, *args, **kwargs):
        self.initial['day_id'] = kwargs['day_id']
        self.initial['weigth'] = 60
        print self.initial
        return FormView.get(self, request, *args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)
    
    @method_decorator(login_required(login_url='/account/'))
    def dispatch(self, request, *args, **kwargs):
        return FormView.dispatch(self, request, *args, **kwargs)
    
    
    
    
    def get_initial(self):
        """
        test = self.get_context_data()
        print test
        print self.day_id
        #day_id = self.request.GET.get('day_id', 1)
        #print day_id
        #exercise_id = self.request.GET.get('exercise_id', 1)
        print self.exercise_id
        program = BO.DayProgramService().get_from_day_exercise_id(self.day_id)
        day_register = workout_models.DayRegister.objects.filter(day_program_id=program.id)
        """
        print self.initial
        
        return {
                'day_excersice' : 1, 
                'day_register' :1 ,
                'set_number' : 1,
                'reps' : '',
                'weight' : self.initial['weigth'],
                'note' : '' 
        }
    
    
    
    