x =[]
t = 0
print(type(x))
for i in range(1,6):
    print("Input#%d :" %(i), end= "")
    y = int(input())
    x.append(y)
choice = input("Select the option: 1) Summary, 2) average, 3) min, 4) max ....")
if choice == "1":
   x = sum(x)
elif choice =="2":
    x = sum(x)/5
elif choice =="3":
    x = min(x)
elif choice =="4":
    x = max(x)

print("Your result is",x)
