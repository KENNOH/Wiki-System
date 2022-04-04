from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *



class WikiObjectForm(forms.ModelForm):
    title = forms.CharField(max_length=150,label='Title', required=True,widget=forms.TextInput(attrs={'class':'form-control','name':'title'}))
    description = forms.CharField(label="Description:", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'description', 'rows': '4'}))
    external_link = forms.URLField(max_length=100, required=True,widget=forms.TextInput(attrs={'class':'form-control','name':'external_link'}))
    

    class Meta:
        model = WikiSearch
        fields = ('title','description','external_link',)
