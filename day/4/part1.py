
def check_row(wareHouseData, checkRowIndex, rowIndex, columnIndex):
    row = wareHouseData[checkRowIndex]
    maxColIndex = len(row)-1

    startCol = columnIndex-1 if columnIndex > 0 else columnIndex
    endCol = colIndex+1 if columnIndex < maxColIndex else columnIndex

    rowScore = 0
    i = startCol
    while i <= endCol:
        if checkRowIndex != rowIndex:
            rowScore += row[i]
        else:
            rowScore += row[i] if i != columnIndex else 0
        i += 1
    
    return rowScore

def forklift_check(warehouseData, rowIndex, columnIndex):
    # if fewer than 4 in adjacent 8 positions return true
    #check row above (if possible)
    rollCount = 0
    if (rowIndex - 1) >= 0:
        rollCount += check_row(warehouseData, rowIndex - 1, rowIndex, columnIndex)
    #check current row
    rollCount += check_row(warehouseData, rowIndex, rowIndex, colIndex)
    #check row below (if possible)
    if (rowIndex + 1) <= (len(warehouseData) - 1):
        rollCount += check_row(warehouseData, rowIndex + 1, rowIndex, columnIndex)

    return rollCount < 4

accessibleRolls = 0
with open(0) as f:
    warehouseData = [[1 if rollBucket == '@' else 0 for rollBucket in line.strip()] for line in f]
    for rowIndex in range(0, len(warehouseData)):
        #debugRow = ''
        for colIndex in range(0, len(warehouseData[0])):
            testChar = '@' if warehouseData[rowIndex][colIndex] == 1 else '.'
            if (warehouseData[rowIndex][colIndex] == 1): # only do the check if there is a roll there
                #if forklift_check(warehouseData, rowIndex, colIndex):
                #    testChar = 'x'
                accessibleRolls += 1 if forklift_check(warehouseData, rowIndex, colIndex) else 0
            #debugRow += testChar
        #print(debugRow)
print(f"accessibleRolls:{accessibleRolls}")

