
### Getting Started with Git & GitHub for Homework Submission

Welcome\! This guide will walk you through the simple steps to submit your homework assignments using Git and GitHub. Following these steps correctly will help you manage your code and share it with your instructors.

-----

### **Step 1: Get the Code**

You'll start by getting the homework code onto your computer. This is called **cloning** the repository.

1.  **Open your terminal or command prompt.** (On Windows, you can use Git Bash or PowerShell; on Mac/Linux, use Terminal).
2.  In your terminal, type `git clone` followed by your repository's URL.

<!-- end list -->

```bash
git clone <repo-url>
```

3.  Press Enter. This creates a new folder on your computer with all the homework files.

-----

### **Step 2: Do Your Homework**

Now you're ready to work\!

1.  Open the cloned directory using any code editor or Integrated Development Environment (IDE) like PyCharm.
2.  Create a new Python file inside this folder. The name of the file should be the homework name with a `.py` extension (e.g., `homework1.py`).
3.  Write your code inside this new file and save it.

-----

### **Step 3: Save Your Changes (Commit)**

Once you've finished your work, you need to save it to your local Git history. This is called a **commit**.

1.  Go back to your terminal and navigate into the folder you created. Replace `<student-name>` with your actual name.

    ```bash
    cd /<student-name>
    ```

2.  Tell Git which changes you want to include in your save.

    ```bash
    git add .
    ```

    (The `.` means "all changes in the current folder.")

3.  Create your save point with a message. Use the provided format. Replace `<student-name>` and `<homework-name>` with the correct information.

    ```bash
    git commit -m "<student-name>: <homework-name> is done"
    ```

-----

### **Step 4: Push to GitHub**

This is the final and most important step. You will now send your saved changes from your computer to the GitHub website.

1.  In your terminal, type one of the following commands:

    ```bash
    git push
    # OR
    git push -u origin head
    ```

2.  Press Enter. Git will send your commit to your remote repository on GitHub.

3.  Go to the GitHub website and refresh the page. You should see your updated code\! Your instructor can now see and grade your work.