txt = input("Enter dd/mm/yyyy:")
if len(txt)==8:
    if  int(txt[2:4])<=12:
        print("Date =",txt[0:2])
        print("Month =",int(txt[2:4]))
        x  = txt[4:]
        x = int(x)-543
        print("Year =",x)
    else:
        print("Error! There're 12 months")
else:
    print("Please enter 8 digits")
