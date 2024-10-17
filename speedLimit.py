loop = int(input())
totalDist = 0
while(loop != -1):
    grah = range(loop)[::-1]
    speed = list()
    time = list()
    for i in range(loop):
        x, y = map(int, input().split())
        speed.append(x)
        time.append(y)
    for j in grah:
        temp = speed[j-1] - speed[j]
        totalDist += time[j] * temp
        print(j)
    print(totalDist, " miles")
    loop = int(input())