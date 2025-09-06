from string import punctuation, ascii_lowercase, ascii_uppercase, digits

s = "Learning Python is fun"
print(s[:9])
print(s[9:16])
print(s[19:])
print(s[1::2])
print(s[::-1])
print("line1\n  line2\n     line3")
print("""line1
    line2
         line3""")
if "thon" in 'python':
    print("line1\n  line2\n     line3")
print("line1\n  line2\n     line3")
if "thon" in 'python':
    for i in range(5):
        print("py")
a="Data"
b="Science"
print(f"{a} {b}")
print(a+" "+b)

sentence = "  Python makes STRING handling Easy and Fun!  "
print(sentence.casefold())
print(sentence.replace(" ",""))
print(sentence.count("n"))
print(sentence.replace("Easy","powerful"))
words=sentence.split()
word=words[0]
replaceword=word.upper()
print(sentence.replace(word,replaceword))
for i in range(1,len(words)-1):
    if len(words[i]) >= len(word):
        word=words[i]
print(word)
print(words[0]=="Python")
print(sentence.lstrip().rstrip().replace(" ",","))

Name="John"
Age=32
Score=91.23
print(f"{Name} {Age} {Score}")
items=["Apple","Banana","Cherry"]
price=[0.99,0.50,2.25]
print("\nItems","Price")
for i in range(3):
    print("{} ${}".format(items[i],price[i]))


def myreverse (sentence):
    listOfsentence=sentence.split()
    reversedsentence=listOfsentence[::-1]
    return " ".join(reversedsentence)
a=myreverse("Python is great")
print(a)
def mypalidrome (myword):
    return myword.split()==myword.split()[::-1]
print(mypalidrome("madam"))
a="abc"
b="aeiou"
count=0
for i in range(len(a)):
    for x in range(len(b)):
        if  a[i]==b[x]:
            count+=1
            break
print(count)

def are_anagrams(word1, word2):
    words1 = list(word1)
    words2 = list(word2)
    answer=False
    if len(words1) == len(word2):
        for wordOne in words1:
            if  word2.find(wordOne) != -1:
                words2.pop(words2.index(wordOne))
                word2="".join(words2)
                answer=True
            else:
                answer=False
                break

    return answer
print(are_anagrams("listen", "silent"))

def checkPassword(password):
    symbols = list(password)
    lowercase=False
    uppercase=False
    digit=False
    punct=False
    notfound=True
    if len(symbols)>=8:
        for symbol in symbols:
            if ascii_lowercase.find(symbol) != -1:
                lowercase=True
            elif ascii_uppercase.find(symbol) != -1:
                uppercase=True
            elif ascii_uppercase.find(symbol) != -1:
                uppercase=True
            elif digits.find(symbol) != -1:
                digit=True
            elif punctuation.find(symbol) != -1:
                punct=True
            else:
                notfound=False
        if lowercase and uppercase and digit and punct and notfound:
                return True
        else:
            return False
    else:
        return False
def mySplit (sentence,splitobject=" "):
    word=""
    myList=[]
    rangestart=0
    a=True
    while True:
        if sentence[rangestart:].find(splitobject)!=-1:
            word+=sentence[rangestart:rangestart+sentence[rangestart:].find(splitobject)]
            myList.append(word)
            word=""
            rangestart+=sentence[rangestart:].find(splitobject)+1
        else:
            word+=sentence[rangestart:]
            myList.append(word)
            return myList

a="abc, sjkf, cjkash"
print(mySplit(a," "))
from pprint import pprint

def myfind(myString,searchString):
    word=""
    myList=list(myString)
    for i in range(len(myList)):
        if myList[i] == searchString[0]:
            word=word.join(myList[i:i+len(searchString)])
            if word == searchString:
                return i
            else:
                word=""
                continue
    return -1

a="AFJHDKJHGIU"
print(myfind(a,"H"))

def sortByFrequency(paragraph):
    paragraph = paragraph.replace(' ', '')
    myList= list(paragraph)
    myChars = list(set(paragraph))
    myChars.sort()
    for x in range(len(myChars)):
        for i in range(1,len(myChars)):
            if  myList.count(myChars[i-1])>myList.count(myChars[i]):
                myChars[i-1],myChars[i]=myChars[i],myChars[i-1]
    myChars=myChars[::-1]
    myString = ''.join(myChars)
    return myString

print(sortByFrequency("aa  bbbbbb  cccc  ddddddd"))

def caesar_cipher(text, shift):
    for char in text:
        text=text.replace(char, chr(ord(char) + shift))
    return text

print(caesar_cipher('abc', 3))

def bannedText(text,bannedList):
    for word in bannedList:
        text = text.replace(word,'****')
    return text

print(bannedText("nigga you are crazy man, nigger",["nigga","nigger"]))

def statisticOfSentences(paragraph):
    numberOfSentences = len(paragraph.split("."))
    numberOfWords = len(paragraph.split(" "))
    numberOfCharactersWithoutSpaces = len(paragraph.replace(" "or "." or "," or "?"or"!",""))
    numberOfCharacters = len(paragraph.replace("." or "," or "?" or"!",""))
    AverageLenghtOfWord=numberOfCharactersWithoutSpaces//numberOfWords
    return print(f"numberOfSentences {numberOfSentences}, numberOfWords {numberOfWords}, numberOfCharacters {numberOfCharacters}, numberOfCharactersWithoutSpaces {numberOfCharactersWithoutSpaces}, AverageLenghtOfWord {AverageLenghtOfWord}")

