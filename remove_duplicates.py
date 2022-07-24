def remove_duplicates(array):
    final_list = []
    for num in array:
        if num not in final_list:
            final_list.append(num)
    return final_list
array = [1,1,2]
#array = [0,0,1,1,1,2,2,3,3,4]
#array = [1,1,1,1,1,1,1,1]
print(remove_duplicates(array))
