n=int(input("enter a number :"))
cout=0
if n<=1:
    print("Not a prime number")

for i in range(1,n+1):
    if (n%i==0):
        cout += 1
if (cout==2):
    print("prime number")
else:
    print("Not a prime number")