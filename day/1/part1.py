import re

DIAL_COMMAND_RE = re.compile(r"^(L|R)(\d+)$", re.MULTILINE)

dialMax = 100
dialStartPosition = 50

#f = """L68
#L30
#R48
#L5
#R60
#L55
#L1
#L99
#R14
#L82
#"""


#commands = [m.groups() for m in DIAL_COMMAND_RE.finditer(f)]

with open("input") as f:
    commands = [DIAL_COMMAND_RE.match(line).groups() for line in f]

zeroCount = 0
position = dialStartPosition  
for direction, amount in commands:
    sign = -1 if direction == 'L' else 1
    position = (position + sign*int(amount)) % dialMax
    if position == 0:
        zeroCount = zeroCount + 1

print("Zeros:",zeroCount)