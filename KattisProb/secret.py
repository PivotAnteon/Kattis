from collections import defaultdict
m, n = list(map(int, input().split()))
d = defaultdict(set)

for i in range(m):
    x, y = input().split()
    if x not in d:
        d[x] = []
    d[x].append(y)
print(d)    
    
def dfs(source, dest):
    visited = set()
    stack = [source]
    while stack:
        current = stack.pop()
        if current == dest:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in d[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False            
        
results = []
for j in range(n):
    a, b = input().split()
    for c1, c2 in zip(a, b):
        if len(a) != len(b):
            result = False
            break
        result = dfs(c1, c2)
        if not result:
            break
    results.append(result)
        
    
for item in results:
    if item:
        print("yes")
    else:
        print("no")