#MadLib.py
#Talia Astorino:
#January 25, 2026:
#Lab 1 Purpose: To print a story using user supplied words.

def main():
  print("Madlib")
  #Ask user for words
adjective1 = input("Enter an adjective. ")
adjective2 = input("Enter another adjective. ")
animal = input("Enter an animal. ")
noun2 = input("Enter a noun. ")
verb1 = input("Enter a verb. ")
verb2 = input("Enter another verb. ")
  #Print the story with the user supplied words.
story = ("One day, a " + adjective1 + " " + animal + " escaped from the zoo! It was very " + adjective2 + " and began to " + verb1 + ". The " + noun2 + " came to " + verb2 + " the " + animal + " before returning it to the zoo.")

print("Here is the story for you!")
print(story)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
