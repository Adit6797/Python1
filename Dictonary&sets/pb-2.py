dictionary = {
    "pyaar": "love",
    "kitab": "book",
    "paani": "water",
    "dost": "friend",
    "ghar": "home",
    "khana": "food",
    "school": "school"
}

print("choose a option:", dictionary.keys())

word = input("Enter a word in hindi: ").lower()
print("Meaning:", dictionary[word])


