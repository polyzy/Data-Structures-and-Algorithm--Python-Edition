#-*- coding:utf-8 -*-


#效率O(N2)
def f1(lst):
    Maxsum= 0
    for num in lst:
        Thissum = 0
        for i in lst[lst.index(num):]:
            Thissum += i
            if Maxsum < Thissum:
                Maxsum = Thissum
        
    return Maxsum


#效率O(N)
def f2(lst):
    Maxsum = Thissum = 0
    for i in lst:
        Thissum += i
        if Maxsum < Thissum:
            Maxsum = Thissum
        elif Thissum < 0:
            Thissum = 0
    return Maxsum


if __name__ == "__main__":
    print f1([-10,2,3,4,5,6])
    print f2([-10,2,3,4,5,6])
        
    
