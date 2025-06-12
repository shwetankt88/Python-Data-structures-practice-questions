def fact(val):
    if val==0:#checking base case
        return 1
    else:
        return val*fact(val-1)#pushes current fact(val) to the stack,calls recursively till base case is reached
        #then returns to previous calls
print(fact(4))