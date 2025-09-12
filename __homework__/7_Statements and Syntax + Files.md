### Homework List

1. **Log Writer Program**

    * Write a program that takes comma-separated values as input from the user.
    * Append (extend) the values into a file line by line, like a log.

2. **Dictionary Builder with Pickle**

    * Write a program that reads the content of a file.
    * Treat every **odd row** as a dictionary key and every **even row** as its value.
    * If a row is empty or contains only spaces:

        * Use a **default key** instead of the missing key.
        * Use **None** instead of the missing value.
    * Save the prepared dictionary into a **pickle file**.
    * Load the dictionary back from the pickle file and display its items **line by line**.

3. **Unique Words Logger**
    * Take a sentence as input from the user.
    * Split it into words, remove duplicates, and sort alphabetically.
    * Append the result to a file, each word on a new line.

4. **Reverse File Reader**
    * Read all lines from a file.
    * Reverse their order.
    * Save the reversed content into another file.

5. **JSON Converter**
    * Read a text file where each line contains `key=value`.
    * Convert it into a dictionary.
    * Save the dictionary into a JSON file.
    * Load the JSON file back and print the dictionary.

6. **Word Counter with Pickle**

    * Read a text file.
    * Count how many times each word appears.
    * Store the word-frequency dictionary in a pickle file.
    * Load it back and display the results line by line.

7. **CSV Merger**
    * Have two CSV files with the same columns.
    * Merge them into one file without duplicates.
    * Display the total number of rows after merging.

8. **Interactive Calculator Log**
    * Ask the user to input a math expression (e.g., `5 + 3 * 2`).
    * Evaluate it safely.
    * Save the expression and the result into a log file (`expression = result`).
    * Allow multiple calculations in one run.

9. **Number Classifier**
    * Ask the user for a list of numbers separated by commas.
    * Using a `for` loop, go through each number and classify it as:
        * even,
        * odd,
        * or zero.
    * Save the classifications into a file in the format: `number → type`.

10. **Guessing Game**

    * Generate a random number between 1 and 50.
    * Using a `while` loop, let the user guess the number.
    * If the guess is low, print `'low'`.
    * If the guess is high, print `'high'`.
    * Stop the loop when the guess is correct and save the total number of attempts into a file.

11. **Menu with Match**

    * Show a text menu with options (1: Add, 2: Subtract, 3: Multiply, 4: Exit).
    * Ask the user to choose an option.
    * Use `match` (Python 3.10+) to perform the corresponding action.
    * Continue showing the menu until the user selects Exit.
    * Save all operations and results into a log file.

