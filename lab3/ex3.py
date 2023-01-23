def is_plusone_dictionary(dict1):
   for i,j in zip(dict1.keys(),dict1.values()):
       if dict1[i] < dict1[i+2] and dict1[i] < dict1[i]+2:
           return True
       else:
           return False

print(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}) )      
           