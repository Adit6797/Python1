text=input("Enter your message:").lower()

if("make a lot of money" in text or "buy now" in text or "subscribe this" in text  or "click here" in text ):
    print("spam detected !!!")
else:
    print("This is normal message")
