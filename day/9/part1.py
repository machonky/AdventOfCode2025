points = [tuple(map(int, line.split(','))) for line in open(0)]
#build a collection of brute-force pairs to try out
corner_pairs = [[points[i], points[j]] for i in range(len(points)) for j in range(i + 1, len(points))]
max_area = 0
for corner_pair in corner_pairs:
    corner_a = corner_pair[0]
    corner_b = corner_pair[1]
    area = (abs(corner_a[0]-corner_b[0])+1) * (abs(corner_a[1]-corner_b[1])+1)
    max_area = max(max_area, area)
print(max_area)
