''' Views to manage and render the profile page '''

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    ''' Display and edit the user profile information '''

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # update user profile information
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'something went wrong \
                                     Please make sure inforation are valid \
                                     or contact us for assistance.')
            return redirect(reverse('profile'))
    else:
        profile_form = UserProfileForm(instance=user_profile)

    template = 'profiles/profile.html'
    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
    }

    return render(request, template, context)
