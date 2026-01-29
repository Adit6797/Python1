class employee:
    @staticmethod
    def __init__(self,salary):
        self.salary=salary
        
    
    def  increment(self,salary):
        if salary<=20000:
            new_salary=(salary*50)/100 + salary 
            return f"Your increamented salary={new_salary}"
        elif(salary>20000 and salary<=50000):
            new_salary=(salary*20)/100 + salary
            return f"Your increamented salary={new_salary}"
        else:
            return "You salary is sufficient!!"

    
a=employee()
print(a.increment(25000))
