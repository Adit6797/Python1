# this program finds the second largest number in a list
arr = list(map(int, input().split()))
# map function is used to convert string inputs to integer list
# split function splits the input based on space by default
arr.sort()
    
print(arr[-2])