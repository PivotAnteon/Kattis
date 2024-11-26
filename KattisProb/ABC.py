x,y,z = input().split()
bang = input()

sorted_values = []
sorted_values.append(int(x))
sorted_values.append(int(y))
sorted_values.append(int(z))
sorted_values.sort()

order_map = {'A': 0, 'B': 1, 'C': 2}

# Output the sorted values according to the order in 'bang'
print(f"{sorted_values[order_map[bang[0]]]} {sorted_values[order_map[bang[1]]]} {sorted_values[order_map[bang[2]]]}")
