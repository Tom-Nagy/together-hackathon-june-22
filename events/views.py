from django.shortcuts import render

# Create your views here.

def all_events(request):
    """
    A view to render all upcoming events
    """
    template = "events/all_events.html"
    context={
        
    }
    return render(request, template, context)
