def bubbleSort(lst):
    n = len(lst)
    for i in range(n):              #一共要循环n次
        for j in range(1,n-i):      #因为每次循环都会找出最大的数并放到最右边，该数字下次就不必再参与循环。所以下次循环的数字的个数就可以减1
            if lst[j-1] > lst[j]:
                temp = lst[j-1]
                lst[j-1] = lst[j]
                lst[j] = temp
    return lst
            
