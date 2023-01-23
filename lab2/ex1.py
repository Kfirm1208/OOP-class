my_list = [int(e) for e in input().split()]

my_list.sort()
if len(my_list) <= 10:
    for i in my_list:
        if i != 0:
            my_list.remove(i)
            my_list.insert(0,i)
            break     
    for j in my_list:
        print(j,end='')
else: 
    pass    
