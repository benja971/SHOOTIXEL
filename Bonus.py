from random import *
from ElementGraphique import ElementGraphique

class Bonus(ElementGraphique):
    def __init__(self, img, fenetre, x=0, y=0):
        super(Bonus, self).__init__(img, fenetre, x, y)

        self.vx = choice([-10, 10])
        self.vy = choice([-10, 10])

    def deplacer(self):

        l, h = self.fenetre.get_size()

        self.rect.x += self.vx
        if self.rect.x > l - self.rect.w:
            self.vx = -abs(self.vx)
        if self.rect.x < 0:
            self.vx = abs(self.vx)

        self.rect.y += self.vy
        if self.rect.y > h - self.rect.h:
            self.vy = -abs(self.vy)
        if self.rect.y < 0:
            self.vy = abs(self.vy)
