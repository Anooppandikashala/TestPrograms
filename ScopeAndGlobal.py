#Scope of a variable & global  keyword 
 
x = 20

def test():
	global x
	x = 10
	print(x)
	y=98
	
	def inside():
		global x
		x=99
		
		
	inside()
	print(x)
		
print(x)	
test()
print(x)
print(y)
