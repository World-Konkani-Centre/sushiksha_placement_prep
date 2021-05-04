from django.shortcuts import render
from .forms import BadgeForm

def award_badge(request):
    if request.method=='POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BadgeForm()

    context = {
        'form':form
    }

    return render(request, 'badge/create.html', context=context)
