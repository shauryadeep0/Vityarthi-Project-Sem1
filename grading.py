def calculate_grade(physics, chemistry, maths):
    """Calculates percentage and determines letter grade."""
    perc = (physics + chemistry + maths) / 3

    if perc >= 90:
        grade = "S"
    elif perc >= 80:
        grade = "A"
    elif perc >= 70:
        grade = "B"
    elif perc >= 60:
        grade = "C"
    elif perc >= 50:
        grade = "D"
    elif perc <= 30:
        grade = "F"
    else:
        grade = "E"

    return round(perc, 2), grade