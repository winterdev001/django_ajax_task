from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(label='Description', widget=forms.Textarea())