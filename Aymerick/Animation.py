import math
from ElementGraphique import ElementGraphique

class ElementGraphiqueAnimee(ElementGraphique):
	def __init__(self, img=[], x=0, y=0, effect=None):
		self.image = img
		self.fps = 0
		self.numimage = 0
		self.deltaX = 10
		self.deltaY = 10
		self.rect = self.image[self.numimage].get_rect()
		self.rect.x = x
		self.rect.y = y
		self.alive = True
		self.effect = effect

	def afficher(self, fenetre):
		self.fps += 0.5
		if (self.fps % 0.5) == 0:
			self.numimage = (self.numimage + 1) % len(self.image)
			fenetre.blit(self.image[self.numimage], self.rect)

# --------

class MonstreAnimee(ElementGraphiqueAnimee):
	def __init__(self, img, x=0, y=0):
			ElementGraphiqueAnimee.__init__(self, img)
			self.t = 0.0
			self.truc = 10
			self.centerx = x
			self.centery = y

	def deplacer(self):
		self.t += 1.0

		self.rect.x = 50*math.cos(self.t/10) + 250
		self.rect.y = 2*self.t