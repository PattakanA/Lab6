import random as r
x = []
for i in range(1,5):
    print("Enter string#%d: "%i,end = "")
    y = input()
    x.append(y)
txt = r.shuffle(x)
txt = " ".join(x)
print("Random order of sentence",txt)