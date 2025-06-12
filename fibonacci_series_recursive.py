def fibo(val):
    if val==0:#checks if value is 0 since the sum will then be 0
        return 0
    elif val==2 or val==1:# checking the next 2 base cases since first two numbers of fibonacci series are predetermined
        return 1
    else:
        return fibo(val-1) + fibo(val-2)#caliing the function recursively,pushes current value to the stack,calls the fuction,
        #repeats the pushing till value is 0,1 or two,if yes if tracks back to the previous calls

print(fibo(6))