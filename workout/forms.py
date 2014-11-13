from django import forms
from workout import models as workout_models

class ExcerciseRegisterForm(forms.ModelForm):
    
    class Meta:
        model = workout_models.ExcerciseRegister
        fields = ['day_excersice', 'day_register', 'set_number', 'reps', 'weight', 'note']
        
        widgets = {
            'day_excersice' : forms.HiddenInput(),
            'day_register' : forms.HiddenInput(),
            'set_number' : forms.HiddenInput(),
            'reps' : forms.TextInput(attrs={'class' : 'form-control'}),
            'weight' : forms.TextInput(attrs={'class' : 'form-control'}),
            'note' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
        
        labels = {
            'day_excersice' : '',
            'day_register' : '',
            'set_number' : '',
            'reps' : 'Reps',
            'weight' : 'Vekt',
            'note' : 'notater',     
        }