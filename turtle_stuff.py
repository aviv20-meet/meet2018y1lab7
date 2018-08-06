import turtle
turtle.goto(0,0)

UP = 0
direction = None

def up():
    global direction
    print("You pressed the up key.")
    
turtle.onkey(up, "Up") 
turtle.listen()

def on_move():
    #to do
