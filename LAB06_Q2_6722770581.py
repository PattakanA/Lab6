x = input("Enter a comma-separated list: ").split(",")
m = []
for i in x:
    for j in x:
        for k in x:
            if i!=j and i != k and j!=k:
                s = sorted([i,j,k])
                if s not in m:
                    print(i,j,k)
                    m.append(s)