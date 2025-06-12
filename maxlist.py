def maxlist(list):
    max_var=0#setting max to 0
    if list==[]:#base case,if the list is empty
        return max_var
    else:
        max_var=list.pop()#if not empty,then popping
        a=maxlist(list)#not necessary,for clarity
        if a>max_var:#checking if the new variable is greater than max
            max_var=a#updating max
    return max_var#final return

l=[1,4,5,2,3,1]
print(maxlist(l))


    
    