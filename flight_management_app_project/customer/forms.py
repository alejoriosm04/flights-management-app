# from django.forms import ModelForm
# from .models import User

## Create an user form with name, id_user, age, email only
# class UserForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ModelForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update({'class': 'form-control'})
#         self.fields['id_user'].widget.attrs.update({'class': 'form-control'})
#         self.fields['age'].widget.attrs.update({'class': 'form-control'})
#         self.fields['email'].widget.attrs.update({'class': 'form-control'})
#     class Meta:
#         model = User
#         fields = ['name', 'id_user', 'age', 'email']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for filedname in ['username', 'password1', 'password2']:
            self.fields[filedname].help_text = None
            self.fields[filedname].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']