# 1 What is the value of the expression 2 * (3 + 4) in Python?
print("1 -->", 2 * (3 + 4))

# 2 What is the value of the expression 2 * 3 + 4 in Python?
print("2 -->", 2 * 3 + 4)

# 3 What is the value of the expression 2 + 3 * 4 in Python?
print("3 -->", 2 + 3 * 4)

# 4 What tools can you use to find a number’s square root, as well as its square?
# Ի՞նչ գործիքներ կարող եք օգտագործել թվի քառակուսի արմատը, ինչպես նաև նրա քառակուսին գտնելու համար։
print("4 -->")
import math

number = int(input('Enter a number: '))
print(number)

square = number ** 2
print("tvi qarakusin-->", square)

square_root = number ** 0.5
print("armaty-->", square_root)

square_root_2 = math.sqrt(number)
print("armaty2-->", square_root_2)


# 5 What is the type of the result of the expression 1 + 2.0 + 3?
result = 1 + 2.0 + 3
print("5 -->", result, type(result))

# 6 How can you truncate and round a floating-point number?
print("6 -->")
import math

x = float(input("kotorakayin tiv grir: "))

print("kloracrac arjeqy depi nerqev:", math.trunc(x))
print("kloracrac arjeqy depi vorin mota:", round(x))
print("kloracrac arjeqy minchev storaketic heto 1 tiv u vorin mota:", round(x, 1))


# 7 How can you convert an integer to a floating-point number?
print("7-->", float(5))

# 8  Investigate "IEEE 754" and its issue. (Simply ask GPT).
print("8 -->", 0.1 + 0.2)  # floating point error

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))  #ճիշտ

# 9 Decimal, Fraction
print("9 -->")

# decimal Բարձր ճշգրտության տասնորդականներ


from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")
c = a + b
print("Decimal արդյունքը:", c)  #ճիշտ

# fractions — Կոտորակ
# kotoraka haskanum

from fractions import Fraction

a = Fraction(1, 3)
b = Fraction(1, 6)
c = a + b
print("Fraction արդյունքը:", c)  # 1/2


# 10 During the last class we talked about +, -, *, **, /, //, % operators. We did not cover other important operators, please find them and play with them.
print("10 -->")
a = 5
b = 3
# a binary:  0101
# b binary:  0011
print(" a & b:", a & b)     #Միայն այն բիթերը կլինեն 1, որոնք երկուսում էլ 1 են։ 0001->1
print(" a | b:", a | b)     #Բիթը կլինի 1, եթե գոնե մեկում 1 է։0111  → 7
print(" a ^ b:", a ^ b)      #Բիթը կլինի 1, եթե միայն մեկում 1 է, բայց ոչ երկուսում։0110  → 6
print(" ~a:", ~a)           #Փոխում է բոլոր բիթերը։ Python-ում թվերը ներկայացվում են two’s complement ձևով, այնպես որ սա ստանում է -(a+1)։a = 5  →  ...00000101   ~a     →  ...11111010  → -6
print(" a << 1:", a << 1)   #a << 1 → shift left (բիթերը ձախ շարժել 1 անգամ)   Ձախ շարժելը բազմապատկում է 2-ով։0101 << 1  →  1010 (10)
print(" a >> 1:", a >> 1)   #a >> 1 → shift right (բիթերը աջ շարժել 1 անգամ)  Աջ շարժելը բաժանում է 2-ի վրա ամբողջ թվով։0101 >> 1  →  0010 (2)


print(" a == b:", a == b)
print(" a != b:", a != b)
print(" a < b:", a < b)


print(" and:", True and False)
print(" or:", True or False)
print(" not:", not True)


nums = [1, 2, 3]
print( 2 in nums)
print( 4 not in nums)


x = [1, 2]
y = x
z = [1, 2]
print( x is y)
print(x is not z)
