import random 
randno=random.randint(1, 3)
if randno==1:
	comp="r"
if randno==2:
	comp="p"
if randno==3:
	comp="s"
you=input("your turn : rock(r), paper(p), scissors (s) ")
if comp==you:
	print(" it is a tie! ")
else:
	if comp=="r":
		if you=="s":
			print(" you loose! ")
		else:
			print(" you win! ")
	elif comp=="p":
		if you=="r":
			print(" you loose! ")
		else:
			print(" you win! ")
	elif comp=="s":
		if you=="p":
			print(" you loose! ")
		else:
			print(" you win! ")

print(f'you chose: {you}, computer chose: {comp}')
	