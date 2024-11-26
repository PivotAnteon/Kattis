numItems, deal = input().split()

items = []
items = list(map(int, input().split()))

items.sort()

dealItems = []

for i in items:
    if i < int(deal):
        dealItems.append(i)

# for i in dealItems:
#     for j in reversed(dealItems):
#         if(i != j):
#             if i + j > int(deal):
#                 dealItems.remove(j)

# if len(dealItems) <= 0:
#     print(1)
# else:
#     print(len(dealItems))
left = 0
right = len(items) - 1


while left < right:
    if items[left] + items[right] > int(deal):
        dealItems.remove(items[right])
        left += 1
        right -= 1
    elif items[left] + items[right] <= int(deal):
        left += 1 

print(len(dealItems))