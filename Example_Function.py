#Greatest Function Implementation:

#This function accept two integer or two float values and return the largest value


def Greatest_Function(num1,num2):
	if(num1 > num2):
		return num1
	else:
		return num2
		
def Smallest_Function(num1,num2):
	if(num1 < num2):
		return num1
	else:
		return num2
		
number1 = input("Enter first number")
number2 = input("Enter second number")

greatestvalue = Greatest_Function(number1,number2)
smallestvalue = Smallest_Function(number1,number2)
print("Larger value : "+ str(greatestvalue))
print("Smaller value : "+ str(smallestvalue))

