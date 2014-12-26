# -*- coding: utf-8 -*-
from django import forms
import models as group_models

form_control = {'class' : 'form-control'}
required_dic = {'required' : u'Feltet er påkrevd'}

class GroupForm(forms.ModelForm):
    class Meta:
        model = group_models.Group
        fields =('name', 'group_admin', 'max_members', 'valid_to_date',)
        
        widgets = {
                   'name' : forms.TextInput(attrs={'class': 'form-control'}),
                   'group_admin' :forms.HiddenInput(), 
                   'max_members' : forms.TextInput(attrs={'class' : 'form-control'}), 
                   'valid_to_date': forms.HiddenInput(),
                   
        }
        
        labels = {
                  'name' : 'Navn', 
                  'max_members' : 'Antall lisenser', 
        }
        
        error_messages = {
                          'name' : required_dic,
                          'max_members' : required_dic
        }