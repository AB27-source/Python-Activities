## Section 1 - variables and functions: 
##--------------------------------------
# Question 1: Create two variables. One should be a string data type, and the other should be of type int.
import string
from turtle import title
from unicodedata import name


intVar = 100
stringVar = "Hello"
# Use a single print statement to print both variables:
print("Integer Value = %d & String Value = %s\n" %(intVar, stringVar))

# Question 2: Create a Python function that prints a greeting with a name as the parameter.
def greeting(name):
    print ("Hello %s\n" %(name))

# Invoke the function with a name argument of your choosing:
greeting("Angad")

## Section 2 - lists:
#--------------------------
# Question 3: Create a list of your favorite movies with  at least 4 elements:
fav_movies = ["Spider-Man (2002)", "Batman Returns", "The Batman", "Harry Potter and the Order of the Phoenix"]

# Question 4: Use a print statement to print the list item at the index of 1:
print("Favorite Movie at index 1: %s\n" %(fav_movies[1]));

# Question 5: Append a movie to the end of your list:
fav_movies.append('Dr. Strange')

# Use a print statement to print this ammended list:
print("Favorite Movies: %s\n" %(fav_movies))

## Section 3 - dictionaries:
#---------------------------------

# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
#The keys should be: "color" and "number".
#Fill out the values on your own:
cellphone={
    "Color" : "Dark Green",
    "Number" : "(123)456-7891"
}

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).
print("Cellphone color = %s\n" %cellphone["Color"])



## Section 4 - strings:
#-------------------------------

# Question 8: Create a variable and store a string with multiple words in it:
stringWithMultipleWords = "this is a string with multiple words"

# Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:
newVar = stringWithMultipleWords.title()

# Use a print statement to print the new string:
print ("newVar = %s\n" %newVar);



#Bonus:

# Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

students_in_order = {
  1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
  2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
  3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
}

# Question 10 A: Write a print function that outputs the second student in the dictionary
print("Second student in the dictionary %s\n" %students_in_order[2])
# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary
print("Name: %s \n" %students_in_order[3]["name"])
# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary
print("Age of Esteban = %s" %students_in_order[1]["age"])