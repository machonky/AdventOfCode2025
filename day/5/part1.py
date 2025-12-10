import re

ingredientRangeRe = re.compile(r"(\d+)-(\d+)")

buckets = []

with open(0) as f:
    for bucketLine in f:
        if bucketLine == "\n":
            break
        startIndexStr, finishIndexStr = ingredientRangeRe.match(bucketLine.strip()).groups()
        buckets.append((int(startIndexStr), int(finishIndexStr)))

    freshCount = 0
    for ingredientLine in f:
        ingredientIndex = int(ingredientLine.strip())
        #found = False
        for startIndex, finishIndex in buckets:
            if ingredientIndex >= startIndex and ingredientIndex <= finishIndex:
                #print(f"{ingredientIndex} fresh")
                #found = True
                freshCount += 1
                break
        #if not found:
        #    print(f"{ingredientIndex} spoiled")
    
    print(f"freshCount: {freshCount}")
