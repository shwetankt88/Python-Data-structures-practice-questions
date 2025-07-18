#find no of unique words in a list of strings
def unique_words_in_string(str):
    temp_set=set()#empty set
    words=str.split()
    for i in words:
        if i not in temp_set:
            temp_set.add(i)# adding non duplicate elements
    return len(temp_set)#gives length
print(unique_words_in_string("this is a test this is only a test"))
#edited

