"""
Calculate quadratic root
"""

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

root = (-b + (b ** 2 - 4 * a * c) ** 0.5) // 2 * a
print(int(root))
root = (-b - (b ** 2 - 4 * a * c) ** 0.5) // 2 * a
print(int(root))