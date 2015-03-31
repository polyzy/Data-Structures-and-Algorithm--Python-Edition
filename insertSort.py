def insertSort(lst):
    n = len(lst)
    for i in range(1,n):
        value = lst[i]
        index = i
        while index > 0 and value < lst[index-1]:
            tmp = lst[index]
            lst[index] = lst[index - 1]
            lst[index-1] = tmp
            index -= 1
    return lst
