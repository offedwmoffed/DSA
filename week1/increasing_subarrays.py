def count_long_subarrays(A:tuple):
    if type(A) == int:
        return 1
    longest_subarray = 1
    current_subarray = 1
    ls_reps = 1
    for index in range(1,len(A)):

        if A[index] <= A[index-1]:
            current_subarray = 0

        current_subarray += 1

        if current_subarray == longest_subarray :
            ls_reps += 1

        elif current_subarray > longest_subarray:
            longest_subarray = current_subarray
            ls_reps = 1

       
                
    return ls_reps


A =(1,3,4,2,7,5,6,9,8)
print(count_long_subarrays(A))




    
