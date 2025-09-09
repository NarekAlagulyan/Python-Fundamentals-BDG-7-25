#String Fundamentals Homework
# Part 1
# 1. How can you type a string literal with single and double quotes inside it?
text = "He said: \"It's fine!\" "
text1 = 'He said: "It\'s fine!" '
print(text)
print(text1)

# 2. How can you type a multiline string?
text2 = """one
two
threee
"""

print(text2)

# 3. Name at least three string methods.
# lower() → փոքրատառ դարձնել
# upper() → մեծատառ դարձնել
# strip() → հեռացնել դատարկ տեղերը սկզբից ու վերջից
# split() → բաժանել string-ը մասերի
# replace() → փոխարինել բառ/տեքստ

# 4. Are strings mutable or immutable? What does this mean for your code?

# string-երը immutable են (չեն փոփոխվում տեղում):
# Սա նշանակում է, որ երբ փոփոխություն ես անում (օր․ replace կամ +), իրականում ստեղծվում է նոր string օբյեկտ, ոչ թե փոփոխվում է հինը։

s = "hello"
s.upper()
print(s)   # hello (մնաց նույնը)
s = s.upper()
print(s)   # HELLO (ստեղծվեց նոր string)
# 5. What is the difference between the string find and index methods?
# find() → եթե չի գտնում, վերադարձնում է -1
# index() → եթե չի գտնում, Error է տալիս ValueError

# 6. How can you check if a string contains only alphabetic characters?
# Օգտագործում ենք .isalpha() մեթոդը

word = "Python"
print(word.isalpha())  # True

# 7. How do you remove whitespace from the ends of a string?
s = "   hello   "
print(s)
print(s.strip())  # "hello"

# 8. How would you split a string into a list of words?
text = "Python makes coding fun"
words = text.split()
print(words)  # ['Python', 'makes', 'coding', 'fun']



# Part 2
# Let's test your string smarts with some more tricky questions!

# 1. What is the output of the following code? `print('H' + 'a' * 5)`
print('H' + 'a' * 5) #Haaaaa

# 2. How would you get the last character of a string `s` without using `len()`?
last = s[-1]
# 3. If `s = 'supercalifragilisticexpialidocious'`, what would `s.find('g')` return?
s = 'supercalifragilisticexpialidocious'
xx = s.find('g')
print(xx)

# 4. How would you convert the string `'123'` into an integer?
num = int('123')

# 5. True or False: `'apple'.upper() == 'Apple'.upper()`
print('apple'.upper() == 'Apple'.upper())

# 6. What method would you use to replace all occurrences of `'i'` with `'o'` in a string?
new_s = s.replace('i', 'o')

# 7. How can you create a raw string? Why would you need one?
# Raw string = r"..." կամ r'...'
path = r"C:\new\test"
# Առանց r-ի, \n կդիտվեր newline, իսկ raw string-ում պահվում է հենց `\n`
# Օգտագործվում է paths, regex-երի և escape-ների հետ աշխատելիս

# 8. What is the result of `'Python'[1:4]`?
# yth

# 9. New! What does the `strip()` method do? Can you give an example?
# Հեռացնում է whitespace-ը (դատարկ տեղերը, tab, newline) string-ի սկզբից ու վերջից։
s = "   hello world   "
print(s.strip())   # "hello world"

# 10. New! How can you check if a string `s` starts with the word `"Hello"`?
s.startswith("Hello")

# 11. New! What is the output of `'python'.islower()`?
# True

# 12. New! How would you join a list of strings `['Hello', 'world']` into a single string with a space in between?
w = ' '.join(['Hello', 'world'])
print(w)


# Part 3: Easy String Tasks
# More practice to build your confidence.

# 1. Greeting Card: Create a variable `name` and assign your name to it. Then create another variable `greeting` and assign a nice message to it. Finally, print the greeting and your name together.
name = "Anna"
greeting = "inchvor ban !!!!"
print(greeting, name)
# 2. String Repeater: Ask the user for their favorite word and a number. Then, print their favorite word that many times.
# word = input("Enter your favorite word: ")
# number = int(input("Enter a number: "))
# print(word * number)

# 3. Slicing Fun: Create a string that is at least 10 characters long. Then print:
#    * The first three characters.
#    * The last three characters.
#    * The string backward.
s = "programming"
print(s[:3])
print(s[-3:])
print(s[::-1])

