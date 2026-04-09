a = [1,2,5,8,9,832,15,63]
print(max(a))
#2} check the palindrome
s = input("enter the string")
if s == "".join(reversed(s)):
    print("Palindrome")