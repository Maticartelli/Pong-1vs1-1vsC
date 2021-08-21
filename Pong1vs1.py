import turtle



#Creamos la ventana para el juego
window = turtle.Screen()
#Ponemos el título
window.title("Pong, The game")
#Ponemos el color
window.bgcolor("black")
#Las dimensiones
window.setup(width=800 , height=600)
window.tracer(0)


#Jugador uno
J1 = turtle.Turtle()
J1.speed(0)
J1.shape("square")
J1.color("violet")
J1.penup()
J1.goto(-350,0)
J1.shapesize(stretch_wid=8,stretch_len=1)

#Jugador dos
J2 = turtle.Turtle()
J2.speed(0)
J2.shape("square")
J2.color("violet")
J2.penup()
J2.goto(350,0)
J2.shapesize(stretch_wid=8,stretch_len=1)


#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.3
pelota.dy = 0.3

#División
division = turtle.Turtle()
division.color("red")
division.goto(0,400)
division.goto(0,-400)

#Marcador de puntos
Marc = turtle.Turtle()
Marc.speed(0)
Marc.color("blue")
Marc.penup()
Marc.hideturtle()
Marc.goto(0,260)
Marc.write("Jugador 1: 0        Jugador 2: 0", align="center", font=("Courier",24,"normal"))

#La variable de puntos para cada jugador
Marc1 = 0
Marc2 = 0

#Movimientos
def J1_up():
    y = J1.ycor()
    y +=20
    if y > 220:
        y = 220
    J1.sety(y)
def J1_down():
    y = J1.ycor()
    y -=20
    if y < -220:
        y = -220
    J1.sety(y)
    
def J2_up():
    y = J2.ycor()
    y +=20
    if y > 220:
        y = 220
    J2.sety(y)
def J2_down():
    y = J2.ycor()
    y -=20
    if y < -220:
        y = -220
    J2.sety(y)
    
#Teclado y movimientos
window.listen()
window.onkeypress(J1_up, "w")
window.onkeypress(J1_down, "s")
window.onkeypress(J2_up, "Up")
window.onkeypress(J2_down, "Down")

#Funcionamiento del juego
while True:
    window.update()
    
    #Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    #Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
        
    if pelota.ycor() < -290:
        pelota.dy *= -1
    
    #Creamos la condición de gol y la ganancia de puntos
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        Marc1 +=1
        Marc.clear()
        Marc.write("Jugador 1: {}        Jugador 2: {}".format(Marc1,Marc2), align="center", font=("Courier",24,"normal"))
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        Marc2 += 1
        Marc.clear()
        Marc.write("Jugador 1: {}        Jugador 2: {}".format(Marc1,Marc2), align="center", font=("Courier",24,"normal"))
        
    #Creamos la colisión de la pelota con los jugadores
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < J2.ycor() + 80 
                 and pelota.ycor() > J2.ycor()-80)):
        pelota.dx *=-1
    
    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < J1.ycor() + 80 
                 and pelota.ycor() > J1.ycor()-80)):
        pelota.dx *=-1
    
