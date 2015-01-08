def Gcd(m,n):
    while n>0:
        c = m%n
        m = n
        n = c
    return m

if __name__ == "__main__":
    print Gcd(1989,1590)
