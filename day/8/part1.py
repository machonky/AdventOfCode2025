import re

JB_RE = re.compile(r"^(\d+),(\d+),(\d+)$")

junction_boxes = [tuple(map(int, JB_RE.match(line.strip()).groups())) for line in open(0)]

def get_distance_score(Bx, By, Bz, Ax, Ay, Az):
    return (Bx-Ax)**2+(By-Ay)**2+(Bz-Az)**2

class ClosestPair:
    def __init__(self, boxA, boxB, i, j):
        self.boxA = boxA
        self.boxB = boxB
        self.score = get_distance_score(*boxB, *boxA)
        self.i = i
        self.j = j

connectionPairs = []    
for i in range(len(junction_boxes)):
    for j in range(i + 1, len(junction_boxes)): # calculate the possible unique pairs of boxes where order is not important
        boxA = junction_boxes[i]
        boxB = junction_boxes[j]
        connectionPairs.append(ClosestPair(boxA, boxB, i, j))

connectionPairs = sorted(connectionPairs, key=lambda p: p.score)

#closestPair = connectionPairs[0]
#print(f"Closest Pair: {closestPair.boxA}-{closestPair.boxB}")

#nextClosestPair = connectionPairs[1]
#print(f"NextClosest Pair: {nextClosestPair.boxA}-{nextClosestPair.boxB}")

#nextClosestPair = connectionPairs[2]
#print(f"NextClosest Pair: {nextClosestPair.boxA}-{nextClosestPair.boxB}")

#nextClosestPair = connectionPairs[3]
#print(f"NextClosest Pair: {nextClosestPair.boxA}-{nextClosestPair.boxB}")

#nextClosestPair = connectionPairs[4]
#print(f"NextClosest Pair: {nextClosestPair.boxA}-{nextClosestPair.boxB}")

#DSU Union Find Algorithm
# initially everything is it's own parent
Parent = list(range(len(junction_boxes)))
#print(Parent)

def find(x):
    if Parent[x] != x:
        return find(Parent[x])
    else:
        return x
    
def union(x,y):
    Parent[find(x)] = find(y)

#perform the connections in order
test_input_size = 10
input_size = 1000
selected_input_size = input_size
for pair in connectionPairs[:selected_input_size]:
    union(pair.i, pair.j)

print(Parent)

sizes = [0]*len(junction_boxes)
for box in range(len(junction_boxes)):
    sizes[find(box)] += 1

print(sizes)

sizes = sorted(sizes, reverse=True)
print(sizes[0]*sizes[1]*sizes[2])
