def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1,n-i):
            if lst[j-1] > lst[j]:
                temp = lst[j-1]
                lst[j-1] = lst[j]
                lst[j] = temp
    return lst
            
