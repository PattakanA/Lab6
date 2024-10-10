List = ["Apple", "Banana", "Orange", "Grape", "Mango", "Kiwi"]
for i in List:
    n=0
    if len(i)>=6:
        print(i,"is 6 characters or more!")
    else:
        for j in i:
            n+=1
        print(i,"is only %d long!" %n)