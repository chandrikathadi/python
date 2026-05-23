#functions
"""a=10
b=20
print("sum:",a+b)
print("diff:",a-b)
print("product:",a*b)
a=100
b=200
print("sum:",a+b)
print("diff:",a-b)
print("product:",a*b)
a=1000
b=2000
print("sum:",a+b)
print("diff:",a-b)
print("product:",a*b)"""


"""def chandrika(a,b):
    print("sum:",a+b)
    print("diff:",a-b)
    print("product:",a*b)
chandrika(10,20)
chandrika(100,200)
chandrika(1000,2000)"""


"""def chandrika(a,b):
    print("power:",a**b)
    print("modules:",a%b)
    print("division:",a//b)
chandrika(2,3)
chandrika(5,4)
chandrika(6,7)"""

"""def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()"""


"""def fullname():
    fname=input("enter fname:")
    lname=input("enter lname:")
    print(fname+" "+lname).title()
fullname()"""

#print v/s return
"""def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(3,5)"""    
    

"""def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(3,5))"""

"""def cal(a,b):
    print("1.add\n","2.sub\n","3.mul")
    c=int(input())
    if(c==1):
        print("add",a+b)
    elif(c==2):
        print("sub",a-b)
    elif(c==3):
        print("mul",a*b)
cal(2,3)"""


"""def add():
    return a+b
def sub():
    return(a-b)
def mul():
    return(a*b)
while True:
    a=int(input("enter a"))
    b=int(input("enter b"))
    option=int(input("1.add,2.sub,3.mul"))
if(option==1):
    add()
elif(option==2):
    sub()
elif(option==3):
    mul()"""


"""def splitbill():
    a=int(input("no of friends:"))
    amount=int(input("amount:"))
    b=amount/a
    print(b)
splitbill()"""

"""while True:
    def splitbill():
        a=int(input("no of friends:"))
        amount=10000
        b=amount//a
        print("total amount for person {}".format{b})
    splitbill()"""


#ATM
"""while True:
    amount=100000
    card="c"
    password=1234
    n=input("insert the card:")
    if(n==card):
        print("welcome chandrika")
        c=int(input("enter password:"))
        if(password==c):
            options=int(input("#choose the option 1.balance enq 2.withdraw:"))
            if(options==1):
                print("Balance is:",amount)
            elif(options==2):
                f=int(input("enter the withdraw amount:"))
                if(amount>f):
                    d=amount-f
                    print("withdraw amount:",f)
                    print("avaliable balance is :",d)
                else:
                     print("amount is not sufficent")
            else:
                 print("option is in valid")
        else:
             print("password is in correct")
    else:
        print("invallid card")"""

        
#keyword and positional arguments
"""def details(id,name,mailid):
    id=10
    name="chandrika"
    mailid="cahndrika@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")"""

"""def details(id,name,mail):
    print(id,name,mail)
details(40,"chandu","chandu@gamil.com")
details(id=20,name="cahndu",mail="c@gamil.com")
details(id=30,name="chinni",mail="k@gamil.com")
details("pavani","p@gmail.com",70)
details(name="pavani",mail="p@gmail.com",id=70)"""


