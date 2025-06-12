#find common languages between 2 developers
def find_common_language(list1,list2):
    set1=set(list1)
    set2=set(list2)#converting into sets
    set3=set1.intersection(set2)#finding the common elements
    return set3
list_a = ["python", "java", "c++", "ruby"]
list_b = ["javascript", "c++", "go", "python"]
print(find_common_language(list_a,list_b))
#why is this better than using a list?
#because the complexity of using a list here would be O(n^2)

