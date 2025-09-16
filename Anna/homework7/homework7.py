# Homework List
# 1. Log Writer Program
    # Write a program that takes comma-separated values as input from the user.
    # Append (extend) the values into a file line by line, like a log.
# Գրեք ծրագիր, որը օգտատիրոջից մուտքագրում է ստորակետերով բաժանված արժեքներ։
# Ավելացրեք (append) արժեքները տող առ տող ֆայլի մեջ, ինչպես գրանցամատյանը։

# file_name = 'log.txt'
# values = input("Մուտքագրեք ստորակետով արժեքներ։ ")
# with open(file_name, 'a', encoding = 'utf8') as f:
#     for value in values.split(','):
#         f.write(value.strip() + '\n')    #strip-ը եթե բացատներ լինեն հանի
# print("Արժեքները գրանցվեցին:", file_name)


# 2. Dictionary Builder with Pickle

    # Write a program that reads the content of a file.
    # Գրեք ծրագիր, որը կարդում է ֆայլի բովանդակությունը։
    # Treat every odd row as a dictionary key and every even row as its value.
    # Յուրաքանչյուր կենտ տողը համարեք բառարանի բանալի, իսկ յուրաքանչյուր զույգ տողը՝ դրա արժեքը։
    # If a row is empty or contains only spaces:
    #Եթե տողը դատարկ է կամ պարունակում է միայն բացատներ՝
        # Use a default key instead of the missing key.
        # Օգտագործեք լռելյայն բանալի բացակայող բանալու փոխարեն։
        # Use None instead of the missing value.
        # Օգտագործեք None բացակայող արժեքի փոխարեն։
    # Save the prepared dictionary into a pickle file.
    # Պահպանեք պատրաստված բառարանը pickle ֆայլում։
    # Load the dictionary back from the pickle file and display its items line by line.
    # Բեռնեք բառարանը pickle ֆայլից և ցուցադրեք դրա տարրերը տող առ տող։

# import pickle
# input_file = "data.txt"
# pickle_file = "data.pkl"
#
# with open(input_file, "r", encoding="utf-8") as f:
#     lines = [line.strip() for line in f.readlines()]
#
# dictionary = {}
#
# for i in range(0, len(lines), 2):
#     key = lines[i] if lines[i] else "default_key"
#     value = None
#     if i+1 < len(lines) and lines[i+1]:
#         value = lines[i+1]
#     dictionary[key] = value
#
#
# # Պահպանում ենք pickle ֆայլում
# with open(pickle_file, "wb") as f:
#     pickle.dump(dictionary, f)
#
# # Վերաբեռնում ենք pickle-ից
# with open(pickle_file, "rb") as f:
#     loaded_dict = pickle.load(f)
#
# # Տպում ենք արդյունքը տող առ տող
# print("Բառարանի պարունակությունը:")
# for k, v in loaded_dict.items():
#     print(f"{k} → {v}")




# 3. Unique Words Logger

    # Take a sentence as input from the user.
    # Split it into words, remove duplicates, and sort alphabetically.
    # Append the result to a file, each word on a new line.
#input նախադասություն։
#Տեքստը բաժանում ենք բառերի:
#Հեռացնում ենք կրկնվող բառերը ։
#Տեսակավորում ենք բառերը։
#Ավելացնում ենք (append) արդյունքը ֆայլում, որտեղ յուրաքանչյուր բառ գրվում է նոր տողի վրա։

# sentence = input("Mutqagreq naxadasutyun: ")
# words = sentence.split()
# unique_words = set(words)
# sorted_words = sorted(unique_words)
#
# with open("words.txt", "a") as file:
#     for word in sorted_words:
#         file.write(word + "\n")
#
#
# print("avelacvel e")
#

# 4. Reverse File Reader

    # Read all lines from a file.
    # Reverse their order.
    # Save the reversed content into another file.

# with open("data.txt","r") as file:
#     lines = file.readlines()
# reversed_lines = lines[::-1]
#
# with open("reversed.txt","w") as file:
#     for line in reversed_lines:
#         file.write(line if line.endswith("\n") else line + "\n")
#


# 5. JSON Converter

    # Read a text file where each line contains key=value.
    # Convert it into a dictionary.
    # Save the dictionary into a JSON file.
    # Load the JSON file back and print the dictionary.

