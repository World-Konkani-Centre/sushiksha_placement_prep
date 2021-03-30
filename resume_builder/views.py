from django.shortcuts import render, redirect

from resume_builder.forms import EducationFormSet


# Create your views here.
def test(request):
    formset = None
    if request.method == 'GET':
        formset = EducationFormSet(request.GET or None)
    elif request.method == 'POST':
        formset = EducationFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                course = form.cleaned_data.get('course')
                percentage = form.cleaned_data.get('percentage')
                print(f" {name} -- {course}--{percentage}")
                return redirect("test")
    return render(request, 'resume-builder/test.html', context={
        'formset':formset, 'heading':"hello"
    })
