import json

with open("mcq_1.json", 'r') as file:
    content = file.read()

data = json.loads(content)
# print(data)

"""content is a string whereas data is a list"""

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternative"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("enter your answer: "))
    question["user_choice"] = user_choice


for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "correct answer"
    else:
        result = "wrong answer"

    message = f"{index+1} {result} -your answer:{question['user_choice']}, " \
              f"correct answer:{question['correct_answer']}"
    print(message)

# print(data)/
print(score, "/", len(data))
