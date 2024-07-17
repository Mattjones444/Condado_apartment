from django.shortcuts import render

def details(request):
    """ A view to return the gallery page """

    return render(request, 'details/details.html')
