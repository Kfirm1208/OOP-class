str1 =input()

def check_string(str1):
    count = {'Upper case':0,'Lower case':0}
    for s in str1:
        if s.isupper():
            count['Upper case'] +=1
        elif s.islower():
            count['Lower case'] +=1
        else:
            pass
    print('No. of Lower case charector :',count['Lower case'])
    print('No. of Upper case charector :',count['Upper case'])

check_string(str1)
                