from django import forms
from .models import ShowcasePost

class PostForm(forms.ModelForm):
  class Meta:
    model = ShowcasePost
    fields = '__all__'

