x = input("Enter a comma-separated list: ").split(",")
for i in x:
    for j in x:
        for k in x:
            if i!=j and i != k and j!=k:
                print(i,j,k)