from django import forms

from django_summernote.widgets import SummernoteWidget
from .models import *

from datetime import timedelta




class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter username...',
               'class': 'input100', 'id': 'loginname'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password...',
               'class': 'input100', 'id': 'loginpword'}))



class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
        exclude = ('vat_pan',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'font-family:BalaramFont',
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'contact_no': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'alt_contact_no': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'map_location': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'pattern': '[\w\.-]+@[\w\.-]+\.\w{2,4}'
            }),
            'alt_email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'slogan': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'facebook': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'youtube': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'whatsapp': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'viber': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'terms_and_conditions': SummernoteWidget(),
        }