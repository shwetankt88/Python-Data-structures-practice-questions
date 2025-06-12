#flatten a given list

def flatten(list):
    final_list=[]
    for i in range(0,len(list)):#iterating the original list
        for j in range(0,len(list[i])):#iterating the inner list
            final_list.append(list[i][j])

    return final_list

l=[[1, 2], [3, 4], [5, 6]]
print(flatten(l))