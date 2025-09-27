from django.shortcuts import render

def index(request):
    """
    Landing page view for FreightController.
    """
    return render(request, "website/index.html")
