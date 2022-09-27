with open('copy.txt') as f:
    content=f.read()
with open('this.txt') as g:
    content2=g.read()
if content==content2:
    print('both files match')
else:
    print('files do not match')