num1=int(input("Enter the marks of English out of 100:\n"))
num2=int(input("Enter the marks of Maths out of 100:\n"))
num3=int(input("Enter the marks of Science out of 100:\n"))
if (num1>=33 and num2>=33 and num3>=33):
	if ((num1+num2+num3)/300) * 100 >= 40:
		print("You have passed the examination!")
	else:
		print("Eligible for rexamination")
else:
		print("Eligible for rexamination")
		