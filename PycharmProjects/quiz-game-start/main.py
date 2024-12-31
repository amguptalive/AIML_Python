from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

# print(question_bank[0].text)
# print(question_bank)
final_score=0
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")