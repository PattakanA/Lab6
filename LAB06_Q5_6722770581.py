a = []
b = []
c = []
num = int(input("how many person in group? : "))
print("please enter grade from group A")
for i in range(num):
    y = float(input("enter grade: "))
    a.append(y)
print("please enter grade from group B")
for i in range(num):
    y = float(input("enter grade: "))
    b.append(y)
print("please enter grade from group C")
for i in range(num):
    y = float(input("enter grade: "))
    c.append(y)
print("the highest grade in group A is",max(a))
print("the highest grade in group B is",max(b))
print("the highest grade in group C is",max(c))