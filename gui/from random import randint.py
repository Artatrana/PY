from random import randint
class RandomBall:
    def __init__(self, canvas, scrnwidth, scrnheight):
        self.canvas = canvas
        self.xpos = randint(10, int(scrnwidth))
        self.ypos = randint(10, int(scrnheight))
        self.xvelocity = randint(6,12)
        self.yvelocity = randint(6,12)
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        self.radius = randint(40,70)
        r = lambda: randint(0,255)
        self.color = '#%02x%02x%02x' % (r(),r(),r())