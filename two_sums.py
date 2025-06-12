#to check if two elements in a list add up to a number
def two_sum(items, target):
    seen = set()#empty set
    for i in items:#iterating items
        if (target - i) in seen:#if the number is there in the list
            return True
        seen.add(i)
    return False
#this method is better because if we had only used lists, 
# then we would have to put two nested loops in the program to check the numbers

nums = [10, 15, 3, 7]
k = 17
print(two_sum(nums,k)) 
nums2 = [1, 2, 3, 9]
k2 = 8
print(two_sum(nums2,k2)) 