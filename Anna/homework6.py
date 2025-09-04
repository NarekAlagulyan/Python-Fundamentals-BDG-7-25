#Tuples, Files, and Everything Else Homework
# Part 1
# 1. What is the main difference between a list and a tuple?
# Տարբերությունը list-ի և tuple-ի միջև։
# list → փոփոխվող է (mutable)։
# tuple → անփոփոխ է (immutable)։

# 2. How do you create a tuple with a single item?
t = (5,)
# 3. Can you change an item within a tuple? What if that item is a list?
# Ոչ, բայց եթե item-ը list է, ապա ներսի list-ը փոխել կարելի է։

z = (1, [2, 3], 4)
z[1].append(5)
print(z)  # (1, [2, 3, 5], 4)
# 4. What does the open() function do?
# Ֆայլ է բացում (կարդալու, գրելու կամ ավելացնելու համար)։

# 5. What is the difference between reading a file with read() and readlines()?
# read() → վերադարձնում է ամբողջ տեքստը։
# readlines() → վերադարձնում է տողերի list։

# 6. How do you write to a file?
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Բարև \n")

# 7. What is the purpose of the close() method for files?
# Փակում է ֆայլը, ազատում հիշողությունը և պահպանում փոփոխությունները։

# 8. What is a context manager (with statement) used for with files?
# Ավտոմատ փակում է ֆայլը նույնիսկ սխալի դեպքում։

# Part 2
# 1. What is the output of (1, 2, 3) * 2?
print((1, 2, 3) * 2)    #(1, 2, 3, 1, 2, 3)

# 2. True or False: (1) == 1.
# True (քանի որ (1) թիվ է, ոչ թե tuple)։

# 3. How can you unpack a tuple t = (a, b, c) into three variables?
tup = (1, 2, 3)
x, y, z = tup
print(x)  # 1
print(y)  # 2
print(z)  # 3

# 4. What mode would you use to open a file for both reading and writing?
open("example.txt", "r+")

# 5. If you open a file for writing ('w') that already exists, what happens to its content?
# առաջին անգամ գրում ենք
with open("esim.txt", "w", encoding="utf-8") as f:
    f.write("Սա առաջին տեքստն է\n")

# երկրորդ անգամ նույն ֆայլը բացում ենք "w"-ով
with open("esim.txt", "w", encoding="utf-8") as f:
    f.write("Սա երկրորդ տեքստն է\n")

