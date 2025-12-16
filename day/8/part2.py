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

circuit_count = len(junction_boxes) # the number of circuits will count down as we make connections.

#perform *all* the connections in order
for pair in connectionPairs:
    if find(pair.i) == find(pair.j): continue # skip - they're on the same circuit
    union(pair.i, pair.j)
    circuit_count -= 1 # connection made.
    if circuit_count == 1: # last circuit
        print(junction_boxes[pair.i][0] * junction_boxes[pair.j][0]) # our result
        break



