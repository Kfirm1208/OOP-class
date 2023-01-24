# def is_plusone_dictionary(d):
#     keys = sorted(d.keys())
#     for i in range(len(keys)):
#         if d[keys[i]] - keys[i] != 1 :
#             return False
#     return True

# def is_plusone_dictionary_v4(d):
#     return all(key+1 == value for key,value in d.items())

# def is_plusone_dictionary_v5(d):
#     return all(key+1 == value for key, value in zip(d.keys(), d.values()))

# def is_plusone_dictionary_v6(d):
#     keys = list(d.keys())
#     values = list(d.values())
#     keys.sort()
#     values.sort()
#     for i in range(len(keys)):
#         if keys[i] + 1 != values[i]:
#             return False
#     return True
def is_plusone_dictionary_v7(d):
    keys = list(d.keys())
    values = list(d.values())
    diff = list(map(lambda x, y: x+1 == y, keys, values))
    return all(diff)

print(is_plusone_dictionary_v7({2:3,4:5,6:7,8:9}))
           