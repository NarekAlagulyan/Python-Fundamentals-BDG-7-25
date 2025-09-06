## Tuples, Files, and Everything Else Homework


### Part 1

1.  What is the main difference between a list and a tuple?
2.  How do you create a tuple with a single item?
3.  Can you change an item within a tuple? What if that item is a list?
4.  What does the `open()` function do?
5.  What is the difference between reading a file with `read()` and `readlines()`?
6.  How do you write to a file?
7.  What is the purpose of the `close()` method for files?
8.  What is a context manager (`with` statement) used for with files?

---

### Part 2

1.  What is the output of `(1, 2, 3) * 2`?
2.  True or False: `(1) == 1`.
3.  How can you unpack a tuple `t = (a, b, c)` into three variables?
4.  What mode would you use to open a file for both reading and writing?
5.  If you open a file for writing ('w') that already exists, what happens to its content?
6.  What does a file's `readline()` method return at the end of the file?
7.  Can you have a tuple as a key in a dictionary?
8.  How would you create a tuple from a list?
9.  **New!** What is the benefit of using a tuple over a list?
10. **New!** How would you open a file in binary mode?
11. **New!** What does the file `tell()` method do?
12. **New!** True or False: You must always close a file after opening it.

---

### Part 3

1.  **Coordinate System:** Create a tuple to store the (x, y) coordinates of a point. Then, unpack the tuple into two variables, `x` and `y`, and print them.
2.  **Student Roster:** Create a list of tuples, where each tuple contains a student's name and their score. Print the roster.
3.  **File Writer:** Write a script that asks the user for their name and then writes "Hello, [name]!" to a file named `greeting.txt`.
4.  **File Reader:** Write a script that reads the `greeting.txt` file and prints its content to the console.
5.  **Line by Line:** Create a text file with at least three lines of text. Write a script that reads the file line by line and prints each line.
6.  **New!** **The Logger:** Write a script that asks the user for a message and appends it to a file called `log.txt` with a timestamp.
7.  **New!** **Configuration Settings:** Create a tuple to store some configuration settings for a program, like `('dark_mode', True, 16)`. Unpack these settings into variables and print them.
8.  **New!** **The File Cloner:** Write a script that reads the content of one file and writes it to a new file.

---

### Part 4: Advanced Tuples & Files Puzzles

1.  **The Appender:** Write a script that opens a file in append mode ('a') and adds a new line of text to it each time the script is run.
2.  **The Number Cruncher:** Create a text file with one number on each line. Write a script that reads the file, calculates the sum of all the numbers, and prints the result.
3.  **CSV Creator:** A CSV (Comma-Separated Values) file is a common way to store data. Write a script that creates a CSV-like file. It should be a list of lists, where each inner list represents a row. Write this data to a file, with each inner list on a new line and the items separated by commas.
4.  **New!** **The Story Writer:** Create a script that prompts the user for a series of inputs (e.g., a name, a place, an adjective) and then writes a short story using these inputs into a new text file.
5.  **New!** **The High Score Keeper:** Write a script for a game that stores the high score in a file. When the script runs, it should read the high score from the file, ask the user for their score, and if their score is higher, update the file with the new high score.

***
