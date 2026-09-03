new_list = [ 3,3]
target = 6
new_dic = {}

for index in range(len(new_list)):
    if target - new_list[index] in new_dic:
        indexes = [index,new_dic[target-new_list[index]]]
        break
    else:
        new_dic[new_list[index]]= index

print(sorted(indexes))


    