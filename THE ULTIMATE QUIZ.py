import pgzrun
HEIGHT = 600
WIDTH = 800
TITLE = "the ultimate quiz!!!!"
messegebox = Rect(0,0,800,100)
questionbox = Rect(20,100,600,150)
answer1 = Rect(20,270,280,100)
answer2 = Rect(340,270,280,100)
answer3 = Rect(20,390,280,100)
answer4 = Rect(340,390,280,100)
skip = Rect(650,270,120,220)
timebox = Rect(650,100,120,120)
questions = []
question = []
total = 7
question_number = 0
questions_correct = 0
def draw():
    screen.fill("black")
    screen.draw.filled_rect(messegebox,"black")
    screen.draw.filled_rect(questionbox,"dark blue")
    screen.draw.filled_rect(answer1,"orange")
    screen.draw.filled_rect(answer2,"orange")
    screen.draw.filled_rect(answer3,"orange")
    screen.draw.filled_rect(answer4,"orange")
    screen.draw.filled_rect(skip,"dark green")
    screen.draw.filled_rect(timebox,"dark blue")
    screen.draw.textbox("welcome to the game!",messegebox,color = "white")
    screen.draw.textbox(question[0],questionbox,color = "white")
    screen.draw.textbox(question[1],answer1,color = "white")
    screen.draw.textbox(question[2],answer2,color = "white")
    screen.draw.textbox(question[3],answer3,color = "white")
    screen.draw.textbox(question[4],answer4,color = "white")
    screen.draw.textbox("skip",skip,color = "white")
    screen.draw.textbox("20",timebox,color = "white")
def read_question_file(): 
    global questions,total
    file = open("questions.txt ","r")
    questions = file.readlines()
    total = len(questions)
    file.close()
def read_question():
    global question
    question = questions[question_number].split(",")
read_question_file()
read_question()  


def update():
    pass







pgzrun.go()
    
