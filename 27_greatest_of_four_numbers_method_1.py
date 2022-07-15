num1=int(input("Enter the first number:\n "))
num2=int(input("Enter the second number:\n "))
num3=int(input("Enter the third number:\n "))
num4=int(input("Enter the fourth number:\n "))
if num1>num2:
	win = num1
elif num2>num1:
	win=num2
if num3>num4:
	win2=num3
elif num4>num3:
	win2=num4
if win>win2:
	print(win, " is the greatest number") 
else:
	print(win2, " is the greatest number") 
	
	
	
