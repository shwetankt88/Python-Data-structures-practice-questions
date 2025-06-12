def len_dict(list): 

    final_dict={}# empty dictionary which will be returned by the function 

    len_list=[]# list to contain the length of the corresponding elements of the parameter 

    count=0 
    temp_list1=[]
    temp_list2=[]


    for i in range(0,len(list)):#loop to put values in len_list 

        len_list.append(len(list[i])) 

    for i in range(0,len(list)):#loop to put key: value pairs in the dictionary
        if len_list[i] in final_dict:
            final_dict[len_list[i]].append(list[i])
        else:
            temp_list1.append(list[i])
            final_dict[len_list[i]]= temp_list1
            temp_list2=temp_list1
        temp_list1=[]


    return final_dict 

l= ["apple", "bat", "banana","dog"] 

print(len_dict(l))

 