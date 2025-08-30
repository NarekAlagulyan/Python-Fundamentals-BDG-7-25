"""
Theory & Conceptual Questions

1․What is a string in Python? Why are strings called sequences?
String–ը սիմվոլների հաջորդականություն է, որը գրվում է չակերտների մեջ ('hello', "hello"):
Python–ում string–ը str դասի օբյեկտ է։


2.Explain the difference between:

2.1 String literals vs string objects
    String literal-ը այն, ինչ գրում ենք կոդի մեջ չակերտներով։
    word = "hi"

    String object-ը String literal-ից ստեղծված  օբյեկտ հիշողության մեջ։
    երկուսն էլ str օբյեկտ են հիշողության մեջ,
    պարզապես literal-ը այն գրավոր արտահայտությունն է կոդում, իսկ object-ը այն, ինչ Python-ը պահում է RAM–ում։
   """
from xndirner_list import words
from xndirner_string import longest_word

a = "hello"
b = str("hello")
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>

"""
    2.2 Unicode vs ASCII vs bytes
    ASCII
    Ստանդարտ կոդավորում 7-bit, որը կարող է ներկայացնել միայն 128 սիմվոլ՝ անգլերեն տառեր, թվեր, նշաններ։
    Օրինակ՝ 'A' → 65, 'a' → 97։
    Հիմնականում միայն լատինատառ տեքստերի համար է։
"""
s = "Hello"
print(ord('H'))  # 72
"""
    Unicode
    Համընդհանուր կոդավորում, որը կարող է ներկայացնել բոլոր լեզուների տառերը, սիմվոլները և էմոջիները։
    Python 3–ում բոլոր str օբյեկտները արդեն Unicode տողեր են։
"""
s = "Աննա 😊"
print(s)          # Աննա 😊
print(len(s))     # 6 (հաշվում է տեսանելի սիմվոլները)
"""
    Bytes
    Bytes – բայթերի շարք, տվյալներ որոնք օգտագործվում են ցանցային փոխանցումների, ֆայլերի ընթերցման կամ կոդավորման/դեկոդավորման ժամանակ։
    Bytes–ը ստեղծվում է .encode() մեթոդով, և հնարավոր է վերադարձնել տող՝ .decode()-ով։
"""
s = "Աննա 😊"
b = s.encode("utf-8")  # տող → bytes
print(b)               # b'\xd4\xb1\xd5\xb6\xd5\xa1\xd5\xb6\xd5\xa1 \xf0\x9f\x98\x8a'

s2 = b.decode("utf-8")  # bytes → str
print(s2)                # Աննա 😊
"""
    2.3 Immutable vs mutable objects
    Immutable նշանակում է, որ ստեղծվելուց հետո չես կարող փոխել դրանց ներքին արժեքը։
    Եթե ցանկանում ես «փոփոխել», Python–ը իրականում ստեղծում է նոր օբյեկտ։
    """
    # String – անփոփոխելի

s = "hello"
print(id(s))  #  Օբյեկտի հասցե հիշողության մեջ
s = s + " world"  # Ստեղծվում է նոր օբյեկտ
print(id(s))  #  Այլ id է


"""
    Այստեղ s-ը նոր արժեք ստացավ, բայց նախկինի վրա փոփոխություն չի կատարվել։
          
        
    Mutable
    Mutable նշանակում է, որ արժեքը կարելի է փոփոխել տեղում, առանց նոր օբյեկտ ստեղծելու։
"""
lst = [1, 2, 3]
print(id(lst))  # Օբյեկտի հասցե
lst.append(4)   # Փոփոխություն տեղում
print(lst)      # [1, 2, 3, 4]
print(id(lst))  # նույն id-ն մնաց

"""
Այստեղ lst-ը փոխվեց նույն օբյեկտի վրա, նոր օբյեկտ չի ստեղծվել։



3.Show examples of using:

single quotes
"""
s1 = 'Բարև'
print(s1)   # Բարև
# Հարմար է, եթե տեքստի մեջ կան կրկնակի չակերտներ։
s = 'He said: "Hello!"'


# double quotes
s2 = "Hello world"
print(s2)   # Hello world
# Հարմար է, եթե տեքստի մեջ կան մեկական չակերտներ։
s = "It's a nice day"
    # triple quotes (multiline)
# Օգտագործվում է բազմատող տեքստերի համար։
s3 = """    Սա
    բազմատող
    տեքստ է"""
print(s3)

    # raw strings (r"text")
# Raw string–ը չի մեկնաբանում escape սիմվոլները (\n, \t և այլն)։
s4 = r"C:\new\test.txt"
print(s4)   # C:\new\test.txt

    # When would you prefer each?
# '...' և "..." → Ըստ հարմարության, կախված որ չակերտներն ունենք տեքստի մեջ։
# '''...''' կամ """...""" → Բազմատող տեքստ։
# r"..." → File path–եր, regex–եր, որտեղ չենք ուզում, որ escape–ները մշակվեն։


# 4.List at least 7 escape sequences and their meanings. Why might \n behave differently on Windows vs Linux?
# 1. \'  Մեկ չակերտ
print('It\'s a nice day')   # It's a nice day

# 2. \"  Կրկնակի չակերտ
print("He said: \"Hello\"") # He said: "Hello"

# 3. \\  Հետընթաց գիծ
print("C:\\Users\\Anna")    # C:\Users\Anna

# 4. \n  Նոր տող
print("Line1\nLine2")
# Արդյունք՝
# Line1
# Line2

