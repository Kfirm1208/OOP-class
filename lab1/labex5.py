ans = list()

for i in range(100,1000):
    for j in range(100,1000):
        num = str(i*j)
        if num == num[::-1]:
            ans.append(int(num)) 
            
ans.sort()   
# same max(ans)      
print(ans[-1]) 
          