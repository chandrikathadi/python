
sno=input("enter sno  :")
sname=input("enter sname  :")
sclass=input("enter sclass  :")
ssec=input("enter ssec  :")
m1=int(input("enter m1  :"))
m2=int(input("enter m2  :"))
m3=int(input("enter m3  :"))
m4=int(input("enter m4  :"))
m5=int(input("enter m5  :"))
m6=int(input("enter m6  :"))
total=m1+m2+m3+m4+m5+m6
avg=total/6
print(".........................")
print("\t marks report")
print("............................")
print("sno=",sno,"\t" "sname=",sname)
print("sclass=",sclass, "\t" "ssec=",ssec)
print("...........................")
print("m1=",m1 ,"\t" "m2=",m2)
print("m3=",m3 ,"\t" "m4=",m4)
print("m5=",m5 ,"\t" "m6=",m6)
print("........................")
print("total marks=",total)
print("average marks=",avg)
print(".......................")
if(m1<35 or m2<35 or m3<35 or m4<35 or m5<35 or m6<35):
  print("result=fail")
  print("grade=no grade")
elif(avg>65):
  print("result=pass")
  print("grade=A")
elif(avg<65 and avg>=45):
  print("result=pass")
  print("grade=B")
elif("avg<45 "):
  print("result=pass")
  print("grade=c")
  print("..........................")
