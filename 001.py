import turtle

#sets up screen
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #turns on turtle tracer

#Paddle A
paddle_a = turtle.Turtle() #creates paddle as an object
paddle_a.speed(0) #sets speed to max for animation
paddle_a.shape('square') #sets shape of paddle
paddle_a.color('white') #creates paddle color to white
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #paddle is 20px by 20px so width will be 5x that number
paddle_a.penup() #lifts the turtle pen up so it does not draw on the screen
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape('square') 
paddle_b.color('white') 
paddle_b.shapesize(stretch_wid=5,stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape('square') 
ball.color('white') 
ball.penup() 
ball.goto(0, 0)

#Setup Ball Movement
ball.dx = 2 #dx = delta x or x movement of ball
ball.dy = 2

#Function
def paddle_a_up(): #creates a function
    y = paddle_a.ycor() #assigns a y cord to the paddle named y
    y += 20 #adds 20(a pixel) to the y value and sets y equal to that new y value
    paddle_a.sety(y) #sets the new y value to paddle_a
def paddle_a_down(): 
    y = paddle_a.ycor() 
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up(): 
    y = paddle_b.ycor() 
    y += 20 
    paddle_b.sety(y)
def paddle_b_down(): 
    y = paddle_b.ycor() 
    y -= 20 
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #tells computer to listen to keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #set x cord of ball to whatever current x cord is plus change in dx (2)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290) #600 is total height so 300 is split but ball is 20px
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #-1 reverses direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1