# 5. \t  Tab
print("Column1\tColumn2")
# Արդյունք՝ Column1   Column2

# 6. \r  Carriage return
print("Hello\rWorld")
# Արդյունք՝ World
# (այստեղ 'Hello'-ն ջնջվեց, որովհետև cursor-ը վերադարձավ տողի սկիզբ)

# 7. \b  Backspace
print("Helloo\b!")
# Արդյունք՝ Hello!

# 8. \f  Form feed
print("Page1\fPage2")
# Արդյունք՝ Page1 (էջափոխում) Page2
# (տերմինալում գուցե պարզապես space երևա)

# 9. \u1234  Unicode սիմվոլ
print("\u0531")  # Ա (Հայկական "Ա")


# 5.Explain with examples:

    # Positive vs negative indexing
# Python–ում string (և մյուս sequence–ները) ունեն ինդեքսավորում․
# Դրական ինդեքսները հաշվում են ձախից → աջ (0, 1, 2 ...)
# Բացասական ինդեքսները հաշվում են աջից → ձախ (-1, -2, -3 ...)
l= "Python"
print(l[0])   # 'P'   (առաջին սիմվոլ)
print(l[2])   # 't'   (երրորդ սիմվոլ)
print(l[-1])  # 'n'   (վերջին սիմվոլ)
print(l[-3])  # 'h'   (երրորդը վերջից)

    # Slice s[a:b:c] (start, stop, step)
 # Slice s[a:b:c] (start, stop, step)
# [start:stop:step] → վերցնում է տողի հատվածը․
# start – որ ինդեքսից սկսի (ներառյալ)
# stop – որտեղ կանգնի (բացառյալ)
# step – քանի քայլով առաջանա
k = "abcdefgh"
print(k[2:6])    # 'cdef'   (սկսում է 2–ից, կանգնում է 6–ից առաջ)
print(k[:4])     # 'abcd'   (սկսում է 0–ից մինչև 4–ից առաջ)
print(k[::2])    # 'aceg'   (յուրաքանչյուր երկրորդ սիմվոլ)
print(k[::-1])   # 'hgfedcba' (շրջում է տողը)
    # What happens if indices go out of range?
# եթե չկա այդ ինդեքսը → IndexError։
s = "abc"
# print(s[5])   # IndexError: string index out of range

# Slice–ում (s[a:b:c]) → Python–ը սխալ չի գցում, ուղղակի կտրվածքի չափով վերադարձնում է ինչ կա։
s = "abc"

print(s[0:10])   # 'abc'
print(s[5:10])   # ''      (դատարկ տող)



# 6.Strings are immutable. Prove it with code. How can we "modify" a string if it is immutable?
# Օրինակ
s = "hello"
print(id(s))   # հիշողության հասցե (object ID)

# Փորձենք փոփոխել առաջին սիմվոլը
try:
    s[0] = "H"
except TypeError as e:
    print(e)                   #'str' object does not support item assignment


# Այսինքն՝ մեկ սիմվոլին արժեք տալ չի թույլատրվում։

# Ինչպես է երևում անփոփոխելիությունը
s = "hello"
print(id(s))   # օրինակ՝ 140338573743024

s = s + " world"   # ստեղծում է ՆՈՐ օբյեկտ
print(s)           # "hello world"
print(id(s))       # այլ ID (նոր string object)


# Սա ապացուցում է, որ string–ը չի փոփոխվել տեղում, այլ ստեղծվել է նոր string օբյեկտ։

#Ինչպես “փոփոխել” string, եթե այն immutable է?
# Ստեղծել նոր string replace–ով կամ concatenation–ով

s = "pillow"
s = s.replace("p", "w")
print(s)   # "willow"

# Կտրել (slice) ու նորով հավաքել

s = "hello"
s = "H" + s[1:]
print(s)   # "Hello"


# Փոխակերպել list → փոփոխել → նորից միացնել

s = "hello"
lst = list(s)     # ['h', 'e', 'l', 'l', 'o']
lst[0] = "H"
s = "".join(lst)
print(s)   # "Hello"


# Ուրեմն՝ string–ը միշտ immutable է, իսկ “փոփոխելը” իրականում նշանակում է ստեղծել նոր string օբյեկտ։



# 7.Compare the three formatting techniques:

    # % formatting
    # .format() method
    # f-strings Which one is most Pythonic today, and why?

# 1. % formatting (հին, C-շ стиlի)

# Օգտագործում է % օպերատոր, ինչպես C լեզվում․
name = "Աննա"
age = 24
print("Անունը %s է, տարիքը %d" % (name, age))
# Անունը Աննա է, տարիքը 24

# Պարզ, հին Python կոդում շատ տարածված է։
# Անհարմար է բարդ արտահայտությունների կամ բազմաթիվ փոփոխականների դեպքում։
# Սխալների հավանականություն կա, եթե placeholder–ները չեն համապատասխանում։


#2. .format() մեթոդ (Python 2.6+ / 3+)
# Օգտագործում է .format() ֆունկցիան․

name = "Աննա"
age = 24
print("Անունը {} է, տարիքը {}".format(name, age))
print("Անունը {0} է, տարիքը {1}".format(name, age))
print("Անունը {n} է, տարիքը {a}".format(n=name, a=age))

# Ավելի ճկուն է, կարող ես փոփոխականները տեղադրել ըստ ինդեքսի կամ անունով։
# Կարելի է ձևաչափել թվեր, alignment, padding։
# Ավելի երկար է կոդը, քան պետք է։


