import re

ingredientRangeRe = re.compile(r"(\d+)-(\d+)")

buckets = []

with open(0) as f:
    for bucketLine in f:
        if bucketLine == "\n":
            break
        startIndexStr, finishIndexStr = ingredientRangeRe.match(bucketLine.strip()).groups()
        buckets.append((int(startIndexStr), int(finishIndexStr)))

    #naieve approach - the number are huge so this won't work in reasonable time
    #ingredientIndices = set()
    #totalIndices = 0
    #for startIndex, finishIndex in buckets:
    #    for index in range(startIndex, finishIndex+1):
    #        ingredientIndices.add(index)

    #print(len(ingredientIndices))
    
    # we need to merge the ranges to produce a distinct collection, then obtain the count from the difference in the merged ranges.
    buckets = sorted(buckets, key = lambda r: r[0])
    merged_buckets = []
    current_start, current_finish = buckets[0]
    for start, finish in buckets[1:]:
        if start <= current_finish+1:
            current_finish = max(current_finish, finish)
        else:
            merged_buckets.append((current_start, current_finish))
            current_start, current_finish = start, finish
    merged_buckets.append((current_start, current_finish))
    print(f"Merged Buckets count:{len(merged_buckets)}")
    # now we can get the count of indices easily...
    totalIndices = 0
    for start, finish in merged_buckets:
        totalIndices += (finish+1)-start
    
    print(f"totalIndices:{totalIndices}")