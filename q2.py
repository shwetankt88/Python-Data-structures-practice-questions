#make a dictionary with the lengths of the word taken from a list

def len_dict(list):
    final_dict={}# emptly dictionary which will be returned by the function
    len_list=[]# list to contain the length of the the corresponding elements of the parameter
    count=0
    for i in range(0,len(list)):#loop to put values in len_list
        len_list.append(len(list[i]))
    for i in range(0,len(list)):#loop to put key:value pairs in the dictionary
        final_dict[len_list[i]]= list[i]
    return final_dict

l= ["apple", "bat", "banana","dog"]
print(len_dict(l))