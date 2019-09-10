
NameMarks = {}
count = 1

def getNameAndMarks():
    global count
    name = raw_input("Enter Name of student "+str(count)+" :")
    marks= []
    for i in range(3):
        m = input("Enter mark "+str(i+1)+" :")
        marks.append(m)
    NameMarks[name] = marks
    count = count+1

def printAverageMarks():
    for name,marks in NameMarks.items():
        print ("Name : "+name)
        sumOfMark = 0
        for mark in marks:
            sumOfMark = sumOfMark + mark

        avgMark = sumOfMark / len(marks)
        print ("Average Mark : " + str(avgMark))
        print ("********************************")

def studentExistence(name):
    if(NameMarks.has_key(name)):
        print("Student Exist")
    else:
        print("Student Not Exist")


n = input("Enter the number of students : ")
for i in range(n):
    getNameAndMarks()

print ("\n*****************Average Marks*****************")
printAverageMarks()


print ("\n*****************Student Existence *****************")

while(True):
    name = raw_input("Enter a name to search")
    studentExistence(name)
