# -*- coding: utf-8 -*-
from django import forms
from programs.models import BaseExercise, Week, DayProgram, DayExcersice
from account.models import UserProfile

name_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=128, help_text="Navn")

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
    
    class Meta:
        model = DayExcersice
        fields = ('base_excersice', 'set', 'reps', 'day_program',)
        
        widgets = {
            'day_program' : forms.HiddenInput(),
            'base_excersice' : forms.Select(attrs={'class' : 'form-control'}),
            'set' : forms.TextInput(attrs={'class' : 'form-control'}),
            'reps' : forms.TextInput(attrs={'class' : 'form-control'}), 
        }
        
        labels = {
            'set' : 'Sets',
            'reps' : 'Reps',
            'base_excersice' : 'Øvelse',
            'day_program' : ''
        }
    
    
    
    
    
