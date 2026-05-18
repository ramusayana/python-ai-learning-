name= "Ram"

print(name=="Ram") ## True

print(name=="Rama") ## False

print(name!="Rams") ## True


age=40

if(age==25):
    print("This is wrong")

else:
    print("This is nothing")



if(age!=25):
    print("This is good")

else:
    print("This is nothing")


if(age>=200):
    print("This is correct")
elif(age>=300):
    print("This may be correct")
elif(age!=4):
    print("This is absolute correct")   
else:
    print("This is nothing")    

# comparison variable using and  or

rank=10
experience = 10

if (rank> 8 or experience < 1):
    print("this is to check")
else:
    print("this is nothing")

#####

if(rank>= 8 and experience < 1):
    print("this is to check")
else:
    print("this is nothing")   


######Test #########


test_score = 50 

if test_score>=90:
    print("Excellent")
elif test_score>=75:
    print("this is good")
elif test_score>=50:
    print("This is a pass")
else:
    print("this is failed")



years_experience= 10
knows_python=True 

if years_experience>=5 or knows_python==True:
    print("Ready for AI development")


if years_experience>=1 and  knows_python==True:
    print("Learn Python first")   

if years_experience>=4 and  knows_python==False:
    print("Get more experience")      


years_experience = 10
knows_python = True

if years_experience == 11 or knows_python == False:
    print("Ready for AI development")
elif knows_python == True:
    print("Learn Python first")
else:
    print("Get more experience")  

## LLM Response Validator
# 
response = "My card is blocked"
token_count = 10
is_safe= True    

if token_count==5 and is_safe== True:
      print("response =" + "Good to use")
elif token_count== 4 or is_safe==False:
    print("response =" + "Not safe to use")
else:
    print("resonse = " + "Nothing is perfect")

if token_count > 5 and is_safe:
    print("Valid response - use it")
elif not is_safe:
    print("Response flagged as unsafe")
else:
    print("Response too short - retry")


# Task 4: User Age Validator
# age = int(input("Enter your age: "))

# if 18 <= age <= 100:
#     print(f"Welcome! You are {age} years old and eligible to proceed")
# elif age < 18:
#     print(f"Sorry, you must be 18 or older. You are {age}")
# elif age > 100:
#     print("Please enter a valid age")
# else:
#     print("Invalid age entered")

age_input = "25"

age_count = int(age_input)

print(age_count + 5)


# age = int(input("Enter you age : "))



########################################
# Lesson 3 - Complete Exercise
# Ram - AI Developer Journey
########################################

# ---- Task 1: Grade Classifier ----
print("--- Task 1: Grade Classifier ---")
test_score = 85

if test_score >= 90:
    print(f"Score: {test_score} - Excellent!")
elif test_score >= 75:
    print(f"Score: {test_score} - Good!")
elif test_score >= 50:
    print(f"Score: {test_score} - Pass")
else:
    print(f"Score: {test_score} - Failed")


# ---- Task 2: Experience Checker ----
print("\n--- Task 2: Experience Checker ---")
years_experience = 10
knows_python = True

if years_experience >= 5 and knows_python:
    print("Ready for AI development!")
elif not knows_python:
    print("Learn Python first")
else:
    print("Get more experience")


# ---- Task 3: LLM Response Validator ----
print("\n--- Task 3: LLM Response Validator ---")
response = "Python is a programming language"
token_count = 8
is_safe = True

if token_count > 5 and is_safe:
    print(f"Valid response: '{response}'")
elif not is_safe:
    print("Response flagged as unsafe - rejected")
else:
    print("Response too short - retry")


# ---- Task 4: User Age Validator ----
print("\n--- Task 4: Age Validator ---")
age = int(input("Enter your age: "))

if 18 <= age <= 100:
    print(f"Welcome! Age {age} - eligible to proceed")
elif age < 18:
    print(f"Must be 18 or older. You are {age}")
else:
    print("Please enter a valid age between 18 and 100")