def pow(x,n):
    if n==1 or n==0:
        return x
    else:
        return x*pow(x,n-1)

print(pow(3,2))
        