# կարդում ենք ֆայլի պարունակությունը
with open("esim.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 6. What does a file's readline() method return at the end of the file?
# Երբ ֆայլի վերջն է հասնում, readline() մեթոդը վերադարձնում է դատարկ string ('')։

# 7. Can you have a tuple as a key in a dictionary?
# Այո, tuple-ը կարող է լինել dictionary-ի key, քանի որ immutable է։
# Բայց tuple-ի մեջ mutable օբյեկտներ (օրինակ՝ list) չպետք է լինեն։

# 8. How would you create a tuple from a list?
my_list = [1, 2, 3]
tup = tuple(my_list)
print(tup)  # (1, 2, 3)

# 9. New! What is the benefit of using a tuple over a list?
# Tuple-ի առավելությունները․
# Անփոփոխ են (ավելի ապահով տվյալների պահեստավորում)։
# Ավելի արագ են, քան list-երը։
# Կարելի է օգտագործել որպես dictionary-ի key կամ set-ի մեջ։

# 10. New! How would you open a file in binary mode?
# Ֆայլ բացելու համար binary ռեժիմով ավելացնում ենք "b"․
# "rb" → կարդալու համար (read binary)
# "wb" → գրելու համար (write binary)

with open("esim.txt", "rb") as f:
    data = f.read()

# 11. New! What does the file tell() method do?
# tell() մեթոդը վերադարձնում է ֆայլի “pointer”-ի ընթացիկ դիրքը (այսինքն՝ որ byte-ի վրա ենք գտնվում)։

with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
    print(f.tell())  # ցույց կտա 5, քանի որ 5 byte ենք գրել

# 12. New! True or False: You must always close a file after opening it.
# False
# Եթե բացում ես open()-ով, ապա պետք է փակես close()-ով։
# Բայց եթե օգտագործում ես with open(...) as f:, ապա ֆայլը ավտոմատ կփակվի, նույնիսկ սխալի դեպքում։

# Part 3
# 1. Coordinate System: Create a tuple to store the (x, y) coordinates of a point. Then, unpack the tuple into two variables, x and y, and print them.
point = (3, 5)
x, y = point
print("x =",x, "y =", y)

# 2. Student Roster: Create a list of tuples, where each tuple contains a student's name and their score. Print the roster.
roster = [("Աննա", 95), ("Արամ", 88), ("Մարիա", 76)]
print(roster)

# 3. File Writer: Write a script that asks the user for their name and then writes "Hello, [name]!" to a file named greeting.txt.
# name = input("Քո անունը: ")
# with open("greeting.txt", "w") as f:
#     f.write(f"Hello, {name}!")

# 4. File Reader: Write a script that reads the greeting.txt file and prints its content to the console.
# with open("greeting.txt", "r") as f:
#     print(f.read())

# 5. Line by Line: Create a text file with at least three lines of text. Write a script that reads the file line by line and prints each line.
with open("text.txt", "r",encoding="utf-8") as f:
    for line in f:
        # print(line)
        print(line.strip()) # հեռացնում ենք սկզբի և վերջի դատարկ space-երը ու \n-ը

# 6. New! The Logger: Write a script that asks the user for a message and appends it to a file called log.txt with a timestamp.
import datetime

# inputt = input("Գրիր հաղորդագրություն: ")
# a -> append
# with open("log.txt", "a", encoding="utf-8") as f:
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     f.write(f"[{timestamp}] {inputt}\n")

print("Հաղորդագրությունը հաջողությամբ ավելացվեց log.txt ֆայլում ")

# 7. New! Configuration Settings: Create a tuple to store some configuration settings for a program, like ('dark_mode', True, 16). Unpack these settings into variables and print them.
config = ("dark_mode", True, 16)

setting, enabled, font_size = config

print("Setting:", setting)
print("Enabled:", enabled)
print("Font size:", font_size)

# 8. New! The File Cloner: Write a script that reads the content of one file and writes it to a new file.
originalfilee = "original.txt"

copyfilee = "copy.txt"

with open(originalfilee, "r", encoding="utf-8") as f:
    content = f.read()

with open(copyfilee, "w", encoding="utf-8") as ff:
    ff.write(content)

print(f"Ֆայլը հաջողությամբ պատճենվեց '{originalfilee}'-ից '{copyfilee}' ")


# Part 4: Advanced Tuples & Files Puzzles
# 1. The Appender: Write a script that opens a file in append mode ('a') and adds a new line of text to it each time the script is run.

# new_line = input("Գրիր նոր տողը, որը ցանկանում ես ավելացնել: ")

# with open("notes.txt", "a", encoding="utf-8") as f:
#     f.write(new_line + "\n")

# print("Տողը հաջողությամբ ավելացվեց notes.txt ֆայլում ")

# 2. The Number Cruncher: Create a text file with one number on each line. Write a script that reads the file, calculates the sum of all the numbers, and prints the result.
with open("numbers.txt", "r", encoding="utf-8") as f:
    total = 0
    for line in f:
        # հեռացնում ենք սպեյսերը և բաժանում ','-ով
        numbers = line.strip().split(",")
        for num in numbers:
            total += int(num.strip())

print("Ամբողջ գումարը:", total)

# 3. CSV Creator: A CSV (Comma-Separated Values) file is a common way to store data. Write a script that creates a CSV-like file. It should be a list of lists, where each inner list represents a row. Write this data to a file, with each inner list on a new line and the items separated by commas.
data = [
    ["Անուն", "Գնահատական"],
    ["Աննա", 95],
    ["Արամ", 88],
    ["Մարիա", 76]
]

with open("data.csv", "w", encoding="utf-8") as f:
    for row in data:
        f.write(",".join(map(str, row)) + "\n")

print("CSV ֆայլը ստեղծվեց ")

# 4. New! The Story Writer: Create a script that prompts the user for a series of inputs (e.g., a name, a place, an adjective) and then writes a short story using these inputs into a new text file.
# name = input("Անուն: ")
# place = input("Տեղ: ")
# adj = input("Ածական: ")
#
# story = f"{name}-ը գնաց {place}, որտեղ ամեն ինչ {adj} էր։"
#
# with open("esim.txt", "w", encoding="utf-8") as f:
#     f.write(story)
#
# print("Պատմությունը պահպանվեց esim.txt ֆայլում ")

# 5. New! The High Score Keeper: Write a script for a game that stores the high score in a file. When the script runs, it should read the high score from the file, ask the user for their score, and if their score is higher, update the file with the new high score.
filename = "highscore.txt"

# Կարդում ենք նախորդ high score
try:
    with open(filename, "r", encoding="utf-8") as f:
        highscore = int(f.read())
except FileNotFoundError:
    highscore = 0

score = int(input("Քո գնահատականը: "))

if score > highscore:
    print("Նոր ռեկորդ!")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(score))
else:
    print("Չի անցել high score-ը:", highscore)