# Կարդացեք ֆայլ, որտեղ յուրաքանչյուր տող պարունակում է key=value:
# Փոխարկեք այն բառարանի:
# Պահպանեք բառարանը JSON ֆայլի մեջ:
# Վերբեռնեք JSON ֆայլը և տպեք բառարանը:


'''
import json
data = {}
with open("data.txt","r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)  # բաժանում ենք միայն առաջին '='-ով
            data[key.strip()] = value.strip()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("Վերաբեռնված dictionary:")
for k, v in loaded_data.items():
    print(f"{k} : {v}")
'''


# 6. Word Counter with Pickle
        #Read a text file.
        #Count how many times each word appears.
        #Store the word-frequency dictionary in a pickle file.
        #Load it back and display the results line by line.
'''

import pickle
import string
from collections import Counter

# Մուտքային և ելքային ֆայլեր
INPUT_FILE = "input.txt"
PICKLE_FILE = "word_counts.pkl"

# Կարդում ենք տեքստը
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Փոքրատառ դարձնել + կետադրությունը հանել
content = content.lower()
for ch in string.punctuation:
    content = content.replace(ch, " ")

# print(content)

# Բաժանում ենք բառերի
words = content.split()

# Հաշվում ենք հաճախականությունը
word_counts = Counter(words)

# Պահպանում pickle ֆայլում
with open(PICKLE_FILE, "wb") as pf:
    pickle.dump(dict(word_counts), pf)

# Վերաբեռնում pickle ֆայլից
with open(PICKLE_FILE, "rb") as pf:
    loaded_counts = pickle.load(pf)

# Տպում ենք բառերը և հաճախականությունը
print("Բառ — Հաճախություն")
for word, count in sorted(loaded_counts.items()):
    print(f"{word} : {count}")

'''
# 7. CSV Merger
        #Have two CSV files with the same columns.
        #Merge them into one file without duplicates.
        #Display the total number of rows after merging.

"""
Միավորենք երկու ֆայլերը։
Հեռացնենք կրկնվող տողերը։
Պահենք նոր CSV ֆայլում։
Տպենք ընդհանուր տողերի քանակը։

"""

'''
import csv

FILE1 = "file1.csv"
FILE2 = "file2.csv"
OUTPUT = "merged.csv"

rows = set()


with open(FILE1, "r", encoding="utf-8") as f1:
    reader = csv.reader(f1)
    header = next(reader)  # պահում ենք առաջին տողը
    for row in reader:
        rows.add(tuple(row))  # յուրաքանչյուր տող դառնում է tuple և ավելանում set-ի մեջ


with open(FILE2, "r", encoding="utf-8") as f2:
    reader = csv.reader(f2)
    next(reader)  # առաջին տողը չենք վերցնում
    for row in reader:
        rows.add(tuple(row))

# Գրանցում ենք merged.csv ֆայլում
with open(OUTPUT, "w", encoding="utf-8", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(header)  # գրում ենք վերնագիրը
    writer.writerows(rows)   # գրում ենք բոլոր տողերը

#  Տպում ենք ընդհանուր տողերի քանակը
print(f"Ընդհանուր տողերի քանակը (առանց կրկնությունների): {len(rows)}")


'''

# 8. Interactive Calculator Log

        # Ask the user to input a math expression (e.g., 5 + 3 * 2).
        # Evaluate it safely.
        # Save the expression and the result into a log file (expression = result).
        # Allow multiple calculations in one run.

# Օգտվողից վերցնում է մաթեմատիկական արտահայտություն (օր. 5 + 3 * 2)
# Ապահով ձևով հաշվում է արդյունքը
# Գրում է log ֆայլում (արտահայտություն = արդյունք)
# Թույլ է տալիս անել մի քանի հաշվարկ՝ մինչև օգտվողը դուրս գա


'''
import math

LOG_FILE = "calc_log.txt"

print("Ինտերակտիվ հաշվիչ (գրիր 'exit' դուրս գալու համար)")

while True:
    expr = input("Մուտքագրիր արտահայտություն: ")

    if expr.lower() == "exit":
        print("Դուրս եկանք հաշվիչից։")
        break

    try:
        result = eval(expr, {}, math.__dict__)

        print(f"Արդյունք: {result}")

        # Գրանցում ենք log ֆայլում
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{expr} = {result}\n")

    except Exception as e:
        print(f"Սխալ արտահայտություն ({e})")

'''


