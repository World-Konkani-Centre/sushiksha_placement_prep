from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BadgeForm
from .models import Reward

@login_required
def award_badge(request):
    if request.user.profile.is_mentor == False:
        messages.error(request, "You don't have access to view this page :)")
        return redirect('index')
    if request.method=='POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            profiles = form.cleaned_data.get('profiles')
            message = form.cleaned_data.get('description')
            badge = form.cleaned_data.get('badge')
            awarded_by = request.user.profile.name

        for user in profiles:
            Reward.objects.create(user=user, awarded_by=awarded_by, description=message, badge=badge)
        messages.success(request, f'{badge.title} Awarded to {len(profiles)} Users')

        return redirect('badge')
    
    form = BadgeForm()

    context = {
        'form':form
    }

    return render(request, 'badge/create.html', context=context)
