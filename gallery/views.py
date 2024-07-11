from django.shortcuts import render

def gallery(request):
    """ A view to return the gallery page """

    return render(request, 'gallery.html')
