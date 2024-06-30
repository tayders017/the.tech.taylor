#Project overview:
#The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
#1. Write a Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
#2. Use the following answers:
# - Yes - definitely
# - It is decidedly so
# - Without a doubt
# - Reply hazy, try again
# - Ask again later
# - Better not tell you now
# - My sources say no
# - Outlook not so good
# - Very doubtful
#Optional: 
# - Add your own additional answers
# - Edit output statements to account for empty strings

#Import random module
import random

#Declare 3 variables: assign one as the name of the asker && assign second to yes/no question && assign third to store Magic 8-Ball answers
name = "Batman"
question = "Does the Joker like the batmobile?"
answer = ""

#Declare variable to store randomly generated value & print number
random_number = random.randint(1, 15)
# print(random_number)

#Possible answers in if & elif statements
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Check with Catwoman, then ask again later"
elif random_number == 11:
  answer = "Twoface says no, can this be trusted?"
elif random_number == 12:
  answer = "Arkham Asylum called, outlook not so good"
elif random_number == 13:
  answer = "The Bat-Signal is lit up, Batman is needed!"
elif random_number == 14:
  answer = "Commissioner Gordon confirmed this is true"
elif random_number == 15:
  answer = "Robin is coming, you better run!"
else:
  answer = "Error"

#Output askers name & question
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)
#Output Magic 8-Balls answer
if question == "":
  print("ERROR - No question was provided")
else:
  print("Magic 8-Ball's answer: " + answer)
