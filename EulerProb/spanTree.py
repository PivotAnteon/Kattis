f = open("0107_network.txt")
matrix = []

lines = f.readLines()
for line in lines:
    line = (x if x != '-' else ()for x in line.split(","))
    matrix.append(line)
    
for i in range(len(matrix)):
    for j in range(len(matrix)):
        total = [i][j]
        
total /= 2