from  CalcultorExample.CalculatorFunctions import *

while(True):
    numb1 = input("Enter Number 1 : ")
    numb2 = input("Enter Number 2 : ")

    print("\n**********Calculator Menu**********")
    print("\t1 . Addition")
    print("\t2 . Subtraction")
    print("\t3 . Multiplication")
    print("\t4 . Division")
    print("\t5 . Quit")
    print("***********************************")

    choice = input("Enter your Choice :")

    if(choice == 1):
        result = addition(numb1,numb2)
        print ("\tResult : "+str(result))
    elif (choice == 2):
        result = subtraction(numb1, numb2)
        print ("\tResult : " + str(result))
    elif (choice == 3):
        result = multiplication(numb1, numb2)
        print ("\tResult : " + str(result))
    elif (choice == 4):
        result = division(numb1, numb2)
        print ("\tResult : " + str(result))
    elif (choice == 5):
        quit(0)
    else:
        print ("\tGive a valid choice")
