def nodig(val):
    val=abs(val)
    if val//10==0:
        return 1
    else:
        return 1 + nodig(val//10)
print(nodig(-3336))