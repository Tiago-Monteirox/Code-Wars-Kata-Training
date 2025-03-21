def get_grade(s1, s2, s3):
    score = (s1+s2+s3) // 3
    if 90 <= score <= 100: 
        letter = 'A'
    elif 80 <= score < 90: 
        letter = 'B'
    elif 70 <= score < 80: 
        letter = 'C'
    elif 70 <= score < 70: 
        letter = 'D'
    else:
        letter = 'F'
    return letter

print(get_grade(10, 20, 70))

