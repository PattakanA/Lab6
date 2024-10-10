a = []
b = []
c = []
h = 97
num = int(input("how many person in group? : "))
for x in [a,b,c]:
    print("please enter grade from group "+chr(h).upper())
    for i in range(num):
        y = float(input("enter grade: "))
        x.append(y)
    h+=1

print("the highest grade in group A is",max(a))
print("the highest grade in group B is",max(b))
print("the highest grade in group C is",max(c))
