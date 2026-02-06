'''
 1)write a python code to count the digits of numbers?
 ex:12345-->output:5

n=int(input("enter number:"))
count = 0
while n>0:
    count+=1
    n=n//10
print("number of digits:",count)

-->2)sum of the digits
n = int(input("enter a number:"))
sum = 0
while n>0:
    sum+=n%10
    n = n//10
print("sum of digits:",sum)

-->product of digits
n = int(input("enter a number:"))
product = 1
while n>0:
    product*=n%10
    n = n//10
print("product of digits:",product)

-->reverse of digits
n = int(input("enter a number:"))
reverse = 0
while n>0:
    reverse = reverse*10 + n%10
    n = n//10
print("reverse of digits:",reverse)

-->count the even and odd digits
n=int(input("enter n"))
even = 0
odd = 0
while n>0:
    d = n%10
    if d%2 == 0:
        even += 1
    else:
        odd += 1
    n//=10
print(even)
print(odd)
'''
#print the largest digit of a number?
