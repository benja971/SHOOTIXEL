from random import *
from ElementGraphique import ElementGraphique

class Monstre(ElementGraphique):
	def __init__(self, img, fenetre, x, y):
		super(Monstre, self).__init__(img, fenetre, x, y)
		self.vx = choice([-10, 10])
		self.vy = choice([-10, 10])
