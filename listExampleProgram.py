
Name = []
Marks = []
Count = 1

def getNameAndMarks():
    global Count
    name = raw_input("Enter Name of student "+str(Count)+" :")
    marks= []
    for i in range(3):
        m = input("Enter mark "+str(i+1)+" :")
        marks.append(m)
    Name.append(name)
    Marks.append(marks)
    Count = Count+1

def printAverageMarks():
    for i in range(len(Name)):
        print ("Name : "+str(Name[i]))
        sumOfMark = 0
        for mark in Marks[i]:
            sumOfMark = sumOfMark + mark

        avgMark = sumOfMark / len(Marks[i])
        print ("Average Mark : " + str(avgMark))
        print ("********************************")


n = input("Enter the number of students : ")
for i in range(n):
    getNameAndMarks()

print ("\n*****************Average Marks*****************")
printAverageMarks()