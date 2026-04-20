#find sum of array elements
def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1):
        s += nums[i]
    return s
print(Array_sum([10,20,30,40]))
def Array_Sum_Recursion(nums,i):
    if i == -1:
        return 0 
    return nums[i] + Array_Sum_Rescursion(nums,i-1)
print(Array_Sum_Recursion([10,20,30,40]))
def Array_Sum_recursion1(nums):
    if len(nums) == 0:
        return 0 
    return nums[-1] + Array_Sum_recursion1(nums[])
#reverse the array using recursion
def Reverse_Array([1,2,3,4,5])
def Reverse_Array(nums,i,j):



def Reverse_String(st):
    if st == "":
        return ""
    return st[-1] + Reverse_String(st[:-1])


print(Reverse_String("abc"))
def is_palindrome
