from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30,label='Username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': '*****'}))
        
    def clean_username(self):
        cd = self.cleaned_data
        if cd['username'] is None:
            raise forms.ValidationError('\nThis field is required.\n') 
            
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] is None:
            raise forms.ValidationError('\nThis field is required.\n') 