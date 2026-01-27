def remove(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["apple","banana","apple","cherry"]

print(remove(l,"a"))