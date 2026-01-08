import random  # imports the random module
import string  # imports the string module

length = int(input("enter the length:")) # get the input from user for length of password 
char = string.digits+"!@#$%^&*()"+string.ascii_uppercase+string.ascii_lowercase  # adds a upper & lower case + special cherater + letters + digits(creates a character pool)
password = "".join(random.choice(char)for i in range(length))   # joins chars and loop the input to mach it wih pass word 
print("pssword generated:",password)  # print the password