# 3. f-strings (Python 3.6+)
# Օգտագործում է f"" սինտաքս, և ուղղակի ներսում {}–ում գրում ես արտահայտությունը։
name = "Աննա"
age = 24
print(f"Անունը {name} է, տարիքը {age}")
print(f"{name.upper()} հաջորդ տարի կլինի {age + 1} տարեկան")

# Ամենակարճ ու ընթեռնելի սինտաքս։
# Թույլ է տալիս արտահայտություններ ներսում ({age+1}, {name.upper()})։
# Ավելի արագ է, քան .format() և %։
# Աշխատում է միայն Python 3.6+։

# Ո՞րը է “Pythonic” այսօր
# f-strings (f"") — համարվում է Pythonic և ժամանակակից լավագույն տարբերակը․
# Կարդացվող է,
# Արագ է,
# Թույլ է տալիս inline արտահայտություններ։


# 8.Explain the difference between split(), partition(), and rsplit(). What’s the difference between find() and index()?
# 1. split(sep, maxsplit)
# Կտրտում է տողը բաժանարարով → վերադարձնում է list։
# maxsplit → քանի անգամ բաժանի (ձախից)։

s = "a,b,c,d"
print(s.split(","))      # ['a', 'b', 'c', 'd']
print(s.split(",", 2))   # ['a', 'b', 'c,d']  (մաքսիմում 2 կտրվածք)

# 2. rsplit(sep, maxsplit)
# Նույնը, բայց բաժանումը սկսում է աջից։
s = "a,b,c,d"
print(s.rsplit(",", 2))  # ['a,b', 'c', 'd']  (մաքսիմում 2 կտրվածք աջից)

# 3. partition(sep)
# Գտնում է առաջին բաժանարարի տեղը։
# Վերադարձնում է 3-մասանոց tuple՝ (մինչև, բաժանարար, հետո)։
s = "a,b,c,d"
print(s.partition(","))   # ('a', ',', 'b,c,d')
print(s.rpartition(","))  # ('a,b,c', ',', 'd') (աջից առաջինը)
# Այսինքն՝ split/rsplit տալիս են list,
# partition/rpartition տալիս են 3-մաս tuple։



# Fundamental Coding Exercises
# 1.Create strings using all possible literal notations. Create a raw string showing a Windows file path.
# 1) Սովորական string-եր
s1 = 'spam'
s2 = "spam"
# 2) Բազմատող
s3 = '''spam
            eggs
         '''
s4 = """spam
            eggs
         """
# 3) Escape-ներով
s5 = 'line1\nline2\tTabbed'  # \n նոր տող, \t tab
# 4) Unicode escape-ներ
s6 = '\u0531\u0561'  # 'Աա' (կանչ Unicode կոդերով)
s7 = '\N{GREEK SMALL LETTER PI}'  # 'π'
# 5) Հին-ոճի "u" նախածանց (Python 3-ում նույնպես կա)
# Python 2-ում (որտեղ դեռ կար str և unicode տիպերի տարբերություն) u"..." նշանակում էր Unicode տող։
# Python 3-ում բոլոր string-երը արդեն Unicode են, ուստի u օգտագործելը այլևս պարտադիր չէ։ Այն պարզապես ընդունվում է, որպեսզի հին կոդը աշխատի առանց սխալի։
s8 = u"unicode string"

# 6) Raw string-եր (backslash-ները չեն մեկնաբանվում)
s9 = r'C:\new\name\test'  # \n չի դառնում նոր տող, մնում է \n
s10 = R"regex:\d+\w*"  # R էլ նույնն է

# 7) f-string-եր (ձևաչափում տեղում)
name = "Anna"
s11 = f"Hello, {name}!"  # ներդրված արտահայտություններ

# 8) Համակցված նախածանցներ
path = r"C:\Users\Anna"
s12 = fr"User path: {path}\files\{2 + 2}"  # raw + f միասին (fr կամ rf)

# 9) Բազմատող raw (regex/ուղիների համար հարմար)
s13 = r"""C:\Program Files\My App\bin\tool.exe
    C:\Windows\System32"""

# 10) Bytes literal (սա string չէ, այլ bytes)
# b1 = b'spam'
# print(b1)          # b'spam'
# print(type(b1))    # <class 'bytes'>
# Byte մեկ մեկ տարրին հասնելիս ստանում ենք ամբողջ թիվ (0-255)

# print(b1[0])       # 115  (ASCII կոդը 's'-ի համար)
b1 = b'spam'  # տեքստ՝ byte-ների տեսքով

# 2․Given s = "Learning Python is fun", extract:
# "Learning"
# "Python"
# "fun"
# Every second character
# The string reversed

s = "Learning Python is fun"

a1 = s[0:8]
a2 = s[9:15]
a3 = s[-3:]
a4 = s[::2]
a5 = s[::-1]
# print(a5)
# 3.Print the following with a single string literal:

# Line1
#    Line2
#        Line3


print("""Line1
    Line2
        Line3
""")

# 4. Check if "thon" is inside "Python". Repeat "Py" 5 times. Concatenate "Data" and "Science" with a space.

print("thon" in "Python")
print("Py" * 5)
x = "Data" + " " + "Science"
print(x)

# 5.Convert an integer, float, and list into strings using str(). Convert back where possible.
num_int = 42
num_float = 3.14
num_list = [1, 2, 3]

