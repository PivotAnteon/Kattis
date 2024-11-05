ts = []
ques = []
results = []
take = 47 
while (take != -1) :
    take = input()
    if take == -1:
        break
    t = int(take[0])
    que = str(take[1])
    result = str(take[2])
    
    ts.append(t)
    ques.append(que)
    results.append(result)
    
a = list(zip(ts, ques, results))

print(a)