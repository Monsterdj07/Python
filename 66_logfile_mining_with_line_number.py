content=True
i=1
with open('logfile.txt') as f:
    while content:
        content=f.readline()
        if 'python' in content.lower() :
            print(f'python found at line number {i} --->>  {content} ')
        i=i+1 