#program that generates random quiz questions and answers


import random

def generate_quiz():
    """Generate a random multiple choice quiz"""
    questions = []
    answers = []

    # Sample question 1
    question = "What is the capital of France?"
    choices = ["Paris", "London", "Berlin", "Rome"]
    correct_answer = "Paris"
    questions.append(question)
    answers.append(choices)
    answers.append(correct_answer)

    # Sample question 2
    question = "What is the largest planet in our solar system?"
    choices = ["Jupiter", "Saturn", "Uranus", "Neptune"]
    correct_answer = "Jupiter"
    questions.append(question)
    answers.append(choices)
    answers.append(correct_answer)
    
    # More questions can be added here

    return questions, answers

quiz = generate_quiz()
print("Quiz Questions: ")
for q in quiz[0]:
    print(q)
print("Answers: ")
print(quiz[1])
