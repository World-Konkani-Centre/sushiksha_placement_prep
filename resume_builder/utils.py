def education_is_valid(education):
    if education.is_valid():
        for form in education:
            name = form.cleaned_data.get('name')
            course = form.cleaned_data.get('course')
            percentage = form.cleaned_data.get('percentage')
            print(f" {name} -- {course}--{percentage}")


def skills_is_valid(skills):
    if skills.is_valid():
        for form in skills:
            name = form.cleaned_data.get('name')
            expertise = form.cleaned_data.get('expertise')
            print(f" {name} -- {expertise}")


def internships_job_is_valid(internships):
    if internships.is_valid():
        for form in internships:
            role = form.cleaned_data.get('role')
            company = form.cleaned_data.get('company')
            description = form.cleaned_data.get('description')
            print(f" {role} -- {company} -- {description}")


def projects_is_valid(projects):
    if projects.is_valid():
        for form in projects:
            title = form.cleaned_data.get('title')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            description = form.cleaned_data.get('description')
            print(f" {title} -- {start_date} -- {end_date} -- {description}")


def achievement_is_valid(achievement):
    if achievement.is_valid():
        for form in achievement:
            name = form.cleaned_data.get('name')
            print(f" {name}")


def other_is_valid(other):
    if other.is_valid():
        for form in other:
            name = form.cleaned_data.get('name')
            print(f" {name}")
