from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='Haslo')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Powtorz haslo')

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('hasla nie sa identyczne')
        return cd['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields =  ['first_name','last_name','email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth','photo']
        labels = {'date_of_birth': 'Data urodzenia', 'photo': 'Zdjecie'}

