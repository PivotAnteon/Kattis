
target = int(input())
output = []
temp = []
for i in nums:
    if target < i:
        temp.append(i)
        print(temp)