def greatestnum():
    a=int(input("Enter the Number"))
    b=int(input("Enter the Number"))
    c=int(input("Enter the Number"))
    if(a>b and a>c):
        print(f"{a} is the Greatest number")
    elif(b>a and b>c):
        print(f"{b} is the Greatest number")
    else:
        print(f"{c} is the Greatest number")

greatestnum()