manifoldLayers = []
with open(0) as file:
    for line in file:
        manifoldLayers.append(list(line.strip()))

def dump_layers():
    for layer in manifoldLayers:
        print("".join(layer))

splitCount = 0
for layerIndex in range(0, len(manifoldLayers)):
    for posIndex in range(0, len(manifoldLayers[0])):
        element = manifoldLayers[layerIndex][posIndex]
        if element == 'S':
            elementBeneath = manifoldLayers[layerIndex+1][posIndex]
            manifoldLayers[layerIndex+1][posIndex] = '|' if elementBeneath != '^' else elementBeneath
            continue
        if element == '^' and manifoldLayers[layerIndex-1][posIndex] == '|':
            manifoldLayers[layerIndex][posIndex-1] = '|'
            manifoldLayers[layerIndex][posIndex+1] = '|'
            splitCount += 1
            continue
        if element == '.' and layerIndex > 0:
            elementAbove = manifoldLayers[layerIndex-1][posIndex]
            if elementAbove == '|':
                manifoldLayers[layerIndex][posIndex] = '|'

dump_layers()
print(f"splitCount:{splitCount}")