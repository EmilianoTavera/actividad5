from random import *
from turtle import *
from freegames import path
import string

car = path('car.gif')
letters = list(string.ascii_letters[:32]) * 2
state = {'mark': None}
hide = [True] * 64
countTap = 0
writer = Turtle(visible=False)
contador = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global countTap
    global contador
    spot = index(x, y)
    mark = state['mark']
    countTap += 1
    writer.undo()
    writer.goto(0, 197)
    writer.write(countTap)
    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        contador += 1
        if contador == 32:
            print("¡Felicidades, has ganado!")

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if letters[mark] in string.ascii_lowercase:
            goto(x + 12, y)
        else:
            goto(x + 2, y)
        color('black')
        write(letters[mark], font=('Arial', 30, 'normal'), align="left")

    update()
    ontimer(draw, 100)

shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
