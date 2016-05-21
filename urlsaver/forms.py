from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.add_error('email', forms.ValidationError('Invalid user.'))
        else:
            if not user.check_password(password) and password:
                self.add_error('password',
                               forms.ValidationError('Invalid password.'))
        return cleaned_data


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already registered.')
        return email

    def clean_confirm(self):
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm']
        if password != confirm:
            raise forms.ValidationError('Passwords must match.')
        return password


class EditForm(forms.Form):
    title = forms.CharField(max_length=500)
    url = forms.CharField(max_length=500)
    groupname = forms.CharField(max_length=25, required=False)


class SearchForm(forms.Form):
    search = forms.CharField()


class RestorePasswordForm(forms.Form):
    pass
