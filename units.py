unit=int(input("enter number of units  :"))
if(unit<50):
  amt=unit*0.50
elif(unit<=150):
  amt=25+((unit-50)*0.75)
elif(unit<=250):
    amount=100+((unit-150)*1.20)
else:
      amt=220+((unit-250)*1.50)
      print("amount=",amt)
      surcharge=amt*0.20
      print("surcharge=",surcharge)
      tot_amt=amt+surcharge
      print("total=",tot_amt)