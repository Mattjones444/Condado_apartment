from django.shortcuts import render

def contact(request):
    """ A view to return the gallery page """

    return render(request, 'contact.html')
