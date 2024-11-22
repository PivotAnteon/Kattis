input()
# takes in the input as an array
cand = list(map(int, input().split()))
# copy input array for maintaining data
hold = cand
# holds opus number for first iteration
opus = cand[0]
# holds total number of candidates
numCand = len(cand)

print(cand)
while len(cand) > 1:
    remove = len(cand) % opus
    print(remove)
    opus = cand[cand.pop(remove - 1)]
    print(cand)

            