from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-white',
            'id': 'username',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-white',
            'id': 'password',
            'placeholder': "Password"}
    ))


class UserRegistrationForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-white',
            'id': 'firstname',
            'placeholder': 'First Name'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-white',
            'id': 'username',
            'placeholder': 'Username'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control bg-white',
            'id': 'email',
            'placeholder': 'Email Address'
        }
    ))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control bg-white',
                                       'id': 'password',
                                       'placeholder': "Enter Password"}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control bg-white',
                                        'id': 'passwordConfirm',
                                        'placeholder': "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match!')
        return cd['password2']
