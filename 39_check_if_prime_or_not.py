a=int(input("Enter the number that you wanna check:\n"))
i=1
count=0
for i in range(1, a):
	p=a%i
	i=i+1
	if p==0:
		count=count+1		
if count>=3:
		print("Not Prime")
else:
		print("Prime")
		