def rec_rev(or_list):
    if or_list==[]:#if list is empty,return nothing
        return
     else:
         print(or_list.pop())#popping from the list and then calling it recursively
         rec_rev(or_list)
list_or=[1,2,3,4]
rec_rev(list_or)



