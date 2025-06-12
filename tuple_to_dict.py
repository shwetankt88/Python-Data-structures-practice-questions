#you have a list of tuples , with unique values,with first element as key and second element of the tuple as value,
##create a dictionary
def tuple_to_dict(input_list):
    final_dict={}
    for i in input_list:#iteration
        final_dict[i[0]]=i[1]#assigning values10
    return final_dict

print(tuple_to_dict([("a", 1), ("b", 2), ("c", 3)]))
