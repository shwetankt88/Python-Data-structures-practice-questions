#approach 2:removing duplicate elements


def rem_dup(list):
    l.sort()#iterating the list
    for i ,v in enumerate(l):#iterating over different elements
        if v==list[i-1]:#checking for duplicates
            list.remove(l[i])#removing duplicates
    return list


l=[1,1,2,2,3,4,4]
print(rem_dup(l))