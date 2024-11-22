answer = 0
fibo = 1
fibo2 = 2

while fibo <= 4000000:
    if(fibo % 2 == 0):
        answer += fibo
    fibo, fibo2 = fibo2, fibo + fibo2
    print(str(fibo) + " " + str(fibo2))
     
print(str(answer) + " = total")