from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            pass
    else:
        form = ContactForm()  # Ensure form is defined here for GET requests

    return render(request, 'contact.html', {'form': form})
