
import os
oldname='this.txt'
newname='renamed_by_python.txt'
with open(oldname) as f:
    content=f.read()
with open(newname,'w') as g:
    g.write(content)
os.remove(oldname)