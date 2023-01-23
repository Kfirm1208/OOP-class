text = input()
# only_english = lambda t:''.join([i for i in t if i.isalpha()])
# print(only_english(text))

def only_english(t):
    text_del_num = [i for i in t if i.isalpha()]
    result = ''.join(text_del_num)
    return result
print(only_english(text))