# Convert to string
str_int = str(num_int)
str_float = str(num_float)
str_list = str(num_list)

print(str_int, type(str_int))
print(str_float, type(str_float))
print(str_list, type(str_list))

# back
int_back = int(str_int)
float_back = float(str_float)
import ast

list_back = ast.literal_eval(str_list)

print(int_back, type(int_back))
print(float_back, type(float_back))
print(list_back, type(list_back))

# Working with String Methods
    # Working with String Methods
    # Given:
    # sentence = "  Python makes STRING handling Easy and Fun!  "
    # Perform:

    # ․․․Normalize (strip spaces, make lowercase).
    # Հեռացնել տողի սկզբում և վերջում գտնվող ավելորդ բացատները (spaces) → strip()
    # Փոխել բոլոր տառերը փոքրատառ → lower()
    # Count how many times "n" appears.
    # Replace "easy" with "powerful".
    # Capitalize only the first word.
    # Split into words and find the longest word.
    # Check if the sentence starts with "Python".
    # Join the words back with commas.

sentence = "  Python makes STRING handling Easy and Fun!  "
normalized = sentence.strip().lower()
print(s)
count_n = normalized.count("n")
print(count_n)
replaced = normalized.replace("easy", "powerful")
print(replaced)
capitalized = replaced.capitalize()
print(capitalized)
words = capitalized.split()
longest_word = max(words, key=len)
print(words)
print(longest_word)
print(capitalized.startswith("Python"))
joined = ",".join(words)
print(joined)


# Part D – String Formatting Challenges
# 1. Using f-strings, format: "Name: John, Age: 32, Score: 91.23" (rounded to 2 decimals).
name = "John"
age = 32
score = 91.23123
formatted = f'Name: {name}, Age: {age},Score: {score: .2f}'
print(formatted)


# 2. Using .format(), print a table:
    # Item       Price
    # Apple      $0.99
    # Banana     $0.50
    # Cherry     $2.25

print("{:<10} {:>5}".format("Item", "Price"))
print("{:<10} ${:>5}".format("Apple", 0.99))
print("{:<10} ${:>5.2f}".format("Banana", 0.50))
print("{:<10} ${:>5}".format("Cherry", 2.25))

# 3. Using % formatting, print:
    # "Pi is approximately 3.1416" (4 decimals)
pi = 3.14159265
print("Pi is approximately %.4f" % pi)   #Pi is approximately 3.1416


    # "Binary of 12 is 1100"
num = 12
binary_str = bin(num)[2:]
print("Binary of %d is %s" % (num, binary_str))

# %d → integer num
# %s → string binary_str

# նույնը
num = 12
print(f"Binary of {num} is {bin(num)[2:]}")



# Applied Coding Tasks
# 1. Word Reversal: Write a function that reverses the order of words in a sentence. "Python is great" → "great is Python".
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print("Python is great->",reverse_words("Python is great"))

# 2. Palindrome Checker: Write is_palindrome(s) that ignores spaces, punctuation, and case.
def is_palondrome(sentence):
    cleaned = "".join(word.lower() for word in sentence if word.isalnum())
    return cleaned == cleaned[::-1]

print("is palidrome ?",is_palondrome("Anna naan"))
# 3. Vowel Counter: Count vowels (a, e, i, o, u) in a given text and return a dictionary.
def count_vowels(text):
    vowels = "aeiou"
    text_lower = text.lower()
    return {v:text_lower.count(v) for v in vowels}

print(count_vowels("Python is great"))

# 4. Anagram Checker: Write are_anagrams(s1, s2) that returns True if two strings are anagrams.
def are_anagrams(s1, s2):

    s1_clean = "".join(c.lower() for c in s1 if c.isalnum())    # "listen"
    s2_clean = "".join(c.lower() for c in s2 if c.isalnum())    # "silent"
    return sorted(s1_clean) == sorted(s2_clean)                 # ['e', 'i', 'l', 'n', 's', 't']

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))

# 5. Password Validator: A valid password must:
    # Be at least 8 characters long
    # Contain uppercase, lowercase, digit, and symbol Write validate_password(pw) that returns True/False.

import string

def validate_password(pw):
    if len(pw) < 8:
        return False
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in string.punctuation for c in pw)
    return all([has_upper, has_lower, has_digit, has_symbol])


# print(validate_password("Abc123!@"))  # True
# print(validate_password("password"))   # False

#
# user_pw = input("Մուտքագրեք գաղտնաբառը՝ ")
# if validate_password(user_pw):
#     print("Գաղտնաբառը անվտանգ է")
# else:
#     print("Գաղտնաբառը բավարար պայմաններ չի պահպանում")
#


# Advanced & Tricky Tasks
# 1. Manual Split: Implement your own version of .split() without using the built-in method.
def manual_split(s, sep=" "):
    result = []
    word = ""
    for char in s:
        if char == sep:
            if word:           # եթե word ոչ դատարկ է
                result.append(word)
                word = ""
        else:
            word += char
    if word:                  # վերջում ավելացնել վերջին բառը
        result.append(word)
    return result

print(manual_split("Python is great"))  # ['Python', 'is', 'great']


# կամ պարզապես
s = "Python is great"
result = s.split()
print(result)
# 2. Substring Finder: Implement your own version of .find() that returns the index of a substring.
def manual_find(sentence, word):
    n, m = len(sentence), len(word)
    for i in range(n - m + 1):
        if sentence[i:i+m] == word:
            return i
    return -1

