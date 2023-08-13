names=[]
phone_num=[]
print("-------------------------------------------")
print("         Welcome to contact file           ")
print("-------------------------------------------")

i=0
while i<100:
 print("        \n *** Chose what do you want***\n")
 print("           1- Add New Item\n ")
 print("           2- Update Item \n")
 print("           3- Delete Item \n")
 print("           4- Display ALL Items \n")
 choice=int(input("\n please enter the number:"))
 if choice==1:
    name=input("\n please enter the name:")
    names.append(name)
    number=int(input("\n please enter the number:"))
    phone_num.append(number)
    print(names,phone_num)
    i+=1
 elif choice==2:
    search_name=input("\n please enter the name that you want to edit it :")
    for search_name in names:
        new_name=input("\n please enter the new name")
        new_number=int(input("\n please enter the new number"))
        index=int(names.index(search_name))
        names[index]=new_name
        phone_num[index]=new_number
        print("\n"+new_name+"  "+str(new_number))
        print(names,phone_num)
 elif choice==3:
    search_name=input("\n please enter the name that you want to delete it :")
    for search_name in names:
     x=int(names.index(search_name))
     names.remove(search_name)
     remove_num=phone_num[x]
     phone_num.remove(remove_num)
     print(names,phone_num)
     break

 elif choice==4:
   print("===============================================")
   for i in range(len(names)):

      print("\n\t\t"+names[i]+"      "+str(phone_num[i]))
      print("===============================================")
      
      






