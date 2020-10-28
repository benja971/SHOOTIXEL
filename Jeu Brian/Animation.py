from math import cos
from ElementGraphique import ElementGraphique

class ElementGraphiqueAnimee(ElementGraphique):
	def __init__(self, img, fenetre, x, y):
		super(ElementGraphiqueAnimee, self).__init__(img, fenetre, x, y)
		self.fps = 0
		self.numimage = 0
		self.deltaX = 10
		self.deltaY = 10
		self.rect = self.image[self.numimage].get_rect()
		self.alive = True
		self.effect = None

	def afficher(self, fenetre):
		self.fps += 0.5
		if (self.fps % 0.5) == 0:
			self.numimage = (self.numimage + 1) % len(self.image)
			fenetre.blit(self.image[self.numimage], self.rect)

# --------

class MonstreAnimee(ElementGraphiqueAnimee):
	def __init__(self, img, fenetre, x, y):
			super(MonstreAnimee, self).__init__(img, fenetre, x, y)
			self.t = 0

	def deplacer(self):
		self.t += 1
		self.rect.x = 50*cos(self.t/10) + 250
		self.rect.y = 2*self.t

# --------
