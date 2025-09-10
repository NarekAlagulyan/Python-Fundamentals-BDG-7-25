# Lists and Dictionaries Homework
# Part 1
# 1. Name two ways to create an empty list.
empty_list = []
empty_list1 = list()

# 2. How would you add an item to the end of a list?
my_list = [1, 2, 3]
my_list.append(4)

# 3. What is the difference between the append and extend list methods?
a = [1, 2]
b = [3, 4]
a.append(b)   # [1, 2, [3, 4]]
a = [1, 2]
a.extend(b)   # [1, 2, 3, 4]

# 4. How do you remove an item from a list by its position? How about by its value?
numbers = [10, 20, 30, 40]
numbers.pop(2)   #index-ով
numbers.remove(40)  #value-ով

# 5. What does the list sort method do? Does it return a new list?
nums = [3, 1, 2]
nums.sort()      # sort-ով դասավորում ենք -> [1, 2, 3]
# It does NOT return a new list, it modifies the original one.
# list նոր չի սարքում, հենց դա է փոխում

# 6. Name two ways to create an empty dictionary.
empty_dict1 = {}
empty_dict2 = dict()

# 7. How do you access the value associated with a key in a dictionary?
person = {"name": "Anna", "age": 25}
print(person["name"])  # "Anna"

# 8. How do you add a new key-value pair to a dictionary?
person["email"] = "anna․galstyan@vxsoft.com"

# Part 2
# 1. What is the output of [1, 2, 3] + [4, 5, 6]?
print([1, 2, 3] + [4, 5, 6])   #   [1, 2, 3, 4, 5, 6]

# 2. If L = ['a', 'b', 'c'], what does L.pop() do?
L = ['a', 'b', 'c']
L.pop()
print(L)  # ['a', 'b']

# 3. True or False: Dictionaries are ordered collections in modern Python versions.
# True

# 4. How do you get a list of all the keys in a dictionary d?
d = {"key1": 1, "key2": 2}
print(list(d.keys()))


# 5. What is the result of d.get('missing_key', 'default_value') if 'missing_key' is not in d?

print(d.get("missing_key", "default_value"))
# ստուգում է եթե առաջին գրածը չկա, 2րդն է տալիս որպես պատասխան

# 6. Can you have a list as a value in a dictionary?
esim = {"fruits": ["apple", "banana"]}
print(esim)

# 7. What is the difference between del d['key'] and d.pop('key')?
demo = {"x": 1, "y": 2}
del demo["x"]        # deletes without returning
val = demo.pop("y")  # deletes and returns value
print(val)

# 8. How would you create a list of numbers from 1 to 5?
print(list(range(1, 6)))

# 9. New! How can you check if a key 'name' exists in a dictionary d?
d = {"name": "Anna", "age": 25}

print("name" in d)   # True
print("email" in d)  # False

# 10. New! Can a list contain different data types (e.g., numbers and strings)?
mixed = [1, "hello", 3.14]
print(mixed)

# 11. New! What method would you use to get a list of all the values in a dictionary?
print(list(d.values()))


# 12. New! What is the index of the first element in a list?
# 0


# Part 3: Easy-Mode List & Dictionary Task
# 1. Shopping List: Create a list of at least five items you want to buy. Then, do the following:
    # Print the first item.
    # Print the last item.
    # Change the third item to something else.
    # Add a new item to the end of the list.
    # Remove the second item.
    # Print the final list.

shopping = ["bread", "milk", "eggs", "cheese", "butter"]
print(shopping[0])       # first item
print(shopping[-1])      # last item
shopping[2] = "chocolate"
shopping.append("juice")
shopping.pop(1)
print(shopping)


# 2. Contact List: Create a dictionary to store a contact. The keys should be "name", "phone", and "email". Fill in your own information. Then, print the contact's name and email.

contact = {"name": "Աննա", "phone": "123456789", "email": "anna.galstyan@vxsoft.com"}
print(contact["name"])
print(contact["email"])

# 3. Number Sorter: Create a list of five numbers in any order. Sort the list and then print it.
numbers = [4, 1, 5, 2, 3]
numbers.sort()
print(numbers)

# 4. Dictionary Flipper: Create a dictionary with three key-value pairs. Then, create a new dictionary where the keys and values are swapped.

d = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in d.items()}
print(flipped)

#kam


d = {"a": 1, "b": 2, "c": 3}
flipped = dict(map(reversed, d.items()))
print(flipped)


# 5. New! The Guest List: Create a list of people you'd invite to a party. Then, use the len() function to print how many people are on your guest list.
guests = ['Արմեն', 'Մարի', 'Նաիրա']
print(len(guests))

# 6. New! Favorite Colors: Create a dictionary where the keys are your friends' names and the values are their favorite colors. Print the favorite color of one of your friends.
colors = {'Արմեն':'կարմիր', 'Մարի':'կանաչ'}
print(colors['Մարի'])

# 7. New! Popping Fun: Create a list of tasks for the day. Use the pop() method to remove and print the last task you need to do.

tasks = ['workout', 'study', 'shop']
last_task = tasks.pop()
print(last_task)

# Part 4: Mind-Bending List & Dictionary Challenges (More Brain Power!)
# 1. The Duplicator: Create a list with duplicate values. Write a script to remove all the duplicates from the list. (Hint: Think about how another data structure, like a dictionary or a set, might help).
lst = [1,2,2,3,3,3]
lst_no_dup = list(set(lst))
print(lst_no_dup)

# 2. Movie Database: Create a list of dictionaries, where each dictionary represents a movie and has keys for "title", "director", and "year". Add at least three movies. Then, write a script that prints the title and director of each movie.

movies = [
    {'title':'Titanic', 'director':'James Cameron', 'year':1997},
    {'title':'Inception', 'director':'Christopher Nolan', 'year':2010},
    {'title':'Avatar', 'director':'James Cameron', 'year':2009}
]
for m in movies:
    print(m['title'], m['director'])

# 3. The Word Counter: Ask the user for a sentence. Create a dictionary where the keys are the words in the sentence and the values are the number of times each word appears.
sentence = "this is a test this is"
words = sentence.split()
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)

# 4. New! The Gradebook: Create a dictionary to store a student's grades. The keys should be the subjects (e.g., "Math", "Science") and the values should be their scores. Write a script to calculate the average score of the student.

grades = {'Math':90, 'Fizic':80, 'History':85}
average = sum(grades.values()) / len(grades)
print(average)

# 5. New! The List Merger: Create two lists of numbers. Write a script to create a new list that contains all the items from both lists, sorted in ascending order.

list1 = [3,1,4]
list2 = [2,5,0]
merged = sorted(list1 + list2)
print(merged)
