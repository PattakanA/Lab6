name = ["Satawat","Pisit","Thanaphong","Pished","Nut","Amon"]
for i in name:
    print("Student list: ",name)
    re = input("Please enter a student's name that you want to delete (q=exit) :")
    if re == "q":
        exit()
    else:
        print("You will remove '%s' from this class" %re)
        con= input("Please type (Comfirm 'y', Cancel 'n') ")
        if con =="y":
            name.remove(re)
        
   