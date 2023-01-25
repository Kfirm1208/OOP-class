# def is_plusone_dictionary(d):
#     keys = sorted(d.keys())
#     last_keys = None
#     for i in range(len(keys)):
#         if d[keys[i]] - keys[i] != 1:
#             return False
#         if last_keys and keys[i] != last_keys + 2:
#             return False
#         last_keys = keys[i]
#     return True

def is_plusone_dictionary(d):
    keys = sorted(d.keys())
    return all(d[keys[i]] - keys[i] == 1 and (i == 0 or keys[i] == keys[i - 1] + 2) for i in range(len(keys)))


# print(is_plusone_dictionary({2:3,4:5,6:7,8:9}))
# print(is_plusone_dictionary({1:2,3:4,5:6,8:10}))
print(is_plusone_dictionary({10:9,8:7}))
           