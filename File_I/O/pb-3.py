
def Gentable(n):
    tables=""
    for i in range(1,11):
        tables+=f"{n} X {i} = {n*i}\n"
    with open (f"tables/table_of_{n}.txt","w") as f:
        f.write(tables)

i=int(input("Enter the number to generate its multiplication table: "))
Gentable(i)