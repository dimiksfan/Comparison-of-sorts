import random as r




def make_lst():
    lst = list(range(20000))
    r.shuffle(lst)
    print(lst)
    return(insert_sort(lst))


def insert_sort(lst):
    for i in range(1, (len(lst))):
        tmp = lst[i]
        while (i > 0) and (tmp <= lst[i - 1]):
            lst[i] = lst[i - 1] 
            i -= 1
        else:
            lst[i] = tmp
    return(lst)

