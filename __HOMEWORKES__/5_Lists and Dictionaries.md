## Theory & Conceptual Questions

1. What is a string in Python? Why are strings called sequences?
2. Explain the difference between:

   * String literals vs string objects
   * Unicode vs ASCII vs bytes
   * Immutable vs mutable objects
3. Show examples of using:

   * single quotes
   * double quotes
   * triple quotes (multiline)
   * raw strings (`r"text"`)
     When would you prefer each?
4. List at least 7 escape sequences and their meanings. Why might `\n` behave differently on Windows vs Linux?
5. Explain with examples:

   * Positive vs negative indexing
   * Slice `s[a:b:c]` (start, stop, step)
   * What happens if indices go out of range?
6. Strings are immutable. Prove it with code. How can we "modify" a string if it is immutable?
7. Compare the three formatting techniques:

   * `%` formatting
   * `.format()` method
   * f-strings
     Which one is most Pythonic today, and why?
8. Explain the difference between `split()`, `partition()`, and `rsplit()`. What’s the difference between `find()` and `index()`?

---

## Fundamental Coding Exercises

1. Create strings using all possible literal notations. Create a raw string showing a Windows file path.
2. Given `s = "Learning Python is fun"`, extract:

   * `"Learning"`
   * `"Python"`
   * `"fun"`
   * Every second character
   * The string reversed
3. Print the following with a single string literal:

   ```
   Line1
       Line2
           Line3
   ```
4. Check if `"thon"` is inside `"Python"`. Repeat `"Py"` 5 times. Concatenate `"Data"` and `"Science"` with a space.
5. Convert an integer, float, and list into strings using `str()`. Convert back where possible.

---

## Working with String Methods

Given:

```python
sentence = "  Python makes STRING handling Easy and Fun!  "
```

Perform:

1. Normalize (strip spaces, make lowercase).
2. Count how many times `"n"` appears.
3. Replace `"easy"` with `"powerful"`.
4. Capitalize only the first word.
5. Split into words and find the longest word.
6. Check if the sentence starts with `"Python"`.
7. Join the words back with commas.

---

## Part D – String Formatting Challenges

1. Using f-strings, format: `"Name: John, Age: 32, Score: 91.23"` (rounded to 2 decimals).
2. Using `.format()`, print a table:

   ```
   Item       Price
   Apple      $0.99
   Banana     $0.50
   Cherry     $2.25
   ```
3. Using `%` formatting, print:

   * `"Pi is approximately 3.1416"` (4 decimals)
   * `"Binary of 12 is 1100"`

---

## Applied Coding Tasks

1. Word Reversal: Write a function that reverses the order of words in a sentence. `"Python is great"` → `"great is Python"`.
2. Palindrome Checker: Write `is_palindrome(s)` that ignores spaces, punctuation, and case.
3. Vowel Counter: Count vowels (`a, e, i, o, u`) in a given text and return a dictionary.
4. Anagram Checker: Write `are_anagrams(s1, s2)` that returns True if two strings are anagrams.
5. Password Validator: A valid password must:

   * Be at least 8 characters long
   * Contain uppercase, lowercase, digit, and symbol
     Write `validate_password(pw)` that returns True/False.

---

## Advanced & Tricky Tasks

1. Manual Split: Implement your own version of `.split()` without using the built-in method.
2. Substring Finder: Implement your own version of `.find()` that returns the index of a substring.
3. Frequency Analysis: Given a paragraph, count the frequency of each character (ignoring spaces). Sort results by frequency.
4. Caesar Cipher: Implement encryption/decryption with shift=3. Example: `"abc"` → `"def"`.
5. Word Censor: Replace all words from a given “banned list” with `"***"`.

---

## Mini Projects

1. Text Statistics Tool: Input a paragraph and compute:
   * Number of characters (with and without spaces)
   * Number of words
   * Average word length
   * Number of sentences
2. Email Extractor: From a given text, extract all valid email addresses using only string methods (no regex).
3. Simple Template Engine: Replace placeholders in a template:

   ```python
   template = "Hello {name}, your balance is {balance} USD."
   ```

   with values from a dictionary.

---

## Reflection Questions

1. Why did Python designers choose to make strings immutable?
2. Which string method(s) do you find most powerful for real-world text processing? Why?
3. How would you explain the difference between raw strings and normal strings to a beginner?
4. When formatting strings, which method would you choose in modern code, and why?
5. How does understanding Unicode affect global software development?

Here is a new, more comprehensive and challenging chapter outline for "Lists and Dictionaries," specifically designed for a complete beginner who only knows how to write flat, sequential code.

### Lists Chapter

-----

#### \#\# Theory & Conceptual Questions

1.  What is a **list** in Python? How is it different from a single string?
2.  How do you find the number of elements in a list?
3.  Explain the difference between a list's **index** and the **element** at that index.
4.  Why are lists called **mutable**? Give a code example showing how to change a list.
5.  What happens when you try to get an item from an index that doesn't exist?
6.  Explain with a simple code example the difference between copying a list using `list_a = list_b` versus `list_a = list_b[:]`.

-----

#### \#\# Fundamental Coding Exercises

