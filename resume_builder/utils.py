def education_is_valid(value, start, end):
    for index, val in enumerate(value.values()):
        if start <= index < end:
            if index % 4 == 0:
                print(f"CGPA -- {val}")
            elif index % 4 == 1:
                print(f"School/Collage Name -- {val}")
            elif index % 4 == 2:
                print(f"Course -- {val}")
            else:
                print(f"Passing Year -- {val}")


def skills_is_valid(skills, rank):
    for sk, rk in zip(skills, rank):
        print(f"skill -- {sk}")
        print(f"rank -- {rk}")

def projects_is_valid(name, start, end, desc):
    for pr, st, en, des in zip(name, start, end, desc):
        print(f"name -- {pr}")
        print(f"start -- {st}")
        print(f"end -- {end}")
        print(f"desc -- {desc}")


def internships_job_is_valid(role, place, desc):
    for rol, pl,des in zip(role, place,desc):
        print(f"role -- {rol}")
        print(f"place -- {pl}")
        print(f"desc -- {desc}")




def achievement_is_valid(ach):
    for ac in ach:
        print(f"achievement -- {ac}")


def other_is_valid(oth):
    for o in oth:
        print(f"oth -- {o}")
