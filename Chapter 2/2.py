a = 5
b = 6
print(a * b) # 30
print(a - b) # -1
print(a + b) # 11
print(a / b) # 0.83333333333334

# arithmetic operator

# assignment operator 


# a = 5 mean assign 5 to a mean when tyhping a 5 is called so good


# now 

# a is 5 

a += 3 # a is getting 3 plus so 5 + 3 = 8 so a = 8 now
print(a) # 8
a -= 2 # a is subtracting 2 so 8 - 2 = a or 6 = a, a = 6 now its 6
print(a) # 6
b *= 4  # b is 6 6 * 4 = 24 so b = 24
print(b) # 24

# print("abbas"*5) # python can multiply string with number easily

# *
# **
# ***
# ****
# *****

# make a code to print that paramit

numOfStar = 5

print('\n') # it will make a line break

for star in range(1, numOfStar + 1):
    print("*"*star)


# Comparison Operator

# it always return a value in boolean format in will be true or false

# scenerio

# ==
# >=
# <=
# <
# >
# !=


# print(5 >= a) # false because we work with a while understanding assignment operator so we will make a new variable to get the result true hope it make sense

newA = 5
print(5 >= newA) # true
print(5 > 6) # false
print(5 < 6) # true
print(5 != 5) # false
print(5 == 5) # true

# remember in comment i write boolean value at lowercase but it will always be capitalize mean this true like this is wrong in python True in this format is correct for python e hope it make sense same goes for false like this False is correct false is incorrect


# Logical Operator 

# Truth table of 'or'
# or logic in simple word aik side true return karni chahie toh true dega 

print("True or False Mai Ans: " , True or False) #true
print("False or False Mai Ans: " , False or False) #false
print("True or True Mai Ans: " , True or True) #true
print("False or True Mai Ans: " , False or True) #true
print("5 > 3 or 3 < 3 Mai Ans: " , 5>3 or 3<3) #true
print("5 < 3 or 3 < 3 Mai Ans: " , 5<3 or 3<3) #false


print('\n') # for line break

# Truth table of 'and'
# and logic in simple word dono side true return karni chahie toh true dega 

print("True and False Mai Ans: " , True and False) #false
print("False and False Mai Ans: " , False and False) #false
print("True and True Mai Ans: " , True and True) #true
print("False and True Mai Ans: " , False and True) #false
print("5 > 3 and 3 < 3 Mai Ans: " , 5>3 and 3<3) #false
print("5 < 3 and 3 < 3 Mai Ans: " , 5<3 and 3<3) #false

# now not it convert oppositely mean true to false and simply false to true

print("Using not with True", not(True)) # false
print("Using not with False", not(False)) # true

# har ke jeetna walai ko baazigar khete hai or joh true ko false or false ko true mai convert karde usse not operator kahtai hai

# Type Start : type tell which type is it boolean, string, int & float ... etc

print(type(5)) # <class 'int'>
print(type("abbas")) # <class 'str'>
print(type(5.2)) # <class 'float'>
print(type(True)) # <class 'bool'>


# change type of openator

str = "31"
strFloat = float(str)
strIntegor = int(str)

print(str, strFloat, strIntegor) # 31, 31.0, 31
print(type(str), type(strFloat), type(strIntegor)) # <class 'str'> <class 'float'> <class 'int'>

num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")

print("The Number of Number 1 is", num1) #1
print("The Number of Number 2 is", num2) #2
print("The Sum of number1 and number2 is", num1 + num2) #it will be 12 because its a string not a number

