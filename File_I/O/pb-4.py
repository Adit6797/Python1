with open ("donkey.txt") as f:
    word=f.read()

nword=word.replace("donkey","#######")
if "donkey" in word:
    with open ("donkey.txt","w") as f:
        f.write(nword)
