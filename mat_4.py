import turtle
t = turtle.Turtle()
t.speed(0)
turtle.setup(1200, 800)

class Flower:


    def __init__(self, x0, y0, x1, y1, colorp, color1, color2, color3, color4):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colorp = colorp
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4

    def printflower(self):
        pass  #викликати рисування стебла, листка і квітки за цими параметрами

class Steam(Flower):

    def __init__(self, x0, y0, x1, y1, colorp):
        Flower.__init__(self, x0, y0, x1, y1, colorp)

    def stprint(self):
        t.up()
        t.goto(self.x0, self.y0)
        t.pensize(5)
        t.color(self.colorp)
        t.down()
        t.goto(self.x1, self.y1)


class Petals(Flower):

    def __init__(self, x1, y1, color1, color2, color3, color4):
        Flower.__init__(self, x1, y1, color1, color2, color3, color4)

    def petprint(self):
        t.up()
        t.setpos(self.x1, self.y1)
        t.down()
        t.color(self.color1)
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.up()
        t.setpos(self.x1, self.y1 + 30)
        t.down()
        t.color(self.color2)
        t.begin_fill()
        t.circle(70)
        t.end_fill()
        t.up()
        t.setpos(self.x1, self.y1 + 55)
        t.down()
        t.color(self.color3)
        t.begin_fill()
        t.circle(45)
        t.end_fill()
        t.up()
        t.setpos(self.x1, self.y1 + 80)
        t.down()
        t.color(self.color4)
        t.begin_fill()
        t.circle(20)
        t.end_fill()


class Leaf(Steam):

    def __init__(self, x1, y1, color1, color2, color3, color4):
        Steam.__init__(self, x1, y1, color1, color2, color3, color4)

    def leprint(self):
        t.up()
        t.goto(self.x1, self.y1)
        t.begin_fill()
        t.down()
        t.goto(self.x1, self.y1-10)
        t.circle(120, 60)
        t.lt(30)
        t.forward(10)
        t.lt(90)
        t.circle(120, 60)
        t.end_fill()
        t.rt(240)


if __name__ == '__main__':
    t.home()
    a = Flower.(425, 0, 100, 100, 'green', 'green', 'green', 'green', 'green')
    a.stprint()
    

turtle.done()