print(manual_find("Hello world", "world"))  # 6
print(manual_find("Hello world", "Python")) # -1
# 3. Frequency Analysis: Given a paragraph, count the frequency of each character (ignoring spaces). Sort results by frequency.
from collections import Counter

def freq_analysis(sentence):
    sentence = sentence.replace(" ", "")
    counter = Counter(sentence)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

# counter.items() → դարձնում է list of tuples, օրինակ՝ [('H',1), ('e',1), ('l',3), ...]
# key=lambda x: x[1] → ասում է՝ սորտավորի ըստ value (այսինքն ըստ հաճախականության)։
# reverse=True → նվազման կարգով (ամենահաճախ հանդիպողը առաջինը լինի)։

text = "Hello world"
print(freq_analysis(text))
# [('l', 3), ('o', 2), ('H', 1), ('e', 1), ('w', 1), ('r', 1), ('d', 1)]

# 4. Caesar Cipher: Implement encryption/decryption with shift=3. Example: "abc" → "def".

# chem nayel

# 5. Word Censor: Replace all words from a given “banned list” with "***".

#chem nayel

# Mini Projects
# 1. Text Statistics Tool: Input a paragraph and compute:

    # Number of characters (with and without spaces)
    # Number of words
    # Average word length
    # Number of sentences

def text_stats(paragraph):
    chars_with_spaces = len(paragraph)
    chars_without_spaces = len(paragraph.replace(" ", ""))
    words = paragraph.split()
    num_words = len(words)
    avg_word_len = sum(len(w) for w in words) / num_words if num_words > 0 else 0
    num_sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')

    return {
        "Տառերի քանակ (բացատներով)": chars_with_spaces,
        "Տառերի քանակ (առանց բացատ)": chars_without_spaces,
        "Բառերի քանակ": num_words,
        "Միջին բառի երկարություն": round(avg_word_len, 2),
        "Նախադասությունների քանակ": num_sentences
    }


text = "Python is great! It makes string handling easy. Do you agree?"
print(text_stats(text))



# 2. Email Extractor: From a given text, extract all valid email addresses using only string methods (no regex).

def extract_emails(text):
    words = text.split()
    emails = []
    for w in words:
        if "@" in w and "." in w:
            # մաքրենք հնարավոր կետադրական նշանները սկզբից և վերջից
            email = w.strip(",;:!?")
            emails.append(email)
    return emails

txt = "Contact us at support@vxsoft.com or anna.galstyan@vxsoft.com. Thank you!"
print(extract_emails(txt))
 # կամ
def extract_emails(text):
    return [w.strip(",;:!?") for w in text.split() if "@" in w and "." in w]

txt = "Contact us at support@vxsoft.com or anna.galstyan@vxsoft.com. Thank you!"
print(extract_emails(txt))



# 3. Simple Template Engine: Replace placeholders in a template:
#   template = "Hello {name}, your balance is {balance} USD."
#   with values from a dictionary.

def render_template(template, values):
    result = template
    for key, val in values.items():
        placeholder = "{" + key + "}"
        result = result.replace(placeholder, str(val))
    return result



template = "Hello {name}, your balance is {balance} USD."
values = {"name": "Anna", "balance": 1250.75}
print(render_template(template, values))
# Hello Anna, your balance is 1250.75 USD.
# կամ պարզապես
template = "Hello {name}, your balance is {balance} USD."
print(template.format(name="Anna", balance=1250.75))


# Reflection Questions
# 1. Why did Python designers choose to make strings immutable?

# Ինչո՞ւ Python–ի ստեղծողները ընտրեցին strings–ը անփոփոխ (immutable) դարձնել։
# Անվտանգություն → Եթե մի անգամ string–ը ստեղծվել է, այն չի կարող պատահաբար փոփոխվել։
# Արագություն (performance) → Անփոփոխ օբյեկտները կարող են պահվել հիշողության մեջ "interning"-ի միջոցով (Python–ը նույն string–ը կրկնակի չի պահում)։
# Hashability → Քանի որ string–երը չեն փոխվում, կարելի է դրանք օգտագործել dictionary–ների keys–ում ու set–երում։


# 2. Which string method(s) do you find most powerful for real-world text processing? Why?
# Որ string method–ներն ես ամենահզորն համարում իրական կյանքում։
# split() և join() → տեքստը բաժանելու ու նորից հավաքելու համար։
# replace() → բառեր կամ նիշեր փոխարինելու համար։
# strip() → ոչ պետքական չակերտներ ու space–եր մաքրելու համար։
# lower() / upper() - որոնման համար։
# Օրինակ, email–ներ, անուններ որոնելիս սրանք են ամենաշատ օգտագործվողները։

# 3. How would you explain the difference between raw strings and normal strings to a beginner?

# Normal string → Python–ը escape sequence–ները (\n, \t, \u) մեկնաբանում է։
# Raw string (r"...") → Python–ը ոչինչ չի մեկնաբանում, ամեն ինչ պահում է ինչպես կա։
# Օրինակ՝
# print("C:\\new_folder\\test.txt")   # պետք է կրկնակի \\ գրենք
# print(r"C:\new_folder\test.txt")    # raw string-ով escape պետք չէ

# Դրա համար raw string–երը շատ են օգտագործվում regex–երում։

# 4. When formatting strings, which method would you choose in modern code, and why?

