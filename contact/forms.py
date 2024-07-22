from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    start_date = forms.DateField(label='Check in Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Check out Date', widget=forms.DateInput(attrs={'type': 'date'}))
    message = forms.CharField(widget=forms.Textarea, label='Your message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))