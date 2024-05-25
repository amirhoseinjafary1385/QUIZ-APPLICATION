
# import random 

# questions = [
#       {
#         "question": "What is the capital of France?",
#         "options": ["Paris", "London", "Berlin", "Madrid"],
#         "answer": "Paris"
#     },
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["Mars", "Venus", "Jupiter", "Saturn"],
#         "answer": "Mars"
#     },
#     # Add more questions here...
# ] 

# def generate_quiz():

#     random.shuffle(questions)
#     return questions [:5] #Return a list of 5 random questions

# def check_answers(answers):
#     correct_answers = 0
#     for i, answer in enumerate(answers):
#         if answer == questions[i]["answer"]:
#             correct_answers += 1
#     return correct_answers

# if __name__ == "__main__":
#     quiz = generate_quiz()
#     print("Welcome to the Quiz!")
#     answers = []
#     for question in quiz:
#         print(question["question"])
#         for i, option in enumerate(question["options"]):
#             print(f"{i + 1}. {option}")
#         user_answer = input("Enter your answer (1-4): ")
#         answers.append(question["options"][int(user_answer) - 1])

#     score = check_answers(answers)
#     print(f"You GOT {score} out of {len(quiz)}questions Carrect!!" )







import random 

questions = [
      {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    # Add more questions here...
] 

def generate_quiz():

    random.shuffle(questions)
    return questions [:5] #Return a list of 5 random questions

def check_answers(answers):
    correct_answers = 0
    for i, answer in enumerate(answers):
        if answer == questions[i]["answer"]:
            correct_answers += 1
    return correct_answers
    
if __name__ == "__main__":
    quiz = generate_quiz()
    print("Welcome to the Quiz!")
    answers = []
    for question in quiz:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        answers.append(question["options"][int(user_answer) - 1])

    score = check_answers(answers)
    print(f"You GOT {score} out of {len(quiz)}questions Carrect!!" )

