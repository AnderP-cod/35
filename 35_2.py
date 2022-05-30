
def list_number(b_list):
    a = 0
    for i in b_list:
        if type(i) == type([]):
            a += list_number(i)
        else:
            a += i
    return a


print(list_number([2, 3, [1, 2], [4, 5, [10, 1]]]))