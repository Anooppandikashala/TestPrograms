'''
python test.py 


['a', 'b', 'c', 'd']
['b', 'c', 'a', 'f', 'h']
['c', 'b', 'd', 'g', 'h']


output :b

'''
x = "abcd"
x_list=list(x)

y = "bcafh"
y_list=list(y)

z = "cbdgh"
z_list=list(z)

print x_list
print y_list
print z_list

minimum = 99999

output = ""

index1 =0
index2 = 0
index3=0
for i in x_list:
	index1 = x_list.index(i)
	#print index1
	if (i in y_list and i in z_list):
		index2 = y_list.index(i)
		index3 = z_list.index(i)
		minimum1 = index1 + index2 + index3
		#print "minimum1 :"+str(minimum1)
		
		if(minimum > minimum1):
			minimum = minimum1
			output = i
			#print output
	else:
		continue
		
print "output :"+output;
	
