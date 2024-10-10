txt = input("Enter a string: ")
new =""
for i in txt:
    if i.isupper():
        x = i.lower()
        new+=x
    else:
        x = i.upper()
        new+=x
print(new)
