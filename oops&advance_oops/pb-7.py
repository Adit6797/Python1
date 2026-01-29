class animals:
    def __init__(self):
        pass
class pets(animals):
    def __init__(self):
        print("This is a pet animal.")
class dogs(pets):
    def __init__(self):
        super().__init__()
    def bark(self):
        return "Woof! Woof!"
    

a=dogs()
print(a.bark())