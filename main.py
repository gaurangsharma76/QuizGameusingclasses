from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in range(len(question_data)):
    j = question_data[i]
    new_q = Question(j['text'], j['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz over!!! Your final score is: {quiz.score}/{len(question_bank)}")

