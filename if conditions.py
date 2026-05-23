"""if
if-else
if-elif
if-elif-else
multiple-elif
multiple-if
nested -if"""
#conditions
#if condition by using comparision operators
#<,>,<=,>=,==,!=

"""a=4
b=8
if(a<b):
    print("true")"""


"""a=4
b=8
if(a>b):
    print("true")"""


"""a=5
b=6
if(a<=b):
    print("true")"""


"""a=5
b=6
if(a>=b):
    print("true")"""



"""a=6
b=6
if(a==b):
    print("equal")"""


"""a=6
b=5
if(a!=b):
    print(" not equal")"""



"""a="python"
b="java"
if(a==b):
    print("java and python same")"""


"""a="python"
b="java"
if(a!=b):
    print("java and python not same")"""


"""a=input()
b=input()
if(a==b):
    print("java and python same")"""




#if-condition by using logical operators


"""a=56
b=65
if(a<=56 and b>=65):
    print("true")"""


"""a=56
b=65
if(a<b and a>b):
    print("true")"""


"""a=5
b=10
if(a!=b and b==a):
    print("true")"""


"""a=5
b=10
if(a<5 or b>10):
    print("true")"""


"""a=5
b=10
if(a<=5 or b>10):
    print("true")"""


"""a=10
b=34
if(a!=b or a==b):
    print("true")"""


"""a=10
b=36
if not (a>b):
    print("empty")"""

"""a=10
b=36
if not (a<b):
    print("empty")"""


"""a=int(input())
b=int(input())
if a==b or a!=b:
    print("true")"""


"""a=10
b=10
if not (a>b or a==b):
    print("empty")"""

#if-condition by using identify operators


"""a=6
if type(a) is int:
    print("it is int")"""

"""a=6
if type(a) is not int:
    print("it is not")"""
    
"""a=int(input("enter a value:"))
if type(a)is int:
    print("true")"""


"""a=float(input("enter avalue:"))
if type(a)is float:
    print("its float")"""

"""a=56.9
if type(a) is  float:
    print("it is float")"""


"""a=56.9
if type(a) is not float:
    print("it is int")"""    


"""a="5"
print(type(a))"""






#if  condition by using membership operators
#in ,not in

"""a=[10,20,30,40,50,60]
if 40 in a:
    print("true")
    
a=[10,20,30,40,50,60]
if 00  not in a:
    print("00 is not in the list of a")

a=[10,20,30,40,50,60]
b=int(input("enter a number:"))
if b in a:
    print("true")"""


"""a=3
b=6
if a<b:
    print("less")
else:
    print("true")

a=3
b=6
if a>b:
    print("less")
else:
    print("true")"""

"""a=3
b=6
if a>b and a<b:
    print("less")
else:
    print("true")"""


"""a=3
b=6
if a>b or a!=b:
    print("less")
else:
    print("true")"""


"""a=3
b=6
if not a>b:
    print("less")
else:
    print("true")"""


"""a=6
if type(a) is int:
    print("it is int")
else:
    print("it is string")


a=6
if type(a) is  not int:
    print("it is int")
else:
    print("it is str")"""
    


"""a=[10,20,30,40,50,60]
if 40 in a:
    print("true")
else:
    print("false")

    
a=[10,20,30,40,50,60]
if 40  not in a:
    print("true")    
else:
    print("false")"""
    
#if-elif-else


"""a=5
b=6
if (a<b):
    print("less")
elif(a>b):
    print("greater")
else:
    print("true")
    
a=7
b=6
if (a<b):
    print("less")
elif(a>b):
    print("greater")
else:
    print("true")    
    
a=7
b=6
if (a==b):
    print("less")
elif(a<b):
    print("greater")
else:
    print("true")"""

"""a=5
b=8
if (a<b):
    print("less")
elif(b>a):
    print("greater")
elif a==b:
    print("true")
    
a=5
b=8
if (a<b and a==b):
    print("less")
elif(b>a):
    print("greater")
elif a==b:
    print("true")    


a=5
b=8
if (a<b):
    print("less")
elif(b>a or a==b):
    print("greater")
elif a==b:
    print("true")


a=5
b=8
if  not (a<b):
    print("less")
elif(b>a):
    print("greater")
elif a==b:
    print("true")"""




"""a=[10,20,30,40,50]
b=int(input())
c=int(input())
if b in a:
    print("true")
elif c==b:
    print("false")
    
a=[10,20,30,40,50]
b=int(input())
c=int(input())
if b  not in a:
    print("true")
elif c==b:
    print("false")"""



"""a="chandrika"
if type(a) is int:
    print("it is int")
elif type(a is str):
    print("it is str")


#multiple-if
a=8
b=10
if a<b:
    print("less")
if b>a:
    print("grater")
if a!=b:
    print("not equal")"""
    
"""a="chandrika"
if type(a is str):
    print("it is int")
if type(a is str):
    print("it is str")
    
a=[10,20,30,40,50]
b=int(input())
c=int(input())
if b in a:
    print("true")
if c==b:
    print("a and b are same")"""

#nested-if
"""a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")
a=5
b=10
if a==b:
    print("less")
    if b>a:
        print("greater")"""

"""a=5
b=6
if a<b:
    print("less")
    if a==b:
        print("false")
    else:
        print("true")

a=5
b=6
if a>b:
    print("less")
    if a==b:
        print("false")
    else:
        print("true")
else:
    print("greater")"""
    
        
"""a=5
b=6
if a<b:
    print("less")
    if a==b:
        print("false")
    elif(a<b):
        print("true")
else:
    print("greater")"""

#voting

"""age=int(input())
if(age>=18):
    print("there are eligible for vote")
else:
    print("Not eligible")"""



#even or odd
"""number=int(input())
if(number%2==0):
    print("even")
else:
    print("odd")"""




#leap year
"""year=int(input())
if(year%4==0):
    print("leap year")
else:
    print("not a leap year")"""




#vowels
"""s=input().lower()
if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
    print("it is vowel")
else:
    print("consonant")"""



#guest code
"""name=input()
if(name=="pooja"):
    print("welcome",name)
else:
    print("welcome guest")"""




#
"""name=["chandrika","chandu","chinni"]
a=input()
if a in name:
    print("welcome",a)
else:
    print("welcome guest")"""


"""user name=pooja
password=1234
it is match
login succes
not matched
not login successfully
both if and nested if"""


#if-else
"""a="pooja"
b="1234"
username=input()
password=input()
if(username==a and password==b):
    print("login successfully")
else:
    print("not login successfully")"""



#nested -if
"""a="pooja"
b="1234"
username=input()
password=input()
if(username==a):
    if(password==b):
        print("login successfully")
    else:
        print("not login successfully")
else:
    print("invalid user name and password")"""

#bakery
"""c=int(input())
if(c==1200):
    print("redvelwet")
elif(c==1000):
    print("choclate cake")
elif(c==800):
    print("almond cake")
elif(c==600):
    print("buttercotch")
elif(c==400):
    print("normal cake")
else:
    print("sorry cake is not available")"""

"""#pizza
p=input()
if(p=="bbq pizza"):
    print("1000")
elif(p=="crispy chicken pizza"):
    print("800")
elif(p=="panner pizza"):
    print("600")
elif(p=="corn pizza"):
    print("400")
elif(p=="French fries&coke"):
    print("200")"""




















































