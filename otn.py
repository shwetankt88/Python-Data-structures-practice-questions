def otn(n):
    if n==1:
        print(1)
    else:
        print(n)
        print(otn(n-1))
otn(3)