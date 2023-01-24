def is_plusone_dictionary(d):
    keys = sorted(d.keys())
    for i in range(len(keys)):
        if d[keys[i]] - keys[i] != 1 :
            return False
    return True

print(is_plusone_dictionary({2:3,4:5,6:7,8:9}))
           