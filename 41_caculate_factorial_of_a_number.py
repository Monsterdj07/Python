n=int(input("Enter the number to calculate the factorial:\n"))
fc=1
for n in range(1,n+1):
	fc=fc*n
	n=n+1
print(fc)
	