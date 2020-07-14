import pgzrun
import random
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 600

#                    x  y  width height
question_box = Rect(20, 20, 600, 200)
timer_box = Rect(640, 20, 140, 200)
answer_box1 = Rect(20, 254, 370, 150)
answer_box2 = Rect(410, 254, 370, 150)
answer_box3 = Rect(20, 430, 370, 150)
answer_box4 = Rect(410, 430, 370, 150)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10  # number of seconds the player has to answer each question

class Question:
    def __init__(self, text, answers, correct_answer):
        self.text = text
        self.answers = answers
        self.shuffle_answers()
        self.correct_answer = correct_answer

    def shuffle_answers(self):
        random.shuffle(self.answers)

    def get_correct_answer_index(self):
        return self.answers.index(self.correct_answer)


q1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Tokyo"], "Paris")
q2 = Question("What is 5+7?", ["12", "10", "14", "8"], "12")
q3 = Question("What is the seventh month of the year?", ["April", "May", "June", "July"], "July")
q4 = Question("Which planet is closest to the Sun?", ["Saturn", "Neptune", "Mercury", "Venus"], "Mercury")
q5 = Question("Where are the pyramids?", ["India", "Egypt", "Morocco", "Canada"], "Egypt")


questions = [
    q1,
    q2,
    q3,
    q4,
    q5
]

# contacts = [
#     Contact("name", "343434"),
#     Contact("djfkj", "3434")
# ]
#
# def find(name):
#     for c in contacts:
#         if text == c.name:
#             return True
#     return False


random.shuffle(questions)
question = questions.pop()         # берем последний вопрос из списка для дальнейшей работы
time_left = 10                     # сколько осталось времени
score = 0

def draw():
    screen.fill("white")
    screen.draw.filled_rect(question_box, "#7F9BB3")  # рисуем прямоугольник
    screen.draw.filled_rect(timer_box, "#43AFA0")     # рисуем таймер
    screen.draw.textbox(str(time_left), timer_box)

    index = 0
    for box in answer_boxes:
        screen.draw.filled_rect(box, "#7F9BB3")
        screen.draw.textbox(question.answers[index], box)
        index += 1

    screen.draw.textbox(question.text, question_box)        # вставляем текст внутри прямоуг. области

def on_mouse_down(pos):
    answer_index = 0
    for box in answer_boxes:
        if box.collidepoint(pos):
            # выбрал ли пользователь правильный ответ?
            if question.get_correct_answer_index() == answer_index:
                get_next_question()
        answer_index += 1

def get_next_question():
    global question, time_left, score

    score += 1
    if questions:
        question = questions.pop()
        time_left = 10
    else:
        game_over()

def game_over():
    global question
    question = Question(f"Game over. You got {score} right questions", ["-", "-", "-", "-"], "-")

def update_time_left():
    global time_left, score

    if time_left > 0:
        time_left -= 1
    else:
        score -= 1
        get_next_question()

clock.schedule_interval(update_time_left, 1)

pgzrun.go()