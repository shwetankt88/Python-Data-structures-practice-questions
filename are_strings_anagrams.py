# tell if letters of 2 strings are same
def are_strings_anagrams(string1,string2):
    set1=set(string1)
    set2=set(string2)
    #set bc in it order doesnt matter
    if set1==set2:#comparision
        return True
    else:
        return False
print(are_strings_anagrams("listen","silentanagram"))
print(are_strings_anagrams("liste","silent"))

