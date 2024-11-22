x = int(input())

hours = x % 60
x = int(x / 60)
minutes = x % 60
x = int(x / 60)
seconds = x

print(str(seconds) + " : " + str(minutes) + " : " + str(hours))