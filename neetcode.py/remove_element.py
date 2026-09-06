def remove_element(nums:list, val:int):
        i = 0
        z = len(nums)
        deleted = 0
        while i < z:
            if nums[i] != val:
                i += 1
                deleted+= 1
            
            else:
                nums.pop(i)
                nums.append("_")
                z -= 1
                

        return deleted


print(remove_element([1,2,2,3,4,55,2],2))