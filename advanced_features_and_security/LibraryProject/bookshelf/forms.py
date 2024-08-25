from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class ExampleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea)