1.  Create a list called `student_ages` with the ages of five imaginary friends.
2.  Print the age of the fourth friend in your list.
3.  Given the list `greetings = ['Hello', 'Hi', 'Hey', 'Yo']`, extract and print the first and last elements using a single piece of code.
4.  Combine `part1 = ['Python', 'is']` and `part2 = ['awesome', '!']` into a new list called `sentence_parts`.
5.  Using the `student_ages` list from exercise 1, change the age of the third friend to a new value.
6.  Create a list that contains a string, an integer, a float, and another list.

-----

#### \#\# Practical Exercises with Methods

Given:

```python
zoo_animals = ['lion', 'tiger', 'lion', 'elephant', 'giraffe']
```

1.  Find and print the total number of animals in the `zoo_animals` list.
2.  Use a list method to count how many times `'lion'` appears in the list.
3.  Remove the first instance of `'lion'` from the list.
4.  Find and print the index of `'elephant'`.
5.  Sort the `zoo_animals` list alphabetically.
6.  Append a new animal, `'zebra'`, to the end of the list.
7.  Create a new list by making a copy of `zoo_animals` and clear all items from the original `zoo_animals` list.

-----

#### \#\# Interesting Challenges

1.  **Manual Min/Max Finder:** Given the list `numbers = [25, 12]`, write code to figure out which number is larger and print it. You can't use `if` statements. (Hint: Use a temporary variable and comparison operators).
2.  **"Reverse" a List:** Given a list `data = [1, 2, 3]`, create a new list that contains the elements in reverse order without using any loops or special reverse methods.
3.  **List Swapper:** Given a list `values = ['A', 'B', 'C']`, swap the first and last elements so the list becomes `['C', 'B', 'A']`. You must use a temporary variable to hold one of the values.
4.  **Find a Duplicate:** Given `items = ['a', 'b', 'c', 'b']`, write a sequence of steps to find and print the first duplicate item.
5.  **Sublist from Slices:** Given a list `my_list = ['A', 'B', 'C', 'D', 'E']`, create a new list that contains only the middle three elements.
6.  **Create a Simple Song:** Create a list with three lines of a song. Then, use string and list methods to add a new line to the middle and print the full song with each line on a new line.

-----

### Dictionaries Chapter

-----

#### \#\# Theory & Conceptual Questions

1.  What is a **dictionary** in Python? How is it different from a list?
2.  Explain the concept of a **key-value pair**. What does a key do?
3.  What are some rules for creating a key in a dictionary?
4.  Can a dictionary have duplicate keys? What about duplicate values? Explain.
5.  Why is a dictionary considered **mutable**?

-----

#### \#\# Fundamental Coding Exercises

1.  Create a dictionary called `employee_data` with keys for `'name'`, `'employee_id'`, and `'department'`.
2.  Access and print the employee's department from the dictionary.
3.  Given `inventory = {'notebooks': 50, 'pens': 100}`, update the number of notebooks to `45`.
4.  Add a new key-value pair to the `inventory` dictionary: `'erasers': 75`.
5.  Create a new dictionary by combining `fruits = {'apple': 1, 'banana': 2}` and `citrus = {'lemon': 3}`.
6.  Create a dictionary where the values are lists. For example, a student dictionary where the key is `'courses'` and the value is a list of courses.

-----

#### \#\# Practical Exercises with Methods

Given:

```python
user_profile = {'username': 'coder123', 'email': 'coder@example.com', 'is_active': True}
```

1.  Use a method to get the value for `'email'` without causing an error if the key doesn't exist.
2.  Check if the key `'is_active'` exists in the `user_profile` and print `True` or `False`.
3.  Print a list of all the keys from the `user_profile`.
4.  Print a list of all the values from the `user_profile`.
5.  Remove the `'is_active'` key-value pair.
6.  Use a method to get the value for `'username'` and remove it from the dictionary in a single step.

-----

#### \#\# Interesting Challenges

1.  **Simple Word Counter:** Given a string `"hello world"`, and a dictionary called `counts = {}`, add key-value pairs to the dictionary to count the number of times each word appears.
2.  **Contact Book:** Given an empty dictionary `contacts`, add two contacts to it. Each contact should be a key with a name and a value with a phone number. Then, update one of the phone numbers.
3.  **Total Price:** Given a shopping list dictionary like `prices = {'apple': 0.5, 'banana': 0.25}` and a quantities dictionary `quantities = {'apple': 3, 'banana': 5}`, calculate the total cost for each item and then the grand total.
4.  **Dictionary Swapper:** Given a dictionary `data = {'a': 1, 'b': 2}`, create a new dictionary where the keys and values are swapped.
5.  **Manual Filter:** Given a dictionary `scores = {'math': 85, 'science': 90, 'history': 75}` and a minimum score of 80, create a new dictionary containing only the subjects where the score is 80 or higher.
6.  **Character Frequency:** Given a string `"mississippi"`, create a dictionary that counts how many times each character appears.
7.  **Data Merger:** Given a dictionary of a person's information `personal_info = {'name': 'Alice', 'age': 25}` and a dictionary of their contact info `contact_info = {'email': 'alice@example.com', 'phone': '555-1234'}`, create a single dictionary that contains all the information from both.