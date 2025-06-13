def gcd(a,b):#find the greatest common divisor 
    if b==0:
        return a#returning a if b is 0
    else:
        return gcd(b,a%b)#calling the function
print(gcd(21,27))