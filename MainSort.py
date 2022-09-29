import AllSort as prog
import random
from time import monotonic


def GetList():
    lst = list(range(000))
    random.shuffle(lst)
    print(lst[0:10], "\n")
    timer(lst)


def timer(lst):
    start = monotonic()
    lst = prog.MonotonicSort(lst)
    finish = monotonic()
    print(lst[:10])
    print("Сортировка вставкой:", round(finish - start, 3), "\n")

    random.shuffle(lst)
    start = monotonic()
    lst = prog.SortChoices(lst)
    finish = monotonic()
    print(lst[:10])
    print("Сортировкой выбором:", round(finish - start, 3), "\n") 

    random.shuffle(lst)
    start = monotonic()
    lst = prog.SortBubble(lst)
    finish = monotonic()
    print(lst[:10])
    print("Сортировка пузырьком:", round(finish - start, 3), "\n") 

    random.shuffle(lst)
    start = monotonic()
    lst = prog.SortBubblePlus(lst)
    finish = monotonic()
    print(lst[:10])
    print("Сортировка пузырьком+:", round(finish - start, 3), "\n")
    

GetList()