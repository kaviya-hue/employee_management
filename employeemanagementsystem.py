dict={}

def add_employee():
    number=int(input("enter how many data:"))
    for i in range(number):
        id=int(input("enter id "))
        name=input("Enter name : ")
        salary=int(input("Enter salary :"))
        
        dict[id]={
            "name":name,
            "salary":salary
        }
    print(dict)


def view_employee():
    print("Displaying employees")
    print(dict)


def update_employee():
    id=int(input("Enter id to be updated"))
    
    if id in dict:
        name=input("Enter name : ")
        salary=int(input("Enter salary :"))
        
        dict[id]["name"]=name
        dict[id]["salary"]=salary
        
        print(dict)
        print("Updated successfully")
    else:
        print("ID not found")


def search_employee():
    id=int(input("Enter id to be searched:"))
    
    if id in dict:
        print(dict[id])
    else:
        print("NOT FOUND")


def exit_employee():
    print("Program exited")


while True:
    print("1. Add 2.Display 3.Update 4. Search 5.Exit")
    choice=int(input("Enter choice :"))

    if choice ==1:
        add_employee()
    elif choice ==2:
        view_employee()
    elif choice==3:
        update_employee()
    elif choice==4:
        search_employee()
    elif choice==5:
        exit_employee()
        break