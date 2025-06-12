def inspec(stringname,charname):
    count=0#counter variable to keep track
    final_str=""#final string which will be returned
    templist=list(stringname)#changing into list,since strings are immutable
    for i in range (0,len(stringname)):#traversing the string
        if templist[i]!=charname:#continue if current charachter is not equal to charname
            continue
        elif count==2 and templist[i]==charname:
            templist.insert(i+1,"$")#count==2 because we are inserting at i+1 index
            

        elif templist[i]==charname and count!=2:#increase count if charname is equal to element but is not third
            count=count+1
       
    final_str= "".join(templist)#join function for the final string
       
    
    return final_str


print(inspec("abaabcd ","a"))



    
