from django import forms
from django.contrib.auth.models import User
from models import UserProfile

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),help_text="Brukernavn")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),help_text="E-post")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), help_text="Passord")


    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    user_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control hidden', 'value' : 'regular', 'readonly':'readonly'}))
    class Meta:
        model = UserProfile
        fields = ('user_type',)