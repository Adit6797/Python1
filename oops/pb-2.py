class calculator:
    def square(self, num):
        ans=num*num
        return ans
   
    def cube(self, num):
        ans=num*num*num
        return ans
       
    def root(self, num):
        ans=num**0.5
        return ans

obj=calculator()
print(obj.square(4))
print(obj.cube(3))
print(obj.root(16))
