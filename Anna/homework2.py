#The Dynamic Typing Interlude

# 1.Consider the following three statements. Do they change the value printed for A?
A = "spam"
B = A
B = "shrubbery"
print("1 -->", A)
print(B)
# 2.Consider these three statements. Do they change the printed value of A?
A = ["spam"]
B = A
B[0] = "shrubbery"
print("2-->", A)
print(B)
# 3.How about these—is A changed now?
A = ["spam"]
B = A[:]
B[0] = "shrubbery"
print("3-->", A)
print(B)
# 4.Explain in details the difference between is and ==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # արժեքն է ստուգում
print(x is y)  # հասցեներն է ստուգում
# 5.What does id function do and what does it return.
a = 42
b = 42
print(id(a), id(b))
# 6.What is Object Interning
a = 256
b = 256
print(a is b)  # True

x = 257
y = 257
print(x is y) #False
# 7.What is Garbage Collector(GC) and how does it work(simple explanation) in CPython
"""
    Garbage Collector (աղբահավաք) – մեխանիզմ է, որը Python-ը օգտագործում է անպետք հիշողությունը ազատելու համար։
    Եթե այդ օբյեկտը այլևս չի օգտագործվում (ոչ մի բան չի հղվում դրան), GC-ն գտնում է այն և ջնջում՝ ազատելով հիշողությունը։
    
    CPython-ում GC-ն հիմնված է երկու հիմնական մեթոդի վրա․
    1. Reference Counting (հղումների հաշվարկ)
    Յուրաքանչյուր օբյեկտ ունի “counter” – թե քանի փոփոխական է հղվում դրան։
    Օրինակ՝
    
    a = [1, 2, 3]   # counter = 1
    b = a           # հիմա counter = 2 (a և b հղվում են նույն list-ին)
    del a           # counter = 1
    del b           # counter = 0 → օբյեկտը ջնջվում է
    
    Երբ counter-ը դառնում է 0, օբյեկտը անմիջապես ջնջվում է։
    
    2. Cycle Detection (ցիկլերի հայտնաբերում)
    Reference counting-ը չի կարող լուծել այն դեպքերը, երբ օբյեկտները իրար են հղվում (ցիկլ ստեղծելով)։
    Օրինակ՝
    
    x = []
    y = []
    x.append(y)
    y.append(x)
    
    Այստեղ x և y իրար են հղվում, և նրանց counter-ը երբեք չի դառնում 0։
    
    Python-ի Garbage Collector-ը պարբերաբար ստուգում է նման օբյեկտների ցիկլեր և ջնջում է դրանք, եթե այլևս հասանելի չեն ծրագրի համար։
    
"""

# 8.Aliasing with mutable and immutable types
# Show examples of what happens when two variables point to the same list, dictionary, string, integer, etc., and one of them changes.
# Why does the change sometimes affect both variables, and sometimes not?

#Mutable
a = [1, 2]
b = a
b.append(3)
print(a)  # փոփոխվեց
print(b)

#Immutable

a = "hi"
b = a
b += "Anna"
print(a)  # չփոփոխվեց, որովհետև string-ը immutable է
print(b)
# 9.Draw a memory diagram
# For each scenario(homework scenarios and your own random scenarios), draw boxes showing
# Objects in memory
# Variable names pointing to them
# How these connections change after each statement

#տետրում գծել եմ