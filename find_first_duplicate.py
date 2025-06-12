#to find the first duplicate number in the list
def find_first_duplicate(items):
    seen=set()#empty set
    for i in items:
        if i not in seen:
            seen.add(i)#adding items which are not in the list
        else:
            return i#if it finds an element which is in the set,that element is returned bc that would be the first duplicate

items = [2, 4, 3, 1, 5, 2, 4]#here,both 5 and 2 are duplicates but it should return 5 bc it is the first duplicate
print(find_first_duplicate(items))