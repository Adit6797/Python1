word=["donkey","freind","bad"]
with open ("donkey.txt") as f:
    word=f.read()
for i in word:
    nword=word.replace(word,"#######")
    if i in word:
        with open ("donkey.txt","w") as f:
            f.write(nword)