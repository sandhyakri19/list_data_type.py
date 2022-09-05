"""5th september 2022 monday"""
"""Topic: list data type"""

# a=[]
# print(type(a))  # 'list'

# b=[1,20]
# print(type(b))  #'list'

# c=[10,20,30]
# # print(c[26])  # IndexError: list out of range
# print(c[1])   # 20
# print(c[2])   # 30
# print(c[3])   # IndexError: list index out of range

# a='hee'
# # print(type(a))  #'str'
# a[0]='s' # TypeError:'str' object does not support item assignment

# b=['hello']
# print(type(b))  # 'list'
# print(b[0])  # hello

# b[0]='bye'  
# print(b) # ['bye']   

# a=[4,5,6]
# a[0]=70
# print(a)  # [70,5,6]

# b=[1,2,3]
# b[5]=10
# print(b)  # IndexError: list assignment index out of range

# x=[1,2,3]
# # x.append(4)  # [ append is used to all the element at the end of the the list]
# # print(x)  # [1,2,3,4]
# x.append(4,5)
# print(x)  # TypeError: list.append() takes exactly one argument (2 given)
 
# a=[10,20] 
# a.clear()
# print(a) # []

# y=[100,200,300,400]
# # y.remove(500)  # ValueError:list.remove(x): x not in list.remove(200)
# y.remove(200)
# print(y) # [100,300,400]

# c=[10,30,40,59]
# c.pop()
# print(c) #[10,30,40]

# c=[10,20,30,40,59]
# c.pop(2)
# print(c)  #[10,20,40,59]

# v=[10,20]
# v.add(40)
# print(v) # AttributeError: 'list' object has no attibute 'add'

# v=[10,20]
# n=[30,40,50]
# v.extend(n)
# print(v)  # [10,20,30,40,50]

# v=[10,20]
# n=[30,40,50,'hello']
# v.extend(n)
# print(v) # [10,20,30,40,50,'hello']

# r=[1,5,7]
# r.insert(0,3)
# print(r)  #[3,1,5,7]

# r.insert(1,3)
# print(r)  #[1,3,5,7]

# r.insert(10,3)
# print(r)  # [1,5,7,3]

# r.insert(2,'hi')
# print(r) # [1,5,'hi',7,3]

# r.insert(2,(70,80))
# print(r) # [1,5,(70,80),'hi',7,3]

# a=['hi',3,4,6,7,8,6]
# print(a.count('hi'))  # 1
# print(a.count('hey')) # 0
# print(a.count(6))     # 2

# h='python'
# print(h.index('p'))  # 0
# print(h.index('t'))  # 2
# print(h.index('v'))  # ValueError: substring not found

# h=['python',5,8,'hi']
# print(h.index('python')) # 0
# print(h.index(8))  # 2
# print(h.index('v'))  # ValueError: 'v' is not in list

# x=[10,20,30,40]
# x.reverse()
# print(x)  # [40,30,20,10]

# z=[3,8,2,8,11,4]
# z.sort()
# print(z)  # [2,3,4,8,8,11]

# z=[3,8,2,8,11,4]
# z.sort(reverse=False)
# print(z) # [2,3,4,8,8,11]

# z=[3,8,2,8,11,4]
# z.sort(reverse=True)
# print(z) # [1,8,8,4,3,2]




