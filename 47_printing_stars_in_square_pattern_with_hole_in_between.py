n=int(input("Enter the number of rows\n"))
for rows in range(1,n+1):
	for col in range( 1,n+1):
		if rows==col==2:
			print(end="  ") 
		else:
			print("*",end=" ")
	print() 
