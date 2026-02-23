''''
li = [1,2,3,4,5]
#output = [1,4,9,16,25]
res = []
for i in li:
    res.append(i**2)
print(res)
this is anoother 
li = ['a','b','c',]
res = ""
for ch in li:
    res = res + ch + " "
print(res)
print(" ".join(li))
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
