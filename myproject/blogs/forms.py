import email
from django import forms
from django.core import validators

class TeachersRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)


    def clean(self):  
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']
        if rightpass != wrongpass:
            raise forms.ValidationError('Password does not match')
        


