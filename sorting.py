def sort_list(list): 
    for i in range(len(list)): 
        min_index = i 
        for j in range(i + 1, len(list)): 
            if list[min_index] > list[j]: 
                min_index = j 
        list[i], list[min_index] = list[min_index], list[i] 
    return list

list = [5,1,4,2,8]

print(sort_list(list)) 