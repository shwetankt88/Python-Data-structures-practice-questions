#replace any third character given by the user with a $ sign
def replace_third_element(str):
    final_str = ""
    for i, v in enumerate(str):#iterating
        final_str =final_str + v#appending the current element

        if (i + 1) % 3 == 0:#if the current elememts index is the third index 
            final_str=final_str + "$"#if yes,then we added the special character which is $
    return final_str
print(replace_third_element("banana is a very good fruit"))




