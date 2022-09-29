def MonotonicSort(lst):
    for i in range(1, (len(lst))):
        tmp = lst[i]
        while (i > 0) and (tmp <= lst[i - 1]):
            lst[i] = lst[i - 1] 
            i -= 1
        else:
            lst[i] = tmp
    return lst


def SortBubble(lst):
    n = len(lst)
    for j in range(1, n):
        for i in range(n-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


def SortBubblePlus(lst):
    n = len(lst)
    for j in range(1, n):
        swap = False
        for i in range(n-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
        if not swap:
            break
    return lst


def SortChoices(lst):
    for i in range(len(lst), 1, -1):
        max = -10000
        for j in range(i):
            if lst[j] >= max: 
                max, index = lst[j], j
        lst[i - 1], lst[index] = lst[index], lst[i - 1]
    return lst