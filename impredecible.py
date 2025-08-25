import turtle
import random

pantalla = turtle.Screen()
pantalla.bgcolor("pink")
pantalla.title("Tortuga impredecible")

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.pensize(10)

def color_aleatorio():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

pantalla.colormode(255)

while True:
    color = color_aleatorio()
    tortuga.color(color)
    distancia = random.randint(20, 100)
    angulo = random.randint(0, 360)
    tortuga.forward(distancia)
    tortuga.left(angulo)





turtle.done