# %  formatting → հնացած է, բայց դեռ հանդիպում է։
# .format() → ավելի ճկուն, լավ տարբերակ է։
# f-strings (Python 3.6+) → ամենաարդի ու ընթեռնելի տարբերակը։
# Այսօր f-strings–ն է համարվում "Pythonic", որովհետև ավելի կարճ ու հասկանալի է։

# 5. How does understanding Unicode affect global software development?
# 1. Բոլոր լեզուների աջակցություն
# ASCII–ն ունի միայն անգլերեն տառեր, թվեր և որոշ նշաններ (ընդամենը 128 սիմվոլ)։
# Unicode–ը ներառում է ավելի քան 150 գրային համակարգ, 140,000+ սիմվոլ․ հայերեն (Ա, Բ, Գ…), չինարեն, արաբերեն, էմոջի 😊 և այլն։
# Եթե ծրագիրը աշխատում է միայն ASCII–ով, այն չի կարող ընդունել անուններ, օրինակ՝ Աննա, 张伟 կամ օգտագործել էմոջի։

# 2. Միատեսակություն բոլոր հարթակներում
# Առանց Unicode–ի, նույն բառը կարող է սխալ երևալ Windows–ում, Linux–ում կամ բրաուզերում։
# Unicode–ը ապահովում է, որ "é" կամ "Ա" բոլոր տեղերում նույն կոդով ներկայացվեն։

# 3. Տվյալների փչացումից խուսափում (mojibake)
# Երբ տեսնում ես անիմաստ նշաններ, օրինակ՝ Ã© փոխարեն é, դա encoding-ի սխալի հետևանք է։
# Unicode (հատկապես UTF-8) օգտագործելը թույլ է տալիս խուսափել այդ սխալներից։
#
# 4. Էմոջիներ, նշաններ և ժամանակակից հաղորդակցություն
# Unicode–ը միայն տառերի համար չէ․ այն ներառում է ❤️, 🔥, 🤖, տարբեր արժույթներ (€, ¥, ₿), մաթեմատիկական նշաններ (∑, √)։
# Այսօր առանց Unicode ծրագրեր գրեթե անհնար է պատկերացնել։
#
# 5. Միջազգային շուկայի համար ծրագրեր
# Եթե ծրագիրը նախատեսված է միայն անգլերենի համար, այն սահմանափակում է օգտատերերին։
# Unicode–ը թույլ է տալիս, որ մեկ և նույն ծրագիրը օգտագործվի տարբեր երկրներում՝ առանց լրացուցիչ փոփոխությունների։
# Եզրակացություն
# Unicode–ը հասկանալը նշանակում է գրել ծրագրեր, որոնք ապահով են, հասկանալի և հարմարավետ ամեն լեզվի և մշակույթի համար։


# Lists Chapter
# ## Theory & Conceptual Questions
# 1. What is a list in Python? How is it different from a single string?
#List → տարրերի հավաքածու է (կարող են լինել թվեր, տեքստեր, այլ list-եր և այլն)։
# String → պարզապես տեքստի հաջորդականություն է (միայն սիմվոլների list-ի նման, բայց immutable)։

my_list = [1, 2, 3, "Python"]  # list
my_string = "Python"           # string

print(type(my_list))
print(type(my_string))

# 2. How do you find the number of elements in a list?
numbers = [10, 20, 30, 40]
print(len(numbers))  # 4

# 3. Explain the difference between a list's index and the element at that index.
fruits = ["apple", "banana", "cherry"]
print(1)          # index թիվն է
print(fruits[1])  # "banana" → index=1-ում գտնվող տարր

# 4. Why are lists called mutable? Give a code example showing how to change a list.
# Mutable նշանակում է, որ կարող ես փոխել list-ի տարրերը տեղում։

nums = [1, 2, 3]
nums[1] = 99
print(nums)  # [1, 99, 3]

# String-ում նույնը անելը Error կտա, որովհետև string immutable է։

# 5. What happens when you try to get an item from an index that doesn't exist?
# IndexError կստանանք։

letters = ["a", "b", "c"]
# print(letters[5])   # IndexError: list index out of range

# 6. Explain with a simple code example the difference between copying a list using list_a = list_b versus list_a = list_b[:].

# list_a = list_b → Երկուսն էլ նույն օբյեկտին են մատնանշում, նույն հասցեն (մեկում փոփոխությունը կանդրադառնա մյուսին)։
# list_a = list_b[:] → Ստեղծվում է նոր copy, և փոփոխությունները չեն ազդում։

list_b = [1, 2, 3]

list_a = list_b        # նույն հղումն է
list_a[0] = 99
print(list_b)          # [99, 2, 3]  → list_b-ն էլ փոխվեց

list_c = list_b[:]     # copy
list_c[0] = 500
print(list_b)          # [99, 2, 3]  → չի փոխվել
print(list_c)          # [500, 2, 3]


# Fundamental Coding Exercises
# Create a list called student_ages with the ages of five imaginary friends.
student_ages = [15, 17, 18, 16, 19]
print("Ընկերների տարիքները:", student_ages)
# Print the age of the fourth friend in your list.
print("Չորրորդ ընկերոջ տարիք:",student_ages[3])
# Given the list greetings = ['Hello', 'Hi', 'Hey', 'Yo'], extract and print the first and last elements using a single piece of code.
greetings = ['Hello', 'Hi', 'Hey', 'Yo']
print(greetings)
print("Առաջին և վերջին ողջույնը:",greetings[0],greetings[-1])
# Combine part1 = ['Python', 'is'] and part2 = ['awesome', '!'] into a new list called sentence_parts.
part1 = ['Python', 'is']
part2 = ['awesome', '!']
sentence_parts = part1 + part2
print(" Միացված ցուցակ:",sentence_parts)

