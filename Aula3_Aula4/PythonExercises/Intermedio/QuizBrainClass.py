import random

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
        
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)
        
    def still_has_questions(self):
        return self.question_number == len(self.questions_list)
        
    def check_answer(self, user_answer, current_answer):
        if current_answer.lower() == user_answer.lower():
            self.score += 1
            print(f'Respuesta correcta. Su puntaje es: {self.score}/{self.question_number} \n')
        else:
            print(f'Respuesta incorrecta. Su puntaje es: {self.score}/{self.question_number} \n')