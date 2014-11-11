from programs import models as program_models
from account import models as account_models
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.

def get_user(request):
    return account_models.UserProfile.objects.get(user=request.user)

@login_required
def index(request):
    programs = program_models.Program.objects.filter(user=get_user(request))
    return render(request, 'Workout/index.html', {'programs' : programs}) 


class LoadExercise(DetailView):
    
    template_name = 'Workout/select.html'
    
    
    
    def get_context_data(self, **kwargs):
        return {'programs' : program_models.Program.objects.get(pk=kwargs['program_id'])}