#Project overview:
#Use your knowledge of Python files to take down an evil hacker once and for all.
#The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own.
#Your mission, should you choose to accept it, is threefold.
#You must acquire access to The Fender‘s systems, you must update his "passwords.csv" file to scramble the secret data.
#The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.
#Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice.
#Work with CSV files and other text files in this exploration of the strength of Python file programming.
#


#Import CSV module
import csv

#Create list of users with compromised passwords
compromised_users = []

#Open file and store it in file object
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  #Iterate through each line in CSV and create loop to save each row to temp variable
  for password_row in password_csv:
    #print(password_row["Username"])
    compromised_users.append(password_row["Username"])
#print(compromised_users)

#Create new block open file in write-mode, write each compromised_user to compromised_user_file
with open("compromised_users.txt", "w") as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

#Import JSON file
import json

#Open new json and save as file object
with open("boss_message.json", "w") as boss_message:
  #Create dictionary object with statement to relay boss message
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

#Create new block and open new_passwords.csv in write-mode
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