#default arguments
def store(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
store( "rice",200)

def store(item="sweet",price=400):
    print("item is %s" %item)
    print("price is %.2f" %price)
store()

def store(item,price=400):
    print("item is %s" %item)
    print("price is %.2f" %price)
store("honey")

"""def store(item="sweet",price):
    print("item is %s" %item)
    print("price is %.2f" %price)
store(500)"''"

#cake ,price ,qty
"""def chandu(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is  %d" %qty)
chandu("honey almond",900,1)

def chandu(cake="honey",price=800,qty=2):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is  %d" %qty)
chandu()


def chandu(cake,price,qty=3):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is  %d" %qty)
chandu("honey almond",500)


def chandu(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is  %d" %qty)
chandu(cake="honey almond",price=900)"""   
        
        

#*argument-> is used to unpack the elements
"""a=[1,2,3,4]
print(a)
print(*a)
print(type(a))"""

"""a=(1,2,3,4)
print(a)
print(*a)
print(type(a))"""

"""a={1,2,3,4}
print(a)
print(*a)
print(type(a))"""


"""a={"year":2026,"month":5}
print(a)
print(*a)
print(type(a))"""

"""a,b,c=1,2,3,4,5
print(a)
print(b)
print(c)"""#error

"""a,*b,c=1,2,3,4,5
print(a)
print(*b)
print(c)"""

"""*a,b,c=1,2,3,4,5
print(*a)
print(b)
print(c)"""

"""*a,*b,c=1,2,3,4,5
print(*a)
print(*b)
print(c)"""#error

"""a="codegana"
print(a)
print(*a)"""

"""a,b,c="cod"
print(a)
print(b)
print(c)"""

"""a,*b,c="codegnan"
print(a)
print(*b)
print(c)"""


"""#attendance
n=int(input("enter number: "))
p=0
a=0
for i in range(1,n+1):
    f=input("sudent{}:".format(i))
    if f=="p":
        p=p+1
    else:
        a=a+1
print("total students:",n)
print("total present:",p)
print("total absent:",a)"""

#variable length argments are automatically stores in tuples and we use the **args

#variable length arguments
"""def check(*a):
    print(a)
    print(type(a))
check()
check(3,4,5,7)
b=[1,2,3,4,5]
check(*b)
c={12,34,5,6}
check(*c)
d={"name":"chandu","birthday":6}
check(*d)"""

"""def check1(*a):
    b=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            b=b+i
            print(b)
check1()
check1(2,3,4,5.6,"pooja")"""


"""#kwargs(**)
def details(**a):
    print(a)
    print(type(a))
details()
d={"id":[10,20,30],
   "names":["pooja","chandu","chinni"],
   "status":["a","b","c"]}
details(**d)"""

"""def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"id":[10,20,30],
   "names":["pooja","chandu","chinni"],
   "status":["a","b","c"]}
details(**d)"""

"""def final(*a,**b):
    d=1
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is:",i)
        print("values is:",j)
final()
data=[2,3,4,5,6.7,8.9,"cahndu",4+5j,True]
final(*data)        
d={"id":[10,20,30],
   "names":["pooja","chandu","chinni"],
   "status":["a","b","c"]}
final(**d)"""

"""#Marks Analysis Report
n=int(input())
marks=[]
for i in range(1,n+1):
    f=int(input("students{}:".format(i)))
    marks.append(f)
total_marks=sum(marks)
average=total_marks/n
print("total no.of students:",n)
print("total marks:",total_marks)
print("heighest marks:",max(marks))
print("lowest marks:",min(marks))
print("Average marks:",average)"""

#global variables and local variables
"""a=3
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)


a=2
def check2():
    a=5
    a=a**4
    print("inside value is:",a)
check2()
print("outside value is:",a)"""

#third case of both global and local varibles
"""a=10
def check3():
    a=5
    print("inside value is:",a)
    a=10
    print("updated value is:",a-5)
    b=20
    b=b-a
    print("value os b:",b)
check3()
print("value of a:",a)
prnt("value of b:",b)"""
    
"""a=10
b=20
def check3():
    a=5
    print("inside value is:",a)
    a=10
    print("updated value is:",a-5)
    b=20
    b=b-a
    print("value os b:",b)
check3()
print("value of a:",a)
print("value of b:",b)"""

#usage of global keyword
"""a=5
def final():
    global a
    print("inside value:",a)
    a=15
    print("udate the value:",a)
    b=20
    b=b+a
    print("value of b:",b)
final()
print("a value is:",a)
print("b value is:",b)"""

"""a=5
def final():
    global a,b
    print("inside value:",a)
    a=15
    print("update the value:",a)
    global b
    b=20
    b=b+a
    print("value of b:",b)
final()
print("a value is:",a)
print("b value is:",b)"""

#geberators
#a=[exp  for var in colllection /range]
"""a=[i for i in range(30)]
print(a)
print(type(a))

a=(i for i in range(30))
print(a)
print(type(a))

a=(i for i in range(30))
print(*a)
print(type(a))

a=(i for i in range(30))
print(list(a))
print(type(a))

a=(i for i in range(30))
print(set(a))
print(type(a))

a=(i for i in range(30))
print(tuple(a))
print(type(a))"""


#yield v/s return
"""a,b=[int(x) for x in input("enter value:").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))    

a,b=[int(x) for x in input("enter value:").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        #yield a
print(*check(a,b))
    
a,b=[int(x) for x in input("enter value:").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))"""

"""def mygen():
    #return "python"
    #return "java"
    #return "dsa"
    return "python","java","dsa"
print(*mygen())


def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())"""

#next()
"""def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())
d=mygen()
print(next(d))
print(next(d))
print(next(d))"""


"""def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))"""
























































