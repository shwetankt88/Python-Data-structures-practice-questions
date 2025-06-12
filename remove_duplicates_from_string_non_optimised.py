def stringrem(stringname):
    templist=list(stringname)
    for i,v in enumerate(templist):
        for j,w in enumerate(templist):
            if v==w and i!=j:
                templist.pop(i)
    final_str="".join(templist)
    return final_str

print(stringrem("banana is a very good fruit"))            
