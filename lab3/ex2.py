def add_score(subject_score,student,subject,score):
    if student in subject_score:
        if subject in subject_score[student]:
            subject_score[student][subject] = score
        else:
            subject_score[student][subject] = score
    else:
     subject_score[student] = {subject: score}
    
    return subject_score

def calc_average_score(data):
    total = 0
    count = 0
    my_score = {}
    for student in data:
        for subject in data[student]:
            total += data[student][subject]
            count += 1
        result = total/count
    my_score[student] = f'{result:.2f}'
    return my_score


score = add_score({'65010682':{'Physic':79}},'65010682','English',60)
print(calc_average_score(score))
