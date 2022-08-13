F=open('poems.txt','r')
search_w=input("Enter then word you want two to search:\n")
a=F.read()
if search_w in a:
    print("word found!")
else:
    print("word not found!")
F.close()