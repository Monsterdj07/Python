with open('logfile.txt') as f:
    content=f.read()
if 'python' in content.lower() :
    print(f'python found')
else:
    print(f'python not present')
    


    