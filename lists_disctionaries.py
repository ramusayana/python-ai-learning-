fruits = [ "apple","banana","cherry"]

print(f"I like eating : {fruits}")

fruits.append("Guava")

print(fruits)

fruits.remove("apple")

print(fruits)

print(fruits[2])

season_update = [ "fruits", 3.0, True,5]

print(season_update)

print(len(season_update))

###. loops

for fruit in fruits:
    print(fruit)
    

 ###   dictiionaries are in the form of key pair and values with a variable and "=" and { key pair : values}
 # 

person = {
    "name" : "Ram",
    "age" : 40,
    "experience" : 10.5,
    "real_time" : True
}   

print(person)

print(person["age"])

person["location"] = "Reading"

print(person)


for key,value in person.items():
    print(f" {key} : {value}")

## Test  for lesson 2 

learning_topics = [ "python","Boto3","AI","LLM","LANGCHAIN"]

print(learning_topics[0])
print(learning_topics[-1])
print(learning_topics[-5])

learning_topics.append("boto")

print(f"Topics are {learning_topics}")

## create a list and tech stack ( my_profile is dictionary)
my_profile = {

"name" : "Ram",
"Expereince":10,
"current_role":"QA_LEAD"
}

tech_stack = ["pyhton","llm","AI"]
my_profile["skills"]= tech_stack

print(f"My complete profile:")

for key,value in my_profile.items():
    print(f"{key},{value}")

### Real time in AI
# 
llm_response= { 
    "model" : "GPT-4",
    "Choice" : [
        {"text" : "HelloWorld" , "score": 0.95},
        {"text": "Hi there Ram", "Rating" :1}
],
    "usage": {"tokens": 150 }

}    


llm_response = {
    "model": "gpt-4",
    "choices": [
        {"text": "Hello world", "score": 0.95},
        {"text": "Hi there", "score": 0.89}
    ],
    "usage": {"tokens": 150}
}

print(llm_response)
print(llm_response["choices"])
#print(llm_response["Choice"])
print(llm_response["choices"][0]["text"])  # Output: Hello world


