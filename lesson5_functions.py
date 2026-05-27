##  Function :
# a Function is a re-usable block of code and we can create once and call it many places

#Basic Function:
def greet():
    print("Good Morning")

greet()
   
def name():
    print(f"My name is Ram")

name()    

#Function with Parameters:

def add(a,b):
    print(a+b)
add(1,2)    


# Return Values:
def addtwonumber(x,y):
    return x+y

result = addtwonumber(4,2)
print(result)

## Default Parameters:

def call_ai_model(prompt, model="gpt-4", temperature=0.7):
    print(f"Prompt: {prompt}")
    print(f"Model: {model}")
    print(f"Temperature: {temperature}")

call_ai_model("what is python", 0.4)  
call_ai_model("LLM")  

## Functions calling Functions (AI Pipeline)
## Tasks to complete now:

def welcome_message():
    print("Ram")
    print("Todays goal is to learn Functions")
    print("todays date is 27th May")

welcome_message()

## Task 2: Create introduce_learner(name, role, goal) - prints formatted introduction. Call with your details and made-up details.

def introduce_learner(name, role, goal):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Goal: {goal}")

introduce_learner("ram" ,"qa","AI") 

print("------------------------")

introduce_learner("John" ,"ML ENGINNER","Algorithms") 

## Task 3: Create calculate_learning_days(hours_per_day) - calculates days to finish 60 hours. Call with 1, 2, and 4 hours.

def calculate_learning_days(hours_per_day):
    print(f" I work {hours_per_day} hours per day ")

calculate_learning_days(9)    
 



