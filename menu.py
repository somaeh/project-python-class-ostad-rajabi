import pyfiglet
import os

print(pyfiglet.figlet_format("phonenumber"))


menunumber = 1
path=r"D:\programing\پروژه پایتون کلاس آقای رجبی\phonebook.txt"

def addnumber(name,phone):
    file=open(path, "a+")
    file.write(name+":"+phone+"\n")
    file.close()
    print("save")
    input()
    
def showall():
    file=open(path, "r")
    for line in file:
        print(line)
    file.close()
    input()
def delete(name):
    file=open(path, "r")
    temp=""
    for line in file.readlines():
        if name!=line.split(":")[0]:
            temp+=line
        else:
            print("not found")
        file.close()
        file=open(path, "w")
        file.write(temp)
        file.close()
        print("delete successfuly")
        input()
    

def search(name):
    file=open(path, "r")
    for line in file.readlines():
        if name==line.split(":")[0]:
            print(line.split(":")[1])
        else:
            print("notfound")
    file.close()
    input()
def exit():
    pass

while menunumber != 5:
    os.system("cls")
    print(pyfiglet.figlet_format("phonenumber"))
    print("1)add number \n"+
          "2)show all \n"+
          "3)delete by name \n"+
          "4)search by name \n"+
          "5)exit \n") 
    menunumber=int(input("please chosse your number : "))
    
    if menunumber == 1:
        os.system("cls")
        print(pyfiglet.figlet_format("addmember"))
        name=input("inter your name : ")
        phone=input("inter your phonenumber : ")
        addnumber(name,phone)
        
        
    elif menunumber == 2:
        os.system("cls")
        print(pyfiglet.figlet_format("addmember"))
        showall()
    elif menunumber == 3:
        os.system("cls")
        print(pyfiglet.figlet_format("deletebyname"))
        name=input("inter your name for delete : ")
        delete(name)
        
    elif menunumber == 4:
        os.system("cls")
        print(pyfiglet.figlet_format("serachbyname"))
        name=input("inter your name for search : ")
        search(name)
    elif menunumber == 5:
        os.system("cls")