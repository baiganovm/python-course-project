"""
Drawing steps according to argument value
"""

import sys
num_steps = int(sys.argv[1])
step = 1
while step <= num_steps:
    print(" "*(num_steps-step) + "#"*step)
    step += 1
