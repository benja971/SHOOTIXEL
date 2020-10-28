from random import *
from ElementGraphique import ElementGraphique

class Bonus(ElementGraphique):
    def __init__(self, img, fenetre, x, y, _type, i):
        super(Bonus, self).__init__(img, fenetre, x, y)
        self.vx = choice([-10, 10])
        self.vy = choice([-10, 10])
        self.type = _type
        self.creationtime = i

    def deplacer(self, largeur, hauteur):

        self.rect.x += self.vx
        if self.rect.x > largeur - self.rect.w:
            self.vx = -abs(self.vx)
        if self.rect.x < 0:
            self.vx = abs(self.vx)

        self.rect.y += self.vy
        if self.rect.y > hauteur - self.rect.h:
            self.vy = -abs(self.vy)
        if self.rect.y < 0:
            self.vy = abs(self.vy)

    def alive(self, i, Bonus_l):
        if i - self.creationtime >= 150:
            if self in Bonus_l:
                Bonus_l.remove(self)
