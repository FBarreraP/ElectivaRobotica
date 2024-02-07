from QuizQuestionModelClass import Question
from QuizData import question_data
from QuizBrainClass import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

quiz = QuizBrain(question_bank)
while not quiz.still_has_questions():
    quiz.next_question()

print('Ha finalizado el quiz')
print(f"Su puntación final fue {quiz.score}/{quiz.question_number}")