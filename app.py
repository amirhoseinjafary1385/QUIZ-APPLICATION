from flask import Flask, render_template, request

import random

app = Flask(__name__)



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
    return questions[:5]  # Return a list of 5 random questions

def check_answers(answers):
    correct_answers = 0
    for i, answer in enumerate(answers):
        if answer == questions[i]["answer"]:
            correct_answers += 1
    return correct_answers

@app.route('/')
def index():
    quiz = generate_quiz()
    return render_template('index.html', quiz = quiz)

@app.route('/submit', methods=['GET'])
def submit():
    answers = request.form.getlist('answer')
    score = check_answers(answers)
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)