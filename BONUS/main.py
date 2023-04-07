import json

with open("data.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, value in enumerate(question["options"]):
        print(f"{index + 1}. {value}")
    user_choice = int(input("Enter your data"))
    question["user_choice"] = user_choice




