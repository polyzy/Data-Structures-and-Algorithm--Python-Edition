def selectSort(lst):
    n = len(lst)
    for i in range(n-1):
        small = i
        for j in range(i+1,n):
            if lst[j] < lst[i]:
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
    return lst
