# -*- coding: utf-8 -*-

#循环方法
def f1(lst, n):
    low = 0
    high = len(lst)-1
    while low <= high:           #注意：必须是<=
        mid = (low + high)/2
        if lst[mid] < n:
            low = mid + 1
        elif lst[mid] > n:
            high = mid - 1;
        else:
            return mid
    return -1

#递归方法
def f2(lst,n,low,high):
    if low > high:
        return -1

    mid = (low + high)/2
    if lst[mid] > n:
        return f2(lst,n,low,mid-1)
    elif lst[mid] < n:
        return f2(lst,n,mid+1,high)
    else:
        return mid

if __name__ == "__main__":
    print f1([1,2,3,34,56,57,78,87],34)
    print f2([1,2,3,34,56,57,78,87],87,0,7)