# Using the student_ages list from exercise 1, change the age of the third friend to a new value.
student_ages[2] = 20
print("Փոփոխված տարիքների ցուցակ:",student_ages)
# Create a list that contains a string, an integer, a float, and another list.
mixed_list = ["Anna", 25, 3.14, [1, 2, 3]]
print("Տարբեր տիպի արժեքներով ցուցակ:", mixed_list)

# Practical Exercises with Methods
# Given:
# zoo_animals = ['lion', 'tiger', 'lion', 'elephant', 'giraffe']
# Find and print the total number of animals in the zoo_animals list.
# Use a list method to count how many times 'lion' appears in the list.
# Remove the first instance of 'lion' from the list.
# Find and print the index of 'elephant'.
# Sort the zoo_animals list alphabetically.
# Append a new animal, 'zebra', to the end of the list.
# Create a new list by making a copy of zoo_animals and clear all items from the original zoo_animals list.


zoo_animals = ['lion', 'tiger', 'lion', 'elephant', 'giraffe']
print("Ընդհանուր կենդանիների քանակը:", len(zoo_animals))
zoo_animals.remove('lion')
print("Առաջին 'lion'-ը հեռացրինք:", zoo_animals)
print("elephant'-ի ինդեքսը:", zoo_animals.index('elephant'))
zoo_animals.sort()
print("Տեսակավորված ցուցակ:", zoo_animals)
zoo_animals.append('zebra')
print("6) Ավելացվեց 'zebra':", zoo_animals)
zoo_copy = zoo_animals.copy()
zoo_animals.clear()
print("7) Կրկնօրինակ ցուցակ:", zoo_copy)
print("   Բնօրինակը մաքրված է:", zoo_animals)

#  Interesting Challenges
# 1. Manual Min/Max Finder: Given the list numbers = [25, 12], write code to figure out which number is larger and print it. You can't use if statements. (Hint: Use a temporary variable and comparison operators).
numbers = [25, 12]

a = numbers[0]
b = numbers[1]

maxs = (a > b) * a + (b > a) * b
mins = (a < b) * a + (b < a) * b
print("Մեծ թիվն է:", maxs)
print("Փոքր թիվն է:", mins)
# 2. "Reverse" a List: Given a list data = [1, 2, 3], create a new list that contains the elements in reverse order without using any loops or special reverse methods.

data = [1, 2, 3]
reversed_data = data[::-1]
print("Reverse:", reversed_data)

# 3. List Swapper: Given a list values = ['A', 'B', 'C'], swap the first and last elements so the list becomes ['C', 'B', 'A']. You must use a temporary variable to hold one of the values.
values = ['A', 'B', 'C']
#['C', 'B', 'A']
x=values[0]
values[0]=values[-1]
values[-1]=x
print(values)

# 4. Find a Duplicate: Given items = ['a', 'b', 'c', 'b'], write a sequence of steps to find and print the first duplicate item.
items = ['a', 'b', 'c', 'b']
seen = set()

for item in items:
    if item in seen:
        print("Առաջին կրկնվողը:", item)
        break
    seen.add(item)

# 5. Sublist from Slices: Given a list my_list = ['A', 'B', 'C', 'D', 'E'], create a new list that contains only the middle three elements.
my_list = ['A', 'B', 'C', 'D', 'E']
middle_three = my_list[1:4]
print("Middle three:", middle_three)


# 6. Create a Simple Song: Create a list with three lines of a song. Then, use string and list methods to add a new line to the middle and print the full song with each line on a new line.
song = ["Line 1: Twinkle twinkle little star",
        "Line 2: How I wonder what you are",
        "Line 3: Up above the world so high"]


song.insert(1, "Line 1.5: Like a diamond in the sky")

for line in song:
    print(line)

# Dictionaries Chapter
# ## Theory & Conceptual Questions
# 1. What is a dictionary in Python? How is it different from a list?

# Dictionary-ը Python-ում տվյալների կառուցվածք է, որը պահում է key-value զույգեր։
# List-ը պահում է միայն կարգավորված էլեմենտների հավաքածու, որոնց տեղը որոշվում է ինդեքսով։
# Dictionary-ում էլեմենտները կարգավորված չեն ըստ ինդեքսի, այլ ըստ բանալիների (key)։

# 2. Explain the concept of a key-value pair. What does a key do?
# Dictionary-ում յուրաքանչյուր արժեք (value) կապված է բանալիի (key) հետ։
# Key-ը հանդես է գալիս որպես նույնականացուցիչ, որի միջոցով մենք գտնում կամ փոփոխում ենք արժեքը։

student = {"name": "Anna", "age": 24}
# "name" -> key
# "Anna" -> value

# 3. What are some rules for creating a key in a dictionary?

# Key-ը պետք է լինի hashable օբյեկտ (այսինքն՝ այն պետք է ունենա հաստատուն արժեք և լինի անփոփոխ)։
# Սովորաբար օգտագործվում են՝ string, number, tuple (եթե tuple-ը միայն hashable օբյեկտներ ունի)։
# Key չի կարող լինել՝ list, dictionary կամ set, քանի որ դրանք mutable են։

# 4. Can a dictionary have duplicate keys? What about duplicate values? Explain.
# Կրկնվող բանալի (key) չի կարող լինել։ Եթե փորձենք, վերջինը կփոխարինի նախորդին։

