import turtle
t = turtle.Turtle()
t.speed(0)
turtle.setup(1200, 800)

class Flower:

    class Petals:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def petprint(self):
            t.up()
            t.setpos(self.x, self.y)
            t.down()
            t.color('red')
            t.begin_fill()
            t.circle(100)
            t.end_fill()
            t.up()
            t.setpos(self.x, self.y + 30)
            t.down()
            t.color('blue')
            t.begin_fill()
            t.circle(70)
            t.end_fill()
            t.up()
            t.setpos(self.x, self.y + 55)
            t.down()
            t.color('yellow')
            t.begin_fill()
            t.circle(45)
            t.end_fill()
            t.up()
            t.setpos(self.x, self.y + 80)
            t.down()
            t.color('black')
            t.begin_fill()
            t.circle(20)
            t.end_fill()

    class Steam:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def stprint(self):
            t.up()
            t.goto(0, -300)
            t.pensize(5)
            t.color('green')
            t.down()
            t.goto(self.x, self.y)

    class Leaf:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def leprint(self):
            t.color('green')
            t.up()
            t.goto(self.x, self.y)
            t.begin_fill()
            t.down()
            t.goto(self.x, self.y-10)
            t.circle(120, 60)
            t.lt(30)
            t.forward(10)
            t.lt(90)
            t.circle(120, 60)
            t.end_fill()
            t.rt(240)











if __name__ == '__main__':
    t.home()
    a = Flower.Steam(425, 0)
    a.stprint()
    a = Flower.Petals(425, 0)
    a.petprint()
    a = Flower.Leaf(425, 0)
    a.leprint()
    b = Flower.Steam(0, 100)
    b.stprint()
    b = Flower.Petals(0, 100)
    b.petprint()
    a = Flower.Leaf(0, 100)
    a.leprint()
    c = Flower.Steam(-425, 0)
    c.stprint()
    c = Flower.Petals(-425, 0)
    c.petprint()
    a = Flower.Leaf(-425, 0)
    a.leprint()
    d = Flower.Steam(-175, -100)
    d.stprint()
    d = Flower.Petals(-175, -100)
    d.petprint()
    a = Flower.Leaf(-175, -100)
    a.leprint()
    e = Flower.Steam(175, -100)
    e.stprint()
    e = Flower.Petals(175, -100)
    e.petprint()
    a = Flower.Leaf(175, -100)
    a.leprint()

    turtle.done()