manifoldLayers = [list(line.strip()) for line in open(0)]

manifoldLayerCount = len(manifoldLayers)

timeline_counts = {} # we'll store results here so we don't need to recalculate with a full recursion

def get_splitter_timeline_count(layerIndex,posIndex):
    #we're at the bottom - we have a 'timeline'
    if layerIndex >= manifoldLayerCount: return 1

    if (layerIndex, posIndex) not in timeline_counts:
        element = manifoldLayers[layerIndex][posIndex]
        #straight down
        if element == 'S' or element == ".":
            timeline_counts[(layerIndex,posIndex)] = \
                get_splitter_timeline_count(layerIndex+1,posIndex)
        # we sum the left and right paths
        if element == '^':
            timeline_counts[(layerIndex,posIndex)] = \
                get_splitter_timeline_count(layerIndex,posIndex - 1) + \
                get_splitter_timeline_count(layerIndex,posIndex + 1)
            
    return timeline_counts[(layerIndex,posIndex)]

#We kick this off by supplying the S position
S = (0, manifoldLayers[0].index('S'))

print(get_splitter_timeline_count(*S))
