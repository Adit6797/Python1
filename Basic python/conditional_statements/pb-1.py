a=int(input("enter the first number:"))
b=int(input("enter the first number:"))
c=int(input("enter the first number:"))
d=int(input("enter the first number:"))

if(a>b and a>c and a>d):
    print("the greatest number=",a)
elif(b>a and b>c and b>d):
    print("the greatest number=",b)  
elif(c>a and c>b and c>d):
    print("the greatest number=",c)
else:
    print("the greatest number=",d)