d = {"a": 1, "a": 2}
print(d)  # {'a': 2}


# Կրկնվող արժեքներ (value) կարող են լինել։

d = {"x": 1, "y": 1}
print(d)  # {'x': 1, 'y': 1}

# 5. Why is a dictionary considered mutable?
# Քանի որ մենք կարող ենք dictionary-ի արժեքները փոխել, ավելացնել նոր key-value զույգեր կամ ջնջել զույգեր՝ առանց dictionary-ն նորից ստեղծելու։

student = {"name": "Anna", "age": 24}
print(student)
student["age"] = 25   # արժեքի փոփոխում
student["grade"] = "A"  # նոր key-value զույգի ավելացում
print(student)


# Fundamental Coding Exercises
# 1. Create a dictionary called employee_data with keys for 'name', 'employee_id', and 'department'.
employee_data = {
    "name": "Աննա",
    "employee_id": 101,
    "department": "IT"
}
# 2. Access and print the employee's department from the dictionary.
print(employee_data["department"])
# 3. Given inventory = {'notebooks': 50, 'pens': 100}, update the number of notebooks to 45.
inventory = {'notebooks': 50, 'pens': 100}
inventory["notebooks"] = 45
print(inventory)
# 4. Add a new key-value pair to the inventory dictionary: 'erasers': 75.
inventory["notebooks"] = 45
print(inventory)
# 5. Create a new dictionary by combining fruits = {'apple': 1, 'banana': 2} and citrus = {'lemon': 3}.
fruits = {"apple": 1, "banana": 2}
citrus = {"lemon": 3}

fruits.update(citrus)
print(fruits)
# 6. Create a dictionary where the values are lists. For example, a student dictionary where the key is 'courses' and the value is a list of courses.

student = {
    "name": "Անի",
    "courses": ["Python", "Math", "English"]
}
print(student)


# Practical Exercises with Methods
# Given:
# user_profile = {'username': 'coder123', 'email': 'coder@example.com', 'is_active': True}
user_profile = {
    'username': 'coder123',
    'email': 'coder@example.com',
    'is_active': True
}
# 1. Use a method to get the value for 'email' without causing an error if the key doesn't exist.
email = user_profile.get('email')
print("Email:", email)

# 2. Check if the key 'is_active' exists in the user_profile and print True or False.
print('is_active' in user_profile)
# 3. Print a list of all the keys from the user_profile.
print("Բոլոր բանալիները:", list(user_profile.keys()))
# 4. Print a list of all the values from the user_profile.
print("Բոլոր արժեքները:", list(user_profile.values()))
# 5. Remove the 'is_active' key-value pair.
user_profile.pop('is_active')
print(user_profile)
# 6. Use a method to get the value for 'username' and remove it from the dictionary in a single step.
username = user_profile.pop('username')
print("Username:", username)
print("Նոր dictionary:", user_profile)

# Interesting Challenges
# 1. Simple Word Counter: Given a string "hello world", and a dictionary called counts = {}, add key-value pairs to the dictionary to count the number of times each word appears.
text = "hello world world ooo"
counts = {}

words = text.split()
print(words)
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

# 2. Contact Book: Given an empty dictionary contacts, add two contacts to it. Each contact should be a key with a name and a value with a phone number. Then, update one of the phone numbers.
contacts = {}
contacts["Anna"] = "1234567"
contacts["Bob"] = "9876543"

contacts["Bob"] = "5556789"
print(contacts)
# {'Anna': '123-4567', 'Bob': '555-6789'}

# 3. Total Price: Given a shopping list dictionary like prices = {'apple': 0.5, 'banana': 0.25} and a quantities dictionary quantities = {'apple': 3, 'banana': 5}, calculate the total cost for each item and then the grand total.
prices = {'apple': 0.5, 'banana': 0.25}
quantities = {'apple': 3, 'banana': 5}

total_cost = {}
grand_total = 0

for item in prices:
    cost = prices[item] * quantities.get(item, 0)
    total_cost[item] = cost
    grand_total += cost

print("Մեկի արժեքը:", total_cost)
print("Ընդհանուր գումարը:", grand_total)


# 4. Dictionary Swapper: Given a dictionary data = {'a': 1, 'b': 2}, create a new dictionary where the keys and values are swapped.
data = {'a': 1, 'b': 2}
swapped = {v: k for k, v in data.items()}
print(swapped)
# {1: 'a', 2: 'b'}
# 5. Manual Filter: Given a dictionary scores = {'math': 85, 'science': 90, 'history': 75} and a minimum score of 80, create a new dictionary containing only the subjects where the score is 80 or higher.
scores = {'math': 85, 'science': 90, 'history': 75}
min_score = 80

filtered = {subject: score for subject, score in scores.items() if score >= min_score}
print(filtered)
# {'math': 85, 'science': 90}
# 6. Character Frequency: Given a string "mississippi", create a dictionary that counts how many times each character appears.
text = "mississippi"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
# 7. Data Merger: Given a dictionary of a person's information personal_info = {'name': 'Alice', 'age': 25} and a dictionary of their contact info contact_info = {'email': 'alice@example.com', 'phone': '555-1234'}, create a single dictionary that contains all the information from both.
personal_info = {'name': 'Alice', 'age': 25}
contact_info = {'email': 'alice@example.com', 'phone': '555-1234'}

merged_info = {**personal_info, **contact_info}
print(merged_info)


