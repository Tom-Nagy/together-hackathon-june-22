''' Views to manage and render the profile page '''

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile


@login_required
def profile(request):
    ''' Display the user profile information '''
    user_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'user_profile': user_profile,
    }
    return render(request, template, context)
