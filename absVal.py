import sys

a,b = map(int, input().split())
for line in sys.stdin():
    print(abs(a-b))
    a,b = map(int, input().split())