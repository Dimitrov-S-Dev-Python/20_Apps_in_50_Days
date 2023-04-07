import json

with open("data.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, value in enumerate(question["options"]):
        print(f"{index + 1}. {value}")
    user_choice = int(input("Enter your number guess: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score += 1

for index, question in enumerate(data):
    message = f"{index + 1}.Your answer: {question['user_choice']},\"" \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(f"{score}/{len(data)}")

