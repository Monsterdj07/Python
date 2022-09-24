def game():
    return 200
score=game()
with open('hiscore.txt') as f:
    a=f.read()
if a=='':
    with open('hiscore.txt', 'w') as f:
            f.write(str(score))
elif score > int(a):
    with open('hiscore.txt', 'w') as f:
            f.write(str(score))
       
