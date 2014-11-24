# -*- coding: utf-8 -*-
from django import forms
from programs.models import BaseExercise, Week, DayProgram, DayExcersice
from account.models import UserProfile
from django.core.exceptions import ValidationError
import re

name_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=128, help_text="Navn")
required_dic = {'required' : 'Feltet er påkrevd'}

class ExcersiceForm(forms.ModelForm):
    muscle_group = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=128, help_text="Muskelgruppe")
    name = name_field

    class Meta:
        model = BaseExercise
        fields = ('muscle_group', 'name',)
        exclude = ('user',)


class WeekForm(forms.ModelForm):

    #name = name_field

    class Meta:
        model = Week
        fields = ('name',)
        exclude = ('program',)

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

        labels = {
            'name' : 'Navn',
        }

        error_messages = {
            'name': {
                'required': 'feltet er påkrevd',
            },
        }

class DayForm(forms.ModelForm):
    class Meta:
        model = DayProgram
        fields = ('name',)
        exclude = ('week',)

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

        labels = {
            'name' : 'Navn',
        }

        error_messages = {
            'name': {
                'required': 'feltet er påkrevd',
            },
        }




class DayExerciseForm(forms.ModelForm):
    
    
        
    def clean_set(self):
        
        data = self.cleaned_data['set']
        values = data.split("-")
        if len(values) > 2:
            raise forms.ValidationError("Må være et tall eller to tall skilt med -")
        for number in values:
            try:
                int(number)
            except:
                raise forms.ValidationError("Må være et tall eller to tall skilt med -")
        return data
        
    """def clean_reps(self):
        reps = self.cleaned_data['reps']
        regex_comma = r'^[\d+,\d+]+$'
        regex_hyphen = r'[\d+-\d+]$'
        comma_match = re.match(regex_comma, reps)
        hyphen_match = re.match(regex_hyphen, reps)
        if not comma_match and not hyphen_match:
            raise forms.ValidationError("Må være på formen 8,6,4, eller 8-12")
        return reps"""
    
    class Meta:
        model = DayExcersice
        fields = ('base_excersice', 'set', 'reps', 'day_program', 'description', 'break_time')
        
        widgets = {
            'day_program' : forms.HiddenInput(),
            'base_excersice' : forms.Select(attrs={'class' : 'form-control', 'id' : 'baseExercise'}),
            'set' : forms.TextInput(attrs={'class' : 'form-control'}),
            'reps' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'description' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'break_time': forms.TextInput(attrs={'class' : 'form-control'}) ,
        }
        
        labels = {
            'set' : 'Sets',
            'reps' : 'Reps',
            'base_excersice' : 'Øvelse',
            'day_program' : '',
            'description' : 'Beskrivelse', 
            'break_time': 'Pause(i min)'
        }
        
        error_messages = {
            'set' : {'required' : 'Feltet er påkrevd', 'format-error' : 'test pala'},
            'reps' : required_dic,
            'base_excersice' : required_dic,
            'day_program' : required_dic,
            
            'break_time': required_dic,
        }
    
        
    
    
    
