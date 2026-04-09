# # ###################### STRINGSSSSSSSSSSSSS #############################################
# # # str is imutable
# # # str is a sequence of characters
# # # str is a collection of characters
# # # """This is a multiline string"""
# # # 'This is a string'
# # # "This is a string"
# # # 'This is a string with a "double quote" inside'
# # # "This is a string with a 'single quote' inside"
# # # REPLACE A CHARACTER IN A STRING
# # # s = "python"
# # # print(s.capitalize()) # Python
# # # print(s) # python
# # # ##Built in functions in Strings
# # # # s = "python"  
# # # print(s.upper()) # PYTHON
# # # print(s.lower()) # python
# # # print(s.title()) # Python
# # # print(s.swapcase()) # PYTHON
# # # print(s.isupper()) # False
# # # print(s.islower()) # True
# # # print(s.istitle()) # False
# # # print(s.isalpha()) # True
# # # print(s.isdigit()) # False
# # # print(s.isalnum()) # True
# # # print(s.startswith("p")) # True
# # # print(s.endswith("n")) # True
# # # print(s.count("o")) # 1
# # # print(s.find("o")) # 4
# # # print(s.index("o")) # 4
# # # print(s.replace("o", "a")) # pythan
# # # print(s) # python
# # d
# ##################### REVERSING A STRING ######################################################################
# # def revstr(n):
# #     r = ""
# #     for i in range ( len(n)-1,-1 , -1):
# #         r += n[i] 
# #     return r
# # s = "python"
# # print(revstr(s))
# # #### 2nd way ##############
# def revstr(s):
#     r = ""
#     for i in s:
#         r = i + r     
#     return r

# ####### PALINDROME CHECKER ########################################################################################
# def is_pal(s):
#     return s == revstr(s)
# s = "pypo"
# print(is_pal(s))
#check wheather a string is a anagram or not
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)
# s1 = "listen"
# s2 = "silent"
# print(is_anagram(s1, s2))
# by using frequncy count
# def is_anagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     freq1 = {}
#     freq2 = {}
#     for i in s1:
#         freq1[i] = freq1.get(i, 0) + 1
#     for i in s2:
#         freq2[i] = freq2.get(i, 0) + 1
#     return freq1 == freq2   
# s1 = "listen"
# s2 = "silent"
# print(is_anagram(s1, s2))
def Reverse_str(s):
    res = ""
    for ch in s:
        res = ch + res
    return res
print(Reverse_str("abc"))
print(Reverse_str("pyhton"))
def Reverse_str1(s):
    res = ""
    stop = -1 * (len(s)+1)
    for i in range(-1,stop,-1):
        res = res +s[i]
    return res
print(Reverse_str("abc"))
print(Reverse_str("pyhton"))
def is_palindrome(s):
    return s == Reverse_str1(s)
    
print(is_palindrome("abc"))
print(is_palindrome("madam"))

def Frequency_count(s):
    d = {}
    for ch in s :
        if ch not in d :
            d[ch] = 1
        else:
            d[ch] += 1
    return d 
print(Frequency_count("abcabc")) 
def Anagrams(str1,str2):
    return Frequency_count(str1) == Frequency_count(str2)
print(Anagrams("paces","space"))
print(Anagrams("aabbcc","abc"))
from collections import Counter
print(Counter("aabbcc"))