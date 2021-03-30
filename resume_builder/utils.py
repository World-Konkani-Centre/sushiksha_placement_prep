def education_is_valid(education):
    if education.is_valid():
        for form in education:
           print(form.cleaned_data)


def skills_is_valid(skills):
    if skills.is_valid():
        for form in skills:
            print(form.cleaned_data)


def internships_job_is_valid(internships):
    if internships.is_valid():
        for form in internships:
            print(form.cleaned_data)


def projects_is_valid(projects):
    if projects.is_valid():
        for form in projects:
            print(form.cleaned_data)


def achievement_is_valid(achievement):
    if achievement.is_valid():
        for form in achievement:
            print(form.cleaned_data)


def other_is_valid(other):
    if other.is_valid():
        for form in other:
            print(form.cleaned_data)
