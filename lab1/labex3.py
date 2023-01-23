h_in,min_in,h_out,min_out = [int (i) for i in input().split()]
diff_h = abs(h_out-h_in)
diff_min = abs(min_out - min_in)


if h_in < 7 or (h_out ==23 and min_out != 0):
    pass
else:
    money = 0 
    if min_in < min_out:
        diff_h -= 1
        diff_min += 60

if diff_min <= 15 and diff_h == 0:
    money = 0
     
if (diff_min > 15 and diff_h ==0) or (1<= diff_h <=3):
    money = 10 * diff_h
    money += 10 if diff_min != 0 and diff_h < 3 else 0 
 
if (3 < diff_h <= 6) or (diff_h == 3 and diff_min !=0):      
    money = 20 * (diff_h-3) + 30
    money += 20 if diff_min !=0 else 0
    
if diff_h > 6 or (diff_h == 6 and diff_min !=0):
   money = 200     

print(money)