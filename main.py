from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

print("Welcome to the Quiz Game!")
print("Answer the following questions and get ready to test your General Knowledge!")
question_bank = []
for question in question_data:
    new_question_text = question["question"]
    new_answer_text = question["correct_answer"]
    new_question = Question(new_question_text, new_answer_text)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
i = 0
for i in range (10) :
    quiz.next_question()
    i = i + 1
print("Thank you for playing!")
print("You have completed the quiz")
print(f" Your final score is {quiz.score}/{quiz.question_number}")
