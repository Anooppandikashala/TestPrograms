n= 4

print("*"*5 + "Pattern" + "*"*5)
print("")

'''

******
******
******
******
******

'''

for i in range(6):
	print("*"*6)

print("")	
print("*"*5 + "Pattern 1" + "*"*5)
print("")

'''
---1----
*
**
***
****
*****
******

'''

for i in range(6):
	print("*"*(i+1))
print("")
print("*"*5 + "Pattern 2" + "*"*5)
print("")
'''

---2----

******
*****
****
***
**
*
'''

for i in range(6,0,-1):
	print("*"*(i))

'''

---3----

     *
    **
   ***
  ****
 *****
******

'''
print("")
print("*"*5 + "Pattern 3" + "*"*5)
print("")

for i in range(1,n+1):
	print(" "*(n-i)+"*"*i)

print("")
print("*"*5 + "Pattern 4" + "*"*5)
print("")
'''
---4----

   *
  ***
 *****
*******

'''

n= 4 
for i in range(n):
 	print(" "*(n-i)+ "*"*((2*i)+1))

print("")
print("*"*5 + "Pattern 5" + "*"*5)
print("")
'''

---5----


   *
  ***
 *****
*******
 *****
  ***
   *
   
'''

n= 4 
for i in range(n):
 	print(" "*(n-i)+ "*"*((2*i)+1))
 	
for i in range(n,-1,-1):
 	print(" "*(n-i)+ "*"*((2*i)+1))

print("")
print("*"*5 + "Pattern 6" + "*"*5)
print("")
'''

---6----

   *
  * *
 *   *
*     *
 *   *
  * *
   *
   
'''

n= 4 
for i in range(n):
	if(i==0):
		print " "*(n-i) + "*" +" "*((2*(i-1))+1)
	else:
		print " "*(n-i) + "*" +" "*((2*(i-1))+1)+ "*"

for i in range(n,-1,-1):
	if(i==0):
		print " "*(n-i) + "*" +" "*((2*(i-1))+1)
	else:
		print " "*(n-i) + "*" +" "*((2*(i-1))+1)+ "*"
