#to tell if a a tuple is present in a given list of tuples
def is_tuple_in_list(input_list,input_tuple):
    for i in input_list:#iterating
        if i==input_tuple:#if current element is equal to input tuple
            return True
     
    return False#false outside the loop,important bc otherwise it would return the value of the last element
           
    
        
print(is_tuple_in_list([(1, 2), (3, 4), (5, 6)],(6,4)))
print(is_tuple_in_list([(1, 2), (3, 4), (5, 6)],(3,4)))