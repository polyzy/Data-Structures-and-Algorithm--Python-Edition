# -*- coding: utf-8 -*-

#递归
def Pow(x,n):
    if n == 0:
        return 1;
    elif n == 1:
        return x
    elif n%2 == 0:
        return Pow(x*x, n/2)
    else:
        return Pow(x*x, n/2) * x



#非递归
def foo(x,n):
    result=1
    while n>0:
        if n%2 == 1:
            result *= x
        x = x * x
        n = n/2
    return result
    

if __name__ == "__main__":
    print Pow(2,100)
