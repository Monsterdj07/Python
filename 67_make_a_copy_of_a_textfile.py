with open('logfile.txt') as f:
    content=f.read()
with open('this.txt','w') as g:
    g.write(content)