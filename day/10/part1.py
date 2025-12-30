import re, itertools

line_re = re.compile(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$")

def calc_machine_state(machine_state: list, button: list) -> list:
    for wire in button:
        machine_state[wire] ^= True
    return machine_state

#test_machine_state = [False, False, False, False]
#test_machine_state = calc_machine_state(test_machine_state, [3])
#print(test_machine_state)
#test_machine_state = calc_machine_state(test_machine_state, [1,3])
#print(test_machine_state)
#test_machine_state = calc_machine_state(test_machine_state, [2])
#print(test_machine_state) # [False, True, True, False]

total_presses = 0
for line in open(0):
    lights, buttons, joltage = line_re.match(line.strip()).groups()
    lights = [light == "#" for light in lights]
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons.split()]
    found = False
    for count in range(1, len(buttons) + 1):
        for attempt in itertools.combinations(buttons, r=count):
            machine_state = [False for _ in range(len(lights))] #lights initially all off.
            for button in attempt:
                machine_state = calc_machine_state(machine_state, button)
            if machine_state == lights:
                total_presses += count
                found = True
                break
        if found: break
print(f"total_presses:{total_presses}")