statisticOfSentences("Hello World .,?! fka")

def emailchecker(email,emailList):
    for emails in emailList:
        if email.find(emails) != -1:
            return True
    return False

print(emailchecker("zhan200423@outlook.ru",["@gmail.com","@mail.ru","@icloud.com","@outlook.com"]))

user={
    "name": input("Enter your name: "),
    "balance": int(input("Enter your balance: ")),
}
print(f"Hello dear {user['name']} your  balance is {user['balance']}")

student_ages=[24,15,35,14,96]
print(student_ages[3])

greetings = ['Hello', 'Hi', 'Hey', 'Yo']
print(greetings[0],greetings[-1])

part1 = ['Python', 'is']
part2 = ['awesome', '!']
sentence_parts=part1+part2
print(sentence_parts)

student_ages[2]=32
print(student_ages[2])

new_List=[15,2.3,"hello",['world']]
print(new_List)

zoo_animals = ['lion', 'tiger', 'lion', 'elephant', 'giraffe']
print(len(zoo_animals))
print(zoo_animals.count('lion'))
zoo_animals.pop(zoo_animals.index('lion'))
print(zoo_animals)
print(zoo_animals.index('elephant'))
zoo_animals.sort()
print(zoo_animals)
zoo_animals+=["zebra"]
zoo_animals.append("giraffe")
print(zoo_animals)
zoo_animals_copy=zoo_animals.copy()
zoo_animals.clear()
print(zoo_animals)
print(zoo_animals_copy)

numbers=list(map(int,(input("enter numbers separated by spaces: ")).split()))
def maxOfTwoNumbers(numbers):
    maximum = 0
    for number in numbers:

        if int(number) > maximum:
            maximum = number
    return maximum
print(maxOfTwoNumbers(numbers))

data = [1, 2, 3]
reverseData = data[::-1]
print(reverseData)

values = ['A', 'B', 'C']
values[0],values[-1]=values[-1],values[0]
print(values)

def findDuplicate(listwithduplicates):
    myList = listwithduplicates.copy()
    mySet = set(listwithduplicates)
    for item in mySet:
        myList.remove(item)
    return myList[0]

items = ['a', 'b', 'c', 'b']
print(findDuplicate(items))

my_list = ['A', 'B', 'C', 'D', 'E']
new_list = my_list[1:4]
print(new_list)

employee_data=dict.fromkeys(["name","employee_id","department"])
employee_data["department"]="HR"
print(employee_data["department"])

inventory = {'notebooks': 50, 'pens': 100}
inventory['notebooks']=45
inventory.update({'erasers': 75})
pprint(inventory)

fruits = {'apple': 1, 'banana': 2}
citrus = {'lemon': 3}
fruits.update(citrus)
pprint(fruits)

university={"professors":[],"students":[],"faculty":[],}
pprint(university)

user_profile = {'username': 'coder123', 'email': 'coder@example.com', 'is_active': True}
print(user_profile.get('email'))
if "is_active" in  list(user_profile.keys()):
    print(f"The user is active exist and it's {user_profile.get('is_active')}")
else:
    print("The user is not active")

print(list(user_profile.keys()))
print(list(user_profile.values()))

del user_profile['is_active']
pprint(user_profile)
username=user_profile.pop('username')
print(username)
pprint(user_profile)

ourString="Hello World"
ourString=ourString.split()
counts=dict.fromkeys(ourString)
for x in ourString:
    counts.update({x:ourString.count(x)})
pprint(counts)

contactBook={"Contact1":"055112233","Contact2":"09422233","Contact3":"095112425"}
contactBook["Contact1"] = "055100233"
pprint(contactBook)

prices = {'apple': 0.5, 'banana': 0.25}
quantities = {'apple': 3, 'banana': 5}
check={'apple':prices['apple']*quantities['apple'],'banana':prices['banana']*quantities['banana'],}
check['summary']=check['apple']+check['banana']
print(f'apple costs {check["apple"]}, banana costs {check["banana"]}, sum was {check["summary"]}')

data = {'a': 1, 'b': 2}
reversed_data={}
for key, value in data.items():
    reversed_data.update({value:key})
pprint(data)
pprint(reversed_data)

scores = {'math': 85, 'science': 90, 'history': 75}
minimum=80
new_scores={}
for key, value in scores.items():
    if value>=minimum:
        new_scores[key]=value
pprint(new_scores)

OurWord="mississippi"
OurWord=list(OurWord)
OurSet=set(OurWord)
newDict= {}
for letter in OurSet:
    newDict[letter]=OurWord.count(letter)
pprint(newDict)

personal_info = {'name': 'Alice', 'age': 25}
contact_info = {'email': 'alice@example.com', 'phone': '555-1234'}
new_personal_info = personal_info | contact_info
pprint(new_personal_info)


















