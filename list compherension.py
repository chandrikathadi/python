#list compherension
#every list compherension can be rewritten as a for loop  but every for loop can not be rewritten by compherension


a=["python","code","codegnan"]
"""b=str(a)
c=b.upper()
print(c)"""

"""for i in a:
    print(i.upper(),end=" ")"""


#syntax
#a=[expression for variable in collection/range]

"""a=[j.upper() for j in a]
print(a)"""


"""a=["vja","hyd","vzg"]
a=[j.title() for j in a]
print(a)"""

"""a=[1,2,3,5,6,8,12,13]
a=[j*j for j in a] or
a=[i**2 for i in a] or
a=[pow(i,2) for i in a]
print(a)"""


"""n=21
a=[i for i in range(n) if i%2==0]
print(a)"""

"""n=16
a=[i*i for i in range(n) if i%2==0 ]
print(a)"""


"""a=["apple","banana","grapes","mango","kiwi","dragon","berry"]

n=[i for i in a if "a"  not in i]
print(n)"""


#non-elif usage in list comprehension
#if-else usage in list comprehension
"""n=int(input())
a=[i*i if i%2==0 else i*5 for i in range(n)]
print(a)"""


#[6,6,6,6,6]
"""a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))] or range(5)
print(c)"""



































































    
