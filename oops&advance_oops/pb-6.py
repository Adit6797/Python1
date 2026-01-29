# Print values in vector form using inheritance.
class Vector2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def display(self):
        print(f"{self.i}i + {self.j}j")
class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def display(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

a=Vector2D(2,3)
ans=Vector3D(2,3,4)

a.display()
ans.display()