# 9. Number Classifier
        # Ask the user for a list of numbers separated by commas.
        # Using a for loop, go through each number and classify it as:
            # even,
            # odd,
            # or zero.
        # Save the classifications into a file in the format: number → type.
# Խնդրեք օգտատիրոջից ստորակետերով բաժանված թվերի ցանկ։
# Օգտագործելով for ցիկլ, անցեք յուրաքանչյուր թվի միջով և դասակարգեք այն որպես՝
# զույգ,
# կենտ,
# կամ զրո։
# Պահպանեք դասակարգումները ֆայլում՝ թիվ → տեսակ ձևաչափով։


'''
OUTPUT_FILE = "numbers.txt"

nums_input = input("Մուտքագրիր թվերը, բաժանված ստորակետերով: ")

#  Թվերը վերածում ենք list-ի (int)
numbers = [int(x.strip()) for x in nums_input.split(",")]


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for num in numbers:
        if num == 0:
            kind = "զրո"
        elif num % 2 == 0:
            kind = "զույգ"
        else:
            kind = "կենտ"

        # Տպում ենք էկրանին
        print(f"{num} → {kind}")

        # Գրում ենք ֆայլում
        f.write(f"{num} → {kind}\n")


'''

# 10.Guessing Game

        # Generate a random number between 1 and 50.
        # Using a while loop, let the user guess the number.
        # If the guess is low, print 'low'.
        # If the guess is high, print 'high'.
        # Stop the loop when the guess is correct and save the total number of attempts into a file.

# Ծրագիրը գեներացնի պատահական թիվ (1–50 միջակայքում)
# Օգտվողը փորձի գուշակել
# Ծրագիրը ասի՝ low եթե փոքր է, high եթե մեծ է
# Երբ ճիշտ թվին հասնենք → խաղն ավարտվի և փորձերի քանակը պահպանվի ֆայլում։

'''
import random

OUTPUT_FILE = "attempts.txt"

#  Գեներացնում ենք պատահական թիվ
secret = random.randint(1, 50)

print("Գուշակիր թիվը (1–50)")

attempts = 0

while True:
    guess = input("Գուշակիր թիվը: ")

    if not guess.isdigit():
        print("Խնդրում եմ մուտքագրիր թիվ։")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("mer pahac tivy aveli meca ")
    elif guess > secret:
        print("mer pahac tivy aveli poqra")
    else:
        print(f"Շնորհավոր, ճիշտ գուշակեցիր {attempts} փորձից հետո։")

        # Պահպանում ենք ֆայլում փորձերի քանակը
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"Ընդհանուր փորձեր: {attempts}\n")

        break

'''

# 11. Menu with Match
        # Show a text menu with options (1: Add, 2: Subtract, 3: Multiply, 4: Exit).
        # Ask the user to choose an option.
        # Use match (Python 3.10+) to perform the corresponding action.
        # Continue showing the menu until the user selects Exit.
        # Save all operations and results into a log file.
# Ցուցադրի մենյու
# Ընդունի ընտրություն
# Կատարի գործողություն (գումարում, հանում, բազմապատկում)
# Պահի արդյունքը log ֆայլում
# Շարունակի այնքան ժամանակ, մինչև օգտվողը ընտրի Exit


LOG_FILE = "menu_log.txt"

print(" Մենյու հաշվիչ")

while True:
    print("\n=== Մենյու ===")
    print("1. Գումարում")
    print("2. Հանում")
    print("3. Բազմապատկում")
    print("4. Ելք")

    choice = input("Ընտրիր գործողություն (1-4): ")

    match choice:
        case "1":
            a = float(input("Մուտքագրիր առաջին թիվը: "))
            b = float(input("Մուտքագրիր երկրորդ թիվը: "))
            result = a + b
            print(f"Արդյունք: {result}")
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{a} + {b} = {result}\n")

        case "2":
            a = float(input("Մուտքագրիր առաջին թիվը: "))
            b = float(input("Մուտքագրիր երկրորդ թիվը: "))
            result = a - b
            print(f"Արդյունք: {result}")
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{a} - {b} = {result}\n")

        case "3":
            a = float(input("Մուտքագրիր առաջին թիվը: "))
            b = float(input("Մուտքագրիր երկրորդ թիվը: "))
            result = a * b
            print(f"Արդյունք: {result}")
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{a} * {b} = {result}\n")

        case "4":
            print("Դուրս եկանք ծրագրից։")
            break

        case _:
            print("Սխալ ընտրություն, փորձիր նորից։")




