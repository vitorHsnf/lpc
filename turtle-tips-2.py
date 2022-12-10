import turtle
from time import sleep

s = turtle.getscreen()
t = turtle.Turtle()

# Usando Loops e Condicionais

# fazer o quadrado 
'''for i in range(4):
    t.fd(100)
    t.rt(90)
    print(i)'''

# circulos e mais circulos
'''n = 10
while n <= 100:
    t.circle(n)
    n += 10'''

# condições 
u = str(input("Desenhar um círculo? [S/N]"))
if u == 'S':
    r = int(input("Tamanho do círculo (raio): "))
    t.circle(r)
elif u == 'N':
    print("Tudo bem")
else:
    print("Sai daqui")