def add_score(subject_score,subject,score):
    subject_score[subject] = score
   
    return subject_score

def calc_average_score(score):
    average = sum(score.values()) /len(score)
    result = f'{average:.2f}'
    
    return result


score = add_score({},'English',60)
print(calc_average_score(score))