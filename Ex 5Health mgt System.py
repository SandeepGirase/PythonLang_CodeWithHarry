
#client_list = {1:"Harry",2:"Rohan",3:"Hammad"}
#log_list = {1:"Exercise",2:"Diet"}

#def getdate():
#    import datetime
#    return datetime,datetime.now()
#
#try:
#    print("Select client Name:")
#    for key, value in client_list.items():
#        print("Press",key, "for, value","/n",end="")
#    client_name = int(input())
#    print("Selected client:",client_list[client_name],"/n",end=" ")
#   print("Press 2 for Retrieve")
#    op = int(input())


import sys, datetime


def getdate():
    return datetime.datetime.now()


print("------------------HEALTH MANAGEMNT SYSTEM-----------------")
while (True):
    print("(1)Do you want write the plans or want to see the plans (2) (3) exit")
    choice = int(input("Enter the proper option"))
    if choice == 1:
        print("Names of person")
        print("yash,kamesh,milan")
        name = input("enter the name of person")
        if (name.upper() == "YASH"):
            file = open("yash.txt", "a")
            print("Enter what you ate today..")
            str1 = ""
            while str1 != '@':
                str1 = input()
                if (str1 != '@'):
                    # g=getdate()
                    file.write(str(getdate()) + ":-->" + str1 + "\n")
            print("RECORD INSERTED")
            file.close()



        elif (name.upper() == "KAMESH"):
            file = open("kamesh.txt", "a")
            print("Enter what you ate today..")
            str1 = ""
            while str1 != '@':
                str1 = input()
                if (str1 != '@'):
                    file.write(str(getdate()) + ":" + str1 + "\n")
            print("RECORD INSERTED")
            file.close()

        elif (name.upper() == "MILAN"):
            file = open("milan.txt", "a+")
            print("Enter what you ate today..")
            str1 = ""
            while str1 != '@':
                str1 = input()
                if (str1 != '@'):
                    file.write(str(getdate()) + ":" + str1 + "\n")
            print("RECORD INSERTED")
            file.close()
        else:
            print(" you entered ..wrong name")
    elif (choice == 3):
        print("close the program")
        sys.exit()
    elif (choice == 2):
        print("yash,kamesh,milan")
        file_name = input("enter the name that you want to open the file")
        file = open(file_name + ".txt", "r")
        for f in file:
            print(f)

    else:
        print("Enter wrong choice")