ts = []
ques = []
results = []

while (True) :
    take = input()
    
    if take == '-1':
        break
    
    parts = take.split()
    
    t = int(parts[0])
    que = parts[1]
    result = parts[2]
    
    ts.append(t)
    ques.append(que)
    results.append(result)
    
a = list(zip(ts, ques, results))

numQScore = 0
timeScore = 0
penalty = 0
for i in a:
    if i[2] == 'right':
        numQScore += 1
        timeScore += i[0]
        for j in a:
            if j[1] == i[1] and j[0] <= i[0] and j[2] != i[2]:
                penalty += 1


penalty = penalty * 20

totalScore = timeScore + penalty

print(str(numQScore) + " " + str(totalScore))