count = {}
with open('filename','r') as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n','')
            if token in count:
                count[token]+=1
            else:
                count[token] = 1
count 
