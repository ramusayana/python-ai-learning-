########################################
# Lesson 4 - Loops
# Ram - AI Developer Journey
########################################

# ---- Basic For Loop ----
print("--- Basic For Loop ---")
fruits = ["apple", "banana", "Guava"]

for fruit in fruits:
    print(fruit)


# ---- Range Loops ----
print("\n--- Range Loops ---")
# range(5) produces: 0, 1, 2, 3, 4
for number in range(5):
    print(number)

# range(1, 6) produces: 1, 2, 3, 4, 5
for number in range(1, 6):
    print(number)


# ---- String Loop ----
print("\n--- String Loop ---")
name = "Ram"
for assignee in name:
    print(assignee)


# ---- Dictionary Loop ----
print("\n--- Dictionary Loop ---")
employee = {
    "name": "Ramu",
    "age": 35,
    "role": "QA Lead"
}

for key, value in employee.items():
    print(f"{key}: {value}")


# ---- While Loop ----
print("\n--- While Loop ---")
count = 0
while count < 4:
    print(f"Count is: {count}")
    count += 1

# Your creative Car_bill example!
Car_bill = 0
while Car_bill < 11:
    print(f"The bill is: £{Car_bill}")
    Car_bill += 1


# ---- Break and Continue ----
print("\n--- Break ---")
for number in range(10):
    if number == 5:
        break
    print(number)

print("\n--- Continue ---")
for number in range(10):
    if number == 6:
        continue
    print(number)


# ---- Enumerate ----
print("\n--- Enumerate ---")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# ---- AI Scenarios ----
print("\n--- AI Scenario 1: Multiple Prompts ---")
prompts = ["What is AI", "What is LLM", "What is RAG"]
for i, prompt in enumerate(prompts):
    print(f"Prompt {i+1}: {prompt}")

print("\n--- AI Scenario 2: API Retry ---")
max_retries = 3
attempt = 0
while attempt < max_retries:
    print(f"Calling AI API... attempt {attempt+1}")
    attempt += 1
print("Max retries reached - stopping")

print("\n--- AI Scenario 3: Response Validator ---")
responses = ["Good answer", "", "Another good answer", "", "Final answer"]
for response in responses:
    if len(response) == 0:
        print("Empty response - skipping")
        continue
    print(f"Valid response: {response}")


# ---- TASK 1: AI Topics with enumerate ----
print("\n--- Task 1: AI Topics ---")
ai_topics = ["LLM", "RAG", "Bedrock", "AI Agents", "Python"]
for i, topic in enumerate(ai_topics):
    print(f"{i+1}: {topic}")


# ---- TASK 2: 5 times table ----
print("\n--- Task 2: 5 Times Table ---")
for number in range(1, 11):
    print(f"5 x {number} = {5 * number}")


# ---- TASK 3: While loop retry ----
print("\n--- Task 3: API Retry ---")
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    print(f"Attempt {attempts+1}: Calling AI API...")
    attempts += 1
print("Max retries reached - stopping")


# ---- TASK 4: Break and Continue ----
print("\n--- Task 4: Odd numbers up to 15 ---")
for number in range(1, 21):
    if number % 2 == 0:
        continue           # skip even numbers
    if number > 15:
        print(f"{number} - stopping here!")
        break
    print(number)


# ---- TASK 5: LLM Response Validator ----
print("\n--- Task 5: LLM Response Validator ---")
llm_responses = [
    "Python is a programming language",
    "",
    "LLMs are large language models",
    "",
    "LangChain is an AI framework",
    "UNSAFE_CONTENT",
    "RAG stands for Retrieval Augmented Generation"
]

valid_count = 0

for response in llm_responses:
    if len(response) == 0:
        print("Empty response - skipping")
        continue
    elif "UNSAFE" in response:
        print("Unsafe response - rejected")
        continue
    else:
        print(f"Valid: {response}")
        valid_count += 1

print(f"\nTotal valid responses: {valid_count}")