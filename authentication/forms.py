from django import forms
from django.contrib.auth.models import User,Group
import datetime
from django.db.models import Q




class UserSignInForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'username', 'id': 'username', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label="Password", max_length=150, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'placeholder': 'Enter your password'}))

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user_qs = User.objects.filter(Q(username__iexact=username))
        user = user_qs.first()
        if user == None:
            raise forms.ValidationError("Incorrect credentials provided!")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect credentials provided!")
        return super(UserSignInForm,self).clean(*args,**kwargs)