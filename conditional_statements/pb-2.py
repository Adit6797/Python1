sub1=int(input("Enter marks of subject 1: "))
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 2: "))

persentage=(sub1+sub2+sub3)/3

if(persentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("You have passed the exam")
else:
    print("you are failed")