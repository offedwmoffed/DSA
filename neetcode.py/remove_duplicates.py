def remove_duplicates(my_list:list):
    items=set()
    i = 0
    z = len(my_list)
    number = 0
    while i < z:
        if my_list[i] not in items:
            items.add(my_list[i])
            i += 1
            number += 1
        else:
            my_list.pop(i)
            my_list.append("_")
            z -= 1
    return number


        
    
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))



