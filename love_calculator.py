# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
    # "Your score is **x**, you go together like coke and mentos."
    # For Love Scores between 40 and 50, the message should be:
    # "Your score is **y**, you are alright together."
    # Otherwise, the message will just be their score. e.g.:
    # "Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇    

#combine the names
both_names = name1 + name2

#use the lower function to make all letters in lower case
lcs = both_names.lower()

#check your work
# print (f"your names are {lcs}")

#count each letter in the combined name and save it in a variable
t = lcs.count("t")
r = lcs.count("r")
u = lcs.count("u")
e = lcs.count("e")

#add the counts for true
true = t + r + u + e

#check your work
# print(f"your true score is {true}")

#count each letter in the combined name and save it in a variable
l = lcs.count("l")
o = lcs.count("o")
v = lcs.count("v")
e = lcs.count("e")

#add the counts for true
love = l + o + v + e

# check your work
# print(f"your love score is {love}")

# concat the true and love
# observation: we need to convert it in strings
love_score = str(true) + str(love) 

# check your work
# print(love_score)

#add the conditions for the love score and print the result
if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")     