# let's say I start a program

a = 1
b = 2

# and then I want to see what's in a and b
# I can use the interactive mode to do that

import IPython; IPython.embed()

print("The rest of the program runs")

print("a is", a)

print(f"b is {b}")