import turtle
from time import sleep

# a tela e a tartaruga
s = turtle.getscreen()
t = turtle.Turtle()

# Mudando a cor da tela
#turtle.bgcolor("cyan")

# Mudar o nome da tela
turtle.title("My Turtle Program")

# Mudar o tamanho da bicha
t.shapesize(2, 2, 2)
# Parâmetros: comprimento da área, largura da área, largura do cortorno

# a cor da bicha e da caneta
# t.fillcolor("red")
# t.pencolor("pink")
# t.color("red", "red")

# formato da bicha
# t.shape('turtle')

# tamanho da tinta
t.pensize(5)

# direções que a tartaruga se mexe: direita(rt), frente(fd), esquerda(lt), trás(bk)
'''t.rt(90)
t.fd(100)
t.lt(90)
t.bk(100)'''

# direção específica
# t.goto(100,100)

# posição inicial (0,0)
# t.home()

# Desenhar formas 
# Quadrado
'''t.forward(100)
sleep(1)
t.right(90)
sleep(1)
t.forward(100)
sleep(1)
t.right(90)
sleep(1)
t.forward(100)
sleep(1)
t.right(90)
sleep(1)
t.forward(100)
sleep(1)'''

# Losango
'''t.right(45)
sleep(1)
t.forward(100)
sleep(1)
t.right(90)
sleep(1)
t.forward(100)
sleep(1)
t.right(90)
sleep(1)
t.forward(100)
sleep(1)
t.right(90)
sleep(1)
t.forward(100)
sleep(1)'''

# Circulo
'''t.pensize(10)
t.circle(90)'''

# Ponto
#t.dot(200)
#sleep(1)

# Preenchendo a imagem
'''t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
sleep(1)
t.end_fill()
sleep(1)'''

# Velocidade da caneta
'''t.speed(1)
t.forward(100)
sleep(1)
t.speed(2)
t.forward(100)
sleep(1)'''

# Customizando em uma linha
# Pen color: purple
# Fill color: orange
# Pen size: 10
# Pen speed: 9
'''t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()'''

# Tirando a caneta + undo()

'''t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.undo()
t.pendown()
sleep(1)
t.clear()'''

# Botando as marcas da bicha na tela
'''t.stamp()
t.fd(100)
t.stamp()
t.fd(100)
sleep(1)
t.clearstamp(8)
sleep(1)
t.clearstamp(9)
sleep(1)
t.clearstamp()
sleep(1)'''

# Clonar a bicha
c = t.clone()

t.color("magenta")
c.color("red")

t.begin_fill()
t.circle(100)
t.end_fill()

c.begin_fill()
c.circle(60)
c.end_fill()
