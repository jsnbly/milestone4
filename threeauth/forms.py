from django import forms

class UserLoginForm(forms.Form):
    #Form to be used for user login
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
