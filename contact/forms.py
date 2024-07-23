from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    check_in = forms.DateField(widget=forms.SelectDateWidget)
    check_out = forms.DateField(widget=forms.SelectDateWidget)