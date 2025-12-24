from shapely.geometry import Polygon, box

points = [tuple(map(int, line.split(','))) for line in open(0)]
christmas_bell = Polygon(points)

corner_pairs = [[points[i], points[j]] for i in range(len(points)) for j in range(i + 1, len(points))]

max_area = 0
for corner_pair in corner_pairs:
    corner_a = corner_pair[0]
    corner_b = corner_pair[1]

    width = abs(corner_a[0]-corner_b[0]) + 1
    height = abs(corner_a[1]-corner_b[1]) + 1
    area = width*height

    min_x = min(corner_a[0], corner_b[0])
    min_y = min(corner_a[1], corner_b[1])
    rectangle = box(min_x, min_y, min_x + width - 1, min_y + height - 1)

    if christmas_bell.contains(rectangle):
        #print(f"corner_a:{corner_a} corner_b:{corner_b}")
        #print(f"rectangle:{rectangle} area:{area}")
        max_area = max(max_area, area)
print(max_area)

