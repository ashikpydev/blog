from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label ="Email Address", required= True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePic(forms.ModelForm):
    profile_pic = forms.ImageField(
		label='Upload Your Photo',
        required=False,
		widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta(object):
        model = Userprofile
        fields = ['profile_pic',]
    
    def save(self, commit=True):
        user = super(ProfilePic, self).save(commit=False)
        if commit:
            user.save()
        return user