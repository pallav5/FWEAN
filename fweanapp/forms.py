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


from django.forms.models import inlineformset_factory,formset_factory
ImageMediaFormSet = inlineformset_factory(
    ImageAlbum,ImageMedia, fields=['image','title'],can_delete = True,
    widgets= {
        'image': forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'style': "border: 1px solid gray;",
        }),
        'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Write image caption here..(optional)',
            'style': "border: 1px solid gray;",
        }),

    }
)



class ImageAlbumForm(forms.ModelForm):
    class Meta:
        model = ImageAlbum
        fields = "__all__"
        # exclude = ()
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'placeholder': 'Desc..',

                "style": "height: 170px; border: 1px solid gray;"
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),


        }
