### Basic Loop

fruits = ["apple","banana","Guava"]

for fruit in fruits:
    print(fruit)


## Loop through a range of numbers

range(5)== 0,1,2,3,4

for number in range(5):
    print(number)
range(1,6)== 1,2,3,4,5

for number in range(1,6):
    print(number)

###loop through a sting

name= "Ram"

for assignee in name:
    print(assignee)

## loop through the dictionary
#

employee = { 
    "name":"Ramu",
    "age":35,
    "Role":"QA Lead"
}   

#print(employee)
 
for key,value in employee.items():
    print(f"{key}={value}") 

### while loop it will be running as long as condition is true and stops when the condition becomes false

# Basic loop

count = 0

while count<4:
    print(f"Count is : {count}")
    count += 1

Car_bill = 0

while Car_bill<11:
    print(f"The bill is {Car_bill}")
    Car_bill += 1


# break - stop the loop completely
for number in range(10):
    if(number==5):
        break
    print(number)   

# continue - skip current item and continue
for number in range(10):
    if(number==6):
        continue
    print(number)     

fruits = ["apple","banana","Guava"]

# enumerate - get index AND value together
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")


###  AI Related scenarios

prompts = [ "what is AI", "what is LLM", "what is RAG"]

for i, prompt in enumerate(prompts):
    print(f"prompts {i+1}: {prompt}")


# Real AI scenario 2: Retry failed API calls

max_retries = 3 
attempt = 0

while attempt<max_retries:
    print(f"calling an AI API { attempt+1}")
    attempt += 1

   # If API succeeds, break
    # If fails, keep retrying

# Real AI scenario 3: Validate a list of responses
responses = ["Good answer", "", "Another good answer", "", "Final answer"]

for response in responses:
    if len(response) == 0:
        print("Empty response - skipping")
        continue
    print(f"Valid response: {response}")    

## Test

ai_topics = [ "llm", "RAG", "Bedrock","AI Agents", "Python"]

for list in ai_topics:
    print(f"{list}")

for i, topics in enumerate(ai_topics):
    print(f"{i+1}: {topics}")  

### Range loop (1,11)


## Task 3: While loop with retry

attempts = 0
max_attempts = 3

while attempts<max_attempts:
    print(f"Attempt 1: Calling AI API {attempts+1}")
    attempts += 1

#Task 4: Loop with break and continue 

numbers = 1,20