# 4. Case Converter: Create a string with a mix of uppercase and lowercase letters. Print the string in all uppercase and then in all lowercase.
text = "PyThOn"
print(text.upper())
print(text.lower())

# 5. Character Counter: Ask the user for a sentence and a letter. Count how many times that letter appears in the sentence.

# sentence = input("Enter a sentence: ")
# letter = input("Enter a letter: ")
# count = sentence.count(letter)
# print(f"'{letter}' krknvum e {count} angam.")

# 6. New! The Titleizer: Take a sentence from the user (e.g., `"the quick brown fox"`) and print it in title case (`"The Quick Brown Fox"`).

# sentence = input("Enter a sentence: ")
# print(sentence.title())

# 7. New! Whitespace Warrior: Create a string with extra spaces at the beginning and end (e.g., `"   some text   "`). Print the string with the extra spaces removed.

s = "   some text   "
print("Before:", repr(s))
print("After :", repr(s.strip()))

# 8. New! The Replacer: Create a sentence like `"I like cats."` Ask the user for a word to replace `"cats"` with, and print the new sentence.

# sentence = "I like cats."
# word = input("Replace 'cats' with: ")
# new_sentence = sentence.replace("cats", word)
# print(new_sentence)

# Part 4: Brain-Teaser String Challenges (More Puzzles!)

# 1. Palindrome Checker: A palindrome is a word or phrase that reads the same backward as forward (e.g., `"madam"`, `"racecar"`). Write a script that checks if a given word is a palindrome. You are not allowed to use any loops. (Hint: Slicing is your friend!)

word = input("Մուտքագրեք բառը: ")

if word == word[::-1]:
    print("Այո, սա պալինդրոմ է")
else:
    print("Ոչ, սա պալինդրոմ չէ")
# 2. The Formatter: Create a Mad Libs-style script. Create a story with placeholders like `[adjective]`, `[noun]`, `[verb]`. Ask the user for words to fill in these placeholders and then print the final story using string formatting.

adjective = input("Մուտքագրեք ածական: ")
noun = input("Մուտքագրեք գոյական: ")
verb = input("Մուտքագրեք բայ: ")

story = f"Մի օր {adjective} {noun}-ը որոշեց {verb} ամբողջ օրը։"

print("\nԱհա ձեր պատմությունը:")
print(story)
# Մուտքագրեք ածական: զվարճալի
# Մուտքագրեք գոյական: կատու
# Մուտքագրեք բայ: պարել

# 3. The Great Swap: Given a string, create a new string where the first and last characters are swapped. For example, `'python'` becomes `'nythop'`.

text = input("Մուտքագրեք բառ: ")

if len(text) < 2:
    swapped = text
else:
    swapped = text[-1] + text[1:-1] + text[0]

print("Արդյունք:", swapped)

# 4. New! The Pig Latin Translator: Write a script that translates a single word into Pig Latin. The rule is simple: move the first letter to the end of the word and add `"ay"`. For example, `"python"` becomes `"ythonpay"`.

word = input("Մուտքագրեք բառ: ")

pig_latin = word[1:] + word[0] + "ay"
print("Pig Latin տարբերակը:", pig_latin)

# 5. New! The Vowel Remover: Ask the user for a sentence and create a new sentence with all the vowels (`a, e, i, o, u`) removed. (Hint: you can use the `replace()` method multiple times).

sentence = input("Մուտքագրեք նախադասություն: ")


vowels = "aeiouAEIOU"
for v in vowels:
    sentence = sentence.replace(v, "")

print("Առանց ձայնավորների:", sentence)

# կամ
sentence = "Hello World"
sentence = sentence.replace("a", "")
sentence = sentence.replace("e", "")
sentence = sentence.replace("i", "")
sentence = sentence.replace("o", "")
sentence = sentence.replace("u", "")
sentence = sentence.replace("A", "")
sentence = sentence.replace("E", "")
sentence = sentence.replace("I", "")
sentence = sentence.replace("O", "")
sentence = sentence.replace("U", "")

print(sentence)

# կամ
import re

sentence = "Hello World"
result = re.sub(r"[aeiouAEIOU]", "", sentence)
print(result)
