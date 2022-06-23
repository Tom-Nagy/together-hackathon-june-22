from django.shortcuts import render, redirect, reverse
from .forms import AddEventForm
from .models import Event

# Create your views here.

def all_events(request):
    """
    A view to render all upcoming events
    """
    events= Event.objects.all

    if request.method == "POST":
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_events')
    else:
        form = AddEventForm()

    template = "events/all_events.html"
    context={
        'form': form,
        'events': events,

    }
    return render(request, template, context)
