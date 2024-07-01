#Project overview:
#You are a student and you are trying to organize your subjects and grades using Python.
#Let’s explore what we’ve learned about lists to organize your subjects and scores.
#
#

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:

#Creating list for subjects that contains classes and list for grades that contains scores
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Combining subjects & grades lists into 2D list
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#Update 2D list with new grade for another class
gradebook.append(["computer science", 100])
print(gradebook)

#Update 2D list with another new grade for another class
gradebook.append(["visual arts", 93])
print(gradebook)

#Access the index of the grade for your visual arts class and modify it to be 5 points greater
gradebook[-1][-1] = 98
print(gradebook)

#Find the grade value for poetry and remove it
gradebook[2].remove(85)
print(gradebook)

#Now add the grade value for poetry as Pass
gradebook[2].append("Pass")
print(gradebook)

#Create variable that combines last semester and this semester
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
