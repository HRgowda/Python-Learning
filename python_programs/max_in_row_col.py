matrix = [[3,7,8],[9,11,13],[15,16,17]]

min_r = []
max_c = []

for i in matrix:
    row = []
    for j in i:
        row.append(j)
    min_r.append(min(row))

# Iterate over each row
for j in range(len(matrix[0])):
    col = []
    # Iterate over each element in the row
    for i in range(len(matrix)):
        col.append(matrix[i][j])
    max_c.append(max(col))

print(min_r)
print(max_c)

