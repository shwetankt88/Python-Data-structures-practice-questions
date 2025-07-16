#reverse a string
<<<<<<< HEAD
print("changes made by developer 2")
=======
print("change made by developer 1 on his own repository")
>>>>>>> 52b4528d09ee532ee95d92c54f97ed1943f1366c
def reverseString(str):
    final_str=""#will be returned finally
    if len(str)==1:#base case
        return str
    else:
        s=str[-1]#accessing last element
        
        final_str=final_str+s#updating final string
        return final_str + reverseString(str[:-1])#recursively calling the function on rest of the string
print(reverseString("banana is a very good fruit"))
    