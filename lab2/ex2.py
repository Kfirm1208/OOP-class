x = ['abba','banana','ann']
c = 'a'
count_char_in_string = lambda x,c: [i.count(c) for i in x]
print(count_char_in_string(x,c))

# def count_char_in_string(x, c):
#   return [i.count(c) for i in x]
# print(count_char_in_string(x, c))