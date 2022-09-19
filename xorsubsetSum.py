#Question 3: Sum of All Subset XOR Totals
# Python3 program to implement the approach
def rec(i, x, arr, size):
 
    if (i == size):
        return x
    
    choice1 = rec(i + 1, x ^ arr[i], arr, size)

    choice2 = rec(i + 1, x, arr, size)
 
    return choice1 + choice2
 
# Returns sum of XORs of all subsets
def xorSum(arr, size):
    return rec(0, 0, arr, size)
 
# Driver code
arr = [1, 5, 6]
size = len(arr)
 
# Function call
print(xorSum(arr, size))
