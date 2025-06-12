def longest_consec(list):
    final_list=[]
    l.sort()#list sorted
    for i in range(0,len(list)-1):
        if list[i]+1 == list[i+1]:
            final_list.append(l[i])
        elif l[i]+1 != l[i+1]:
            final_list.append(l[i])
            break
    return final_list
       
l=[3,7,2,5,8,4,6,0,1]
print(longest_consec(l))