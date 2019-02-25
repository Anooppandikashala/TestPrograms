
class Car:
    def __init__(self,enginame):
        print("car created")
        self.number_of_wheels = 4
        self.engine = str(enginame)
        self.registration_number = ""

    def start(self):
        print("car get started")

    def setRegistrationNumber(self,registrationNumber):
        self.registration_number = str(registrationNumber)

    def getRegistrationNumber(self):
        return str(self.registration_number)

    def move(self):
        print("car moving")

    def stop(self):
        print("car stopped")


toyota = Car("Toyota")
print(toyota.number_of_wheels)
print (toyota.engine)
print (toyota.registration_number)


toyota.setRegistrationNumber("KL599678")

print (toyota.getRegistrationNumber())

toyota.start()
toyota.move()


toyota.stop()
