import re
import math

dataLineRe = re.compile(r"\d+(?:\s+\d+)*")
operationLineRe = re.compile(r"(\*|\+)(?:\s+(\*|\+))*")

totalChecksum = 0
dataLines = []
operationLine = []
with open(0) as f:
    for line in f:
        if dataLineRe.match(line.strip()):
            dataLines.append(re.findall(r"\d+", line))
        if operationLineRe.match(line.strip()):
            operationLine = re.findall(r"\*|\+", line)

for colIndex, operation in enumerate(operationLine):
    stack = []
    for dataLine in dataLines:
        stack.append(int(dataLine[colIndex]))
    columnResult = sum(stack) if operation == '+' else math.prod(stack)
    totalChecksum += columnResult

print(f"totalChecksum:{totalChecksum}")

