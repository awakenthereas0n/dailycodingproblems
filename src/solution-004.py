# April 9, 2021
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def lowestPosInt(A):
    m = max(A)
    if(m < 1):
        return 1
    if(len(A) == 1):
        return 2 if A[0] == 1 else 1       
    
    l = [0] * m 
    for i in range(len(A)): 
        if A[i] > 0: 
            if l[A[i] - 1] != 1: 
                #Changing the value status at the index of list A
                l[A[i] - 1] = 1 
    
    for i in range(len(l)):
        if l[i] == 0:  
            return i+1
    return i+2 

A = [3, 4, -1, -2]
print(lowestPosInt(A))

A = [0, 10, 2, -10, -20] 
print(lowestPosInt(A))

