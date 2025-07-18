def stringremove_duplicates(stringname):
    setname=set()#initializing an empty set
    listname=[]#initializing an empty list
    for i,v in enumerate(stringname):#loop to iterate the list
        if v not in setname:#checking if the current character is in the set
            setname.add(v)#if no,then add that element in the set
            listname.append(v)#appending that element if not present
    #nothing is done if the element is present,i.e. that element will not be appended to the list,thus,no duplicate elements
    final_string="".join(listname)#join function to change the list to a string to return final ans
    return final_string#final return statement


print(stringremove("banana"))
#edited
