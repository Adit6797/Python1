def pattern(n):
    if(n==0):
        return
    else:
        print("*"*n)
    return pattern(n-1)

n=int(input("enter the Row of the pattern"))
pattern(n)
    