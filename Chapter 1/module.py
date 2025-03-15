# module 3

# imported os
import os

# Steps 

# Step 1: Make a directory_path variable and assign it with its resprective directory according
# Step 2: os is an object go to its method of .listdir to get the list of folders in it no file folders
# Step 3: Make a for loop and print all item


# directory_path="/Users/cv/OneDrive/Desktop/Python/Chapter 1/1.py" #error because not a folder its a file as tell in step 2
directory_path="/Users/cv/OneDrive/Desktop/Python/Chapter 1" # no error because of being a folder

# step 2 followed
content = os.listdir(directory_path)

# step 3 followed
for item in content:
    print(item)

# module 2

# imported pyttsx3 first install it in terminal with pip install pyttsx3

import pyttsx3

# Steps

# Step 1 :- init in variable
# Step 2 :- variable is an object now and in its method tell what to say through method .say
# Step 3 :- then again variable is an object now and in its method tell to be run & wait through runAndWait method
# Step 4 :- Run

engine = pyttsx3.init() # follow step 1
engine.say("Hello Abbas, How are you!") # follow step 2
engine.runAndWait() # follow step 3
# follow step 4 and listen the string you write in step 2 i listen Hello Abbas, How are you!

# module 1

# imported pyjokes first install it in terminal with pip install pyjokes

import pyjokes

# a line for generating random joke through pyjokes
joke = pyjokes.get_joke()

# printing jokes
print(joke)