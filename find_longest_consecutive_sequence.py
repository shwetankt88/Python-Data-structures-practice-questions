#Longest Consecutive Sequence
#trying to create a conflict

def longestConsecutive(nums):
        fin_list1=[]
        fin_list2=[]
        nums.sort()#list sorted
        if len(nums)==0:
                return 0
        for i in range(0,len(nums)-1):
            
            if nums[i]+1==nums[i+1]:
                fin_list1.append(nums[i])
                
            elif nums[i]==nums[i+1]:
                continue
                print("")

            elif nums[i]+1 != nums[i+1] and nums[i]-1==nums[i-1]:
                fin_list1.append(nums[i])
                if len(fin_list1) > len(fin_list2):
                    fin_list2 = fin_list1 
                fin_list1=[]

                

            
            
        return fin_list2

l=[100, 4 , 200, 1, 3, 2,101,102,103,104,105,106,107,108 ,20,30,40,50,60,61,62,63,5,6,7,8]
print(longestConsecutive(l))



""""Pseudocode
FUNCTION longestConsecutive(nums)
    SET temp_list to empty list
    SET final_list to empty list
    SORT nums
    IF nums is empty
        RETURN 0
    END IF
    FOR i from 0 TO len(nums)-1
        IF nums[i]+1 EQUALS nums[i+1] THEN
            APPEND num[i] TO final_list1
        END IF
        ELIF nums[i] EQUALS nums[i+1] THEN
            CONTINUE
        END ELIF
        ELIF nums[i]+1 does not EQUALS nums[i+1] AND nums[i]-1 EQUALS nums[i-1] THEN
            APPEND nums[i] TO fin_list1
            IF len(final_list1) is greater than len(final_list2) THEN
                SET fin_list2=final_list1
            END IF
            SET final_list1 TO empty  
        END ELIF
    END FOR
    RETURN final_list2       
"""