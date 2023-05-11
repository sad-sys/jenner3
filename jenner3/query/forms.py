# forms.py
from django import forms

class QueryForm(forms.Form):
    user_query = forms.CharField(label='Your query', max_length=100)
