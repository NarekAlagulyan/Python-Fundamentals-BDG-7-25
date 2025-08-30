import math
from fractions import Fraction
from decimal import Decimal

print(2*(3+4)) # Result: 14
print(2*3+4)   # Result: 10
print(2+3*4)   # Result: 14
print(type(1 + 2.0 + 3)) # Result: float
number = 5.893
intNumber = int(number)  # Result: 5
print(intNumber)

otherIntNumber = math.trunc(number)  # Result: 5
print(otherIntNumber)

anotherIntNumber = round(number)      # Result: 6
roundNumber= round(number, 2)         # Result: 5.89
print(anotherIntNumber,roundNumber)

smallNumber = math.floor(number)  # Result: 5
bigNumber = math.ceil(number)     # Result: 6
print(smallNumber,bigNumber)

number=10
floatNumber=float(number) # Result: 10.0
print(floatNumber)
floatNUmber=number+0.0    # Result: 10.0
print(floatNumber)

stringFloat="1.5"
decimalNumber= Decimal(stringFloat) # Result: 1.5 type Decimal
print(decimalNumber, type(decimalNumber))

francNumber= Fraction(1,2)          # Result: 1/2 type fraction
print(francNumber, type(francNumber))
# IEEE 754 errors is about float objects
