with open("C:\\Users\\ag065\\OneDrive\\Dokumen\\python\\File_I\\O\\poem.txt","r") as f:
    content=f.read().lower()
    if "twinkle" in content:
        print("Word found in the poem")
    else:
        print("word not found in the poem")