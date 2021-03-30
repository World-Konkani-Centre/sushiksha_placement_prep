def education_is_valid(education):
    if education.is_valid():
        for form in education:
            name = form.cleaned_data.get('ed_name')
            course = form.cleaned_data.get('ed_course')
            percentage = form.cleaned_data.get('ed_percentage')
            passing_year = form.cleaned_data.get('ed_passing_year')
            print(f" {name} -- {course}--{percentage}--{passing_year}")


def skills_is_valid(skills):
    if skills.is_valid():
        for form in skills:
            name = form.cleaned_data.get('sk_name')
            expertise = form.cleaned_data.get('sk_expertise')
            print(f" {name} -- {expertise}")


def internships_job_is_valid(internships):
    if internships.is_valid():
        for form in internships:
            role = form.cleaned_data.get('ij_role')
            company = form.cleaned_data.get('ij_company')
            description = form.cleaned_data.get('ij_description')
            print(f" {role} -- {company} -- {description}")


def projects_is_valid(projects):
    if projects.is_valid():
        for form in projects:
            title = form.cleaned_data.get('p_name')
            start_date = form.cleaned_data.get('p_start_date')
            end_date = form.cleaned_data.get('p_end_date')
            description = form.cleaned_data.get('p_description')
            print(f" {title} -- {start_date} -- {end_date} -- {description}")


def achievement_is_valid(achievement):
    if achievement.is_valid():
        for form in achievement:
            name = form.cleaned_data.get('a_name')
            print(f" {name}")


def other_is_valid(other):
    if other.is_valid():
        for form in other:
            name = form.cleaned_data.get('o_name')
            print(f" {name}")
