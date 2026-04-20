#digital root
def Digital_root(n):
    if n <= 9:
        return n
    s = sum([int(i) for i in str(n)])
    return Digital_root(s)
print(Digital_root(456))
def is_Sorted_Array(nums):
    pass
print(is_Sorted_Array([10,20,30,40,50]))
print(is_Sorted_Array([10,20,30,40,50]))