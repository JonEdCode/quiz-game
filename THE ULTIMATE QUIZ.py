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
listthing = [answer1,answer2,answer3,answer4]
questions = []
question = []
total = 7
question_number = 0
score = 0
gameEnd = False 
timeleft = 10
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
def on_mouse_down(pos):
    option = 1
    for answer in listthing:
        if answer.collidepoint(pos):
            if option == int(question[5]):
                corectanswer()
            else:
                gameover()
        option = option +1
    if skip.collidepoint(pos):
        read_question()
def corectanswer():
    global score,question_number,timeleft
    score = score +1 
    question_number = question_number + 1
    timeleft = 10
    if question_number == total:
        gameover()
    else:
        read_question()
def gameover():
    global gameEnd , question , timeleft
    gameEnd = True 
    question = ["game over","-","-","-","-","-"]
    timeleft = 0 





def update():
    pass







pgzrun.go()
    
