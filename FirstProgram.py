#FirstProgram.py
#Talia Astorino:
#January 25, 2026:
#Lab 1 Purpose: To ask a user for their name, and calculate their birth year.

def main():
  print("First Program")
  
print("Hello!")
  #Ask for the user's name
name = input("What is your name?")
  #Use the user's name in the program.
print(f"Hi, {name}, it is nice to meet you!")
  #Ask the user for their age.
age = int(input("How old are you?"))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
birth_year = 2025 - age
print(f"Your birth year is {birth_year}.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
