from django import forms

from django.contrib.auth.models import User

#----------------------------------------------------------------------------
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

#----------------------------------------------------------------------------
class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)

    clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.get(email=email)
        if user is not None:
            raise forms.ValidationError("This email already registered.")

    clean_confirm(self):
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm']
        if password != confirm:
            raise forms.ValidationError("'Passwords must match.'")

#----------------------------------------------------------------------------
class EditForm(forms.Form):
    title = forms.CharField(max_length=500)
    url = forms.CharField(max_length=500)
    groupname = forms.CharField(max_length=25, required=False)
