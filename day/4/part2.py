
def check_row(wareHouseData, checkRowIndex, rowIndex, columnIndex):
    row = wareHouseData[checkRowIndex]
    maxColIndex = len(row)-1

    startCol = columnIndex-1 if columnIndex > 0 else columnIndex
    endCol = columnIndex+1 if columnIndex < maxColIndex else columnIndex

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
    rollCount = 0
    if (rowIndex - 1) >= 0:
        rollCount += check_row(warehouseData, rowIndex - 1, rowIndex, columnIndex)

    rollCount += check_row(warehouseData, rowIndex, rowIndex, columnIndex)

    if (rowIndex + 1) <= (len(warehouseData) - 1):
        rollCount += check_row(warehouseData, rowIndex + 1, rowIndex, columnIndex)

    return rollCount < 4

def calc_accessible_rolls(warehouseData, rollCoordinates):
    accessibleRolls = 0
    for rowIndex in range(0, len(warehouseData)):
        #debugRow = ''
        for colIndex in range(0, len(warehouseData[0])):
            #testChar = '@' if warehouseData[rowIndex][colIndex] == 1 else '.'
            if (warehouseData[rowIndex][colIndex] == 1): # only do the check if there is a roll there
                #if forklift_check(warehouseData, rowIndex, colIndex):
                #    testChar = 'x'
                if forklift_check(warehouseData, rowIndex, colIndex):
                    accessibleRolls += 1
                    rollCoordinates.append((rowIndex,colIndex))
            #debugRow += testChar
        #print(debugRow)
    return accessibleRolls


with open(0) as f:
    warehouseData = [[1 if rollBucket == '@' else 0 for rollBucket in line.strip()] for line in f]

    totalAccessibleRows = 0
    prevTotalAccessibleRolls = 0
    while True:
        rollCoordinates = []
        totalAccessibleRows += calc_accessible_rolls(warehouseData, rollCoordinates)
        for removableRollRow, removableRollCol in rollCoordinates:
            warehouseData[removableRollRow][removableRollCol] = 0

        if prevTotalAccessibleRolls == totalAccessibleRows:
            break

        prevTotalAccessibleRolls = totalAccessibleRows

print(f"totalAccessibleRows:{totalAccessibleRows}")

