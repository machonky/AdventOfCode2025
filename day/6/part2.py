import re
import math

dataLineRe = re.compile(r"\d+(?:\s+\d+)*")
operationLineRe = re.compile(r"(\*|\+)(?:\s+(\*|\+))*")

totalChecksum = 0
dataLines = []
operationLine = ""
with open(0) as f:
    for line in f:
        if dataLineRe.match(line.strip()):
            dataLines.append(line.rstrip("\n"))
        if operationLineRe.match(line.strip()):
            operationLine = line.strip()

# the operation line gives us the start index of the data block as well as the operation
opIndices = [(m.start(), m.group()) for m in re.finditer(r"\*|\+", operationLine)]
maxIndex = len(opIndices)-1
for index, opIndex in enumerate(opIndices):
    groupLines = []
    for dataLine in dataLines:
        startCharIndex = opIndex[0]
        finishCharIndex = len(dataLine) if index == maxIndex else opIndices[index+1][0]
        groupLines.append(dataLine[startCharIndex:finishCharIndex])
    #print(f"len(groupLines):{len(groupLines)}")
    glStripes = len(groupLines[0])
    #print(f"glStripes:{glStripes}")
    glValues = []
    for glStripeIndex in range(0, glStripes):
        stripeValue = 0
        digitMagnitude = 0
        for glIndex in range(len(groupLines)-1,-1,-1): # collect numbers from least to most significant
            cellChar = groupLines[glIndex][glStripeIndex]
            if cellChar.isdigit():
                stripeValue += int(cellChar)*10**digitMagnitude
                digitMagnitude += 1
        if stripeValue != 0:
            #print(f"stripeValue:{stripeValue}")
            glValues.append(stripeValue)
    groupValue = sum(glValues) if opIndex[1] == '+' else math.prod(glValues)
    #print(f"groupValue:{groupValue}")
    totalChecksum += groupValue
print(f"totalChecksum:{totalChecksum}")