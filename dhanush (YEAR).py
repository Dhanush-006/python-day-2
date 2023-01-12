b=float(input("enter the year"))
a=int(b)
if a>b:
    if a%400==0 or a%4==0:
        print("the year is a leap year!")
elif a%4==1:
    print("given year is non leap year !")
    print ("leap year is:,",a-1)
elif a%4==2:
    print("given year is non leap year!")
    print("leap year is :,",a-2)
elif a%4==3:
    print ("given year is non leap year!")
    print ("leap year is :,",a-3)
else:
    print("the year can not be zero or negative!")
