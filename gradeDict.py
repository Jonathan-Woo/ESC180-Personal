grades = {"PHY":"A","PRA":"A-","CALC":"A-","CSC":"A+"}

#takes a target grade and returns the subjects that match
#that target grade
def get_subj(grades, targest_grade):
    subjects = []
    for subj in grades:
        if grades[subj] == targest_grade:
            subjects.append(subj)
    return subjects

#Invert a dictionary: make a new dictionary whose keys are the
#values of the input dictionary, and whose values are lists
#of keys in the input dictionary that correspond to particular
#values

def invert_grades(grades):
    inverted_grades = {}
    all_grades = list(grades.values())
    #all_grades = list(dict.fromkeys(all_grades))

    for grade in all_grades:
        inverted_grades[grade] = get_subj(grades,grade)

    return inverted_grades
