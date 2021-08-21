import turtle

#Creamos la ventana para el juego
window = turtle.Screen()
#Ponemos el título
window.title("Pong, The game")
#Ponemos el color
window.bgcolor("black")
#Las dimensiones
window.setup(width=8000 , height=600)
window.tracer(0)

#Jugador uno
J1 = turtle.Turtle()
J1.speed(0)
J1.shape("square")
J1.color("white")
#J1.penup()
J1.goto(-350,0)

while True:
    window.update()