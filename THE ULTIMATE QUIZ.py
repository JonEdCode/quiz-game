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
    screen.draw.textbox("question",questionbox,color = "white")
    screen.draw.textbox("answer 1",answer1,color = "white")
    screen.draw.textbox("answer 2",answer2,color = "white")
    screen.draw.textbox("answer 3",answer3,color = "white")
    screen.draw.textbox("answer 4",answer4,color = "white")
    screen.draw.textbox("skip",skip,color = "white")
    screen.draw.textbox("20",timebox,color = "white")


def update():
    pass







pgzrun.go()
    
