import re
from z3 import *

line_re = re.compile(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$")

# each row is a distinct linear programming exercise
# where:
# - coefficients are integers - can't have fractional button clicks
# - coefficients are >= 0 - can't have negative button clicks
# - equation is sum of coefficient_i*button_i = joltage_i; i = 0 to i < len(button)
# - we must minimise the sum of coefficients

# Worked experimental example
#buttons = [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
#joltages = [3, 5, 4, 7]
#optimizer = Optimize()
#variables = Ints(f"x_{i}" for i in range(len(buttons))) #declare a collection of z3 integer symbolic variables.
#print(variables)
#for var in variables:
#    optimizer.add(var >= 0) # apply the >= 0 constraint
# build the equations
#for wire, jolt in enumerate(joltages):
#    equation = 0
#    for b, button in enumerate(buttons):
#        if wire in button:
#            equation += variables[b]
#    optimizer.add(equation == jolt)
#declare the objective function    
#click_count_eqn = sum(variables) 
#minimize the objective function
#optimizer.minimize(click_count_eqn) 
#print(optimizer)
#if optimizer.check() == sat: # satisfiability check
#    model = optimizer.model()
#    print(model)
    # get the actual objective function value for this solution
    #print(type(model.evaluate(click_count_eqn)))
#    click_count = model.evaluate(click_count_eqn).as_long()
#    print(f"click_count: {click_count}")

total_clicks = 0
for line in open(0):
    lights, buttons, joltages = line_re.match(line.strip()).groups()
    lights = [light == "#" for light in lights]
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons.split()]
    joltages = list(map(int, joltages.split(",")))
    #print(f"buttons:{buttons}")
    #print(f"joltage:{joltages}")
    optimizer = Optimize()
    variables = Ints(f"x_{i}" for i in range(len(buttons))) #declare integer symbolic variables.
    for var in variables: optimizer.add(var >= 0) # apply the >= 0 constraint
    # build the equations
    for wire, jolt in enumerate(joltages):
        equation = 0
        for b, button in enumerate(buttons):
            if wire in button:
                equation += variables[b]
        optimizer.add(equation == jolt)
    #declare the objective function
    click_count_eqn = sum(variables)
    #minimize the objective function
    optimizer.minimize(click_count_eqn)
    if optimizer.check() == sat: # satisfiability check
        model = optimizer.model()
        click_count = model.evaluate(click_count_eqn).as_long()
        total_clicks += click_count

print(f"total_clicks:{total_clicks}")

