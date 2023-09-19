# import functions
from utility import sum, calculate


print(sum(1,2))
print(calculate(2,3,'*'))


import utility

print(utility.sum(10, 20))
print(utility.concat("A", 1, 2))
print(utility.calculate(20, 30, '*'))

import utility as u

print(u.sum(10, 20))
print(u.concat("A", 1, 2))
print(u.calculate(20, 30, '*'))

from  utility import sum as s

print(s(20, 30, 40))