'''
#1)Creating of list:
a = [1,23,45,68]
print(a)
b=list((1,23,4,5,7,98))
print(b)

#2) Accessing of list: Index 0,-1
a[1,23,45,68]
print(a[1])
print(a[2])
print(a[-1])

#3)Creating list with repeated elements
a=[1,2,3]
print(a*2)

#4)Adding element to a list
a=[1,2,3]
a.append(50)
a.insert(1,20)
print(a)

#5) Removing elements from list
b=list((1,2,3,4,5))
print(b)
b.remove(3)
print(b)
'''
#creation of set
a=[1,2,3,4,5,6]
print(a)
b=set([1,2,3,4,5])
print(b)
 # Adding element in set
b=set([1,2,3,4,5])
b.add(50)
print(b)

#Removing
b=set([1,2,3,4,5])
b.remove(4)
print(b)

#set operations
a={1,2,3,4,5,6}
b={1,5,4,3,6,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#tuple
t=(1,2,3,4,5)
print(t)
#Acessing of tuples
#concatenation
t1=(2,3,4,5)
t2=(5,6,7,8)
print(t1+t2)
#nesting of tuples
t1=(1,23,45,67)
t2=(23,4,5,67,89)
print(t1,t2)
#repetition of tuples
t1=(1,2,3,4)
print(t1*3)
#slicing of tuples
t1=(1,23,45,67,89)
print(t1[1:])
print(t1[0:3])
print(t1[::-1])

#Deleting a tuple
t1=(1,23,45,66)
del t1

#creation ({},dict())
d = {'name':'Bharath','age':18}
print(d)
d=dict(name='Bharath',age=18)
print(d)

#acessing dict items (key[],get()):
#adding & updating dict items
d={'name':'Bharath','age':18}
d=['phn'] = 76567565
print(d)
# Removing dict items(de,pop()-->)
d={'name':'bharath','age':18}
del d['age']
d.pop('name')
print(d)
d.clear
print(d)