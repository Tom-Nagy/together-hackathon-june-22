''' Views to manage and render the profile page '''

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    ''' Display and edit the user profile information '''

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # update user profile information
        profile_form = UserProfileForm(request.POST, request.FILES,
                                       instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()

            # Update User info
            user = User.objects.get(username=request.user.username)
            username = request.POST['username']
            email = request.POST['email']
            user.username = username
            user.email = email
            user.save()

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
