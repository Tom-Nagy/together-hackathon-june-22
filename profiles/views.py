''' Views to manage and render the profile page '''

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    ''' Display and Edit the user profile information '''

    user_profile = get_object_or_404(UserProfile, user=request.user)
    user = User.objects.get(username=request.user.username)

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
            return redirect('profile')
        else:
            messages.error(request, 'something went wrong \
                                    Please make sure inforation are valid \
                                    or contact us for assistance.')
            return redirect(reverse('profile'))

    profile_form = UserProfileForm(instance=user_profile)
    template = 'profiles/profile.html'
    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
    }

    return render(request, template, context)


@login_required
def edit_make_profile_public_status(request):
    ''' Edit/switch the status of make profile public '''

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        make_profile_public = request.POST['make_profile_public']
        user_profile.make_public = make_profile_public
        user_profile.save()
        if make_profile_public == 'True':
            messages.success(request, 'Your profile is now public')
        else:
            messages.success(request, 'Your profile is now private')

        return redirect('profile')


@login_required
def delete_profile(request):
    ''' Delete the user profile and the user '''

    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        user.delete()

        messages.success(request, 'Your profile was deleted successfuly')
        return redirect('home')
