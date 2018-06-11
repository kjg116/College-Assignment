# CSE 1384
# Lab 3 driver file

###
### Comment out any of the tests below you have not yet implemented while
### working through the lab.
###

from lab3 import Rational

# Create the numbers

print()
print('Creating rational numbers 1/5 and 3/7...')
print()

one_fifth = Rational(1, 5)
three_sevenths = Rational(3, 7)

# Arithmetic

print('Addition (+)')
print('Expected value:    22/35')
print('Calculated value:  ', one_fifth + three_sevenths, sep='')
print()

print('Subtraction (-)')
print('Expected value:    -8/35')
print('Calculated value:  ', one_fifth - three_sevenths, sep='')
print()

print('Multiplication (*)')
print('Expected value:    3/35')
print('Calculated value:  ', one_fifth * three_sevenths, sep='')
print()

print('Division (/)')
print('Expected value:    7/15')
print('Calculated value:  ', one_fifth / three_sevenths, sep='')
print()

print('Less than (<)')
print('Expected value:    True')
print('Calculated value:  ', one_fifth < three_sevenths, sep='')
print()

print('Less than or equal to (<=)')
print('Expected value:    True')
print('Calculated value:  ', one_fifth <= three_sevenths, sep='')
print()

print('Equal to (==)')
print('Expected value:    False')
print('Calculated value:  ', one_fifth == three_sevenths, sep='')
print()

print('Not equal to (!=)')
print('Expected value:    True')
print('Calculated value:  ', one_fifth != three_sevenths, sep='')
print()

print('Greater than (>)')
print('Expected value:    False')
print('Calculated value:  ', one_fifth > three_sevenths, sep='')
print()

print('Greater than or equal to (>=)')
print('Expected value:    False')
print('Calculated value:  ', one_fifth >= three_sevenths, sep='')
print()

# Simplification

print('Simplification of 8/8')
print('Expected value:    1/1')
print('Calculated value:  ', Rational(8, 8), sep='')
print()

print('Simplification of 4/8')
print('Expected value:    1/2')
print('Calculated value:  ', Rational(4, 8), sep='')
print()

# Zero denominator

print('Attempting to create a rational number with a denominator of zero...')
try:
    not_valid = Rational(3, 0)
except ZeroDivisionError:
    print('Error caught successfully!')
