[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22355953)
# Lab 1 – CIST1600 Practical Scripting
## Purpose of This Lab

This lab introduces you to:
- running Python programs
- using `input()` and `print()`
- understanding how users interact with scripts
- practicing basic testing and debugging

You will complete **two Python programs** in this repository.

Detailed explanations, examples, and workflow instructions are provided in **Canvas**.  
This README focuses only on what to do **inside this repository**.

---

## Files in This Repository

You will work with **both** of the following files:

### `FirstProgram.py`
A guided introductory program that helps you practice:
- user input
- storing values in variables
- simple calculations
- printing output

Instructions for this program are written **inside the file as comments**.

---

### `MadLib.py`
A creative program where you:
- ask the user for words (nouns, verbs, adjectives, etc.)
- store the input
- construct and display a short story

Your program must:
- ask for at least 6 words
- clearly prompt the user
- produce readable output
- run without errors

---

## Required File Headers

Both files must include completed header comments at the top:

```python
# Name:
# Date:
# Assignment: Lab 1
# Purpose:


## FirstProgram.py
The instructions for the program is in code. In python, a pound sign (#) is used to denote a comment. This is code that will not execute and is only there for the benefit of the programmer.

Please label all of your work. There is an area at the top of the code for the file name, your name, the purpose of the file, and the last revision date. Please update all of this info.
```
#FirstProgram.py
#Name:
#Date:
#Assignment: Lab 1
#Purpose: To ask a user for their name, and calculate their birth year.
```
- We are going to make a program that that says hello and asks for your name.  
- We have not yet used input, you will need the following code to make it work. Experiment to answer these questions.
  - Do I need a prompt or can I simply get input?
  - How do I use the value the user just gave me?
  - What is the data type of the value the user just gave me?
    - Can it be printed?
    - What happens if it is a number and we try to do math with it?
    - Can I convert data types if this one is not correct for my needs?

```
answer = input("This is a prompt for info: ")
print(answer)
```

## MadLib.py
Create a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) where the user supplies key adjectives, nouns, verbs, adverbs, or other types of speech then constructs a full story with those words.

Your Mad Lib must:
- Ask for at least 6 words
- Consider usability in design (be clear)
- Create a story with the user supplied words.

There are a few ways to join words in python:

```
noun1 = "Bicycle"
print("I like to ride my " + noun1)
print("I like to ride my", noun1)
```
Test which works best for you, note where the spaces fall using the different methods.

Please remember to fill in all of the info at the top of the document.


## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
- Add a commit message
- Commit to GitHub
- Sync work with Repo
- Submit your repo link to Canvas
