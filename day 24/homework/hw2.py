def get_grade(s1, s2, s3):
    averange = (s1 + s2 + s3) / 3
    if averange >= 90:
        return "A"
    elif averange >= 80:
        return "B"
    elif averange >= 70:
        return "C"
    elif averange >= 60:
        return "D"
    else:
        return "F"
