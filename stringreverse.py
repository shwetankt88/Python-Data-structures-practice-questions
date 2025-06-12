#reverse a string
def reverseString(str):
    final_str=""#will be returned finally
    if len(str)==1:#base case
        return str
    else:
        s=str[-1]#accessing last element
        
        final_str=final_str+s#updating final string
        return final_str + reverseString(str[:-1])#recursively calling the function on rest of the string
print(reverseString("banana is a very good fruit"))
    