from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactSubmission

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            
            # Email content
            email_message = f"""
            Name: {name}
            Email: {email}
            Message: {message}
            Check-in Date: {check_in}
            Check-out Date: {check_out}
            """

            # Save the form data to the database
            ContactSubmission.objects.create(
                name=name,
                email=email,
                message=message,
                check_in=check_in,
                check_out=check_out
            )

            # Send an email
            send_mail(
                f'Contact Form Submission from {name}',
                email_message,
                email,  # From email address
                ['condado539@gmail.com'],  # To email address
                fail_silently=False,
            )
            
            # Redirect after successful submission
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    """ A view to return the gallery page """

    return render(request, 'contact_success.html')



