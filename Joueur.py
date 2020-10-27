import pygame
from ElementGraphique import *

class Perso(ElementGraphique):
	def __init__(self, img, fenetre, x=0, y=0, effect=None):
		super(Perso, self).__init__(img, fenetre, x, y)
		self.vitesse = 10
		self.vie = 4
		self.boost = 0

	def deplacer(self, touches):

		l, h = self.fenetre.get_size()

		if touches[pygame.K_q] and self.rect.x > 0:
			if self.boost:
				self.rect.x -= self.vitesse * 2
			else:
				self.rect.x -= self.vitesse
# ------------------------------ Or
		if touches[pygame.K_LEFT] and self.rect.x > 0:
			if self.boost:
				self.rect.x -= self.vitesse * 2
			else:
				self.rect.x -= self.vitesse

		if touches[pygame.K_d] and self.rect.x < l - self.rect.w:
			if self.boost:
				self.rect.x += self.vitesse * 2
			else:
				self.rect.x += self.vitesse
# ------------------------------ Or
		if touches[pygame.K_RIGHT] and self.rect.x < l - self.rect.w:
			if self.boost:
				self.rect.x += self.vitesse * 2
			else:
				self.rect.x += self.vitesse

		if self.boost:
			self.boost -= 1

	def Centre(self, monstre, fenetre):
		if self.collide(monstre):
			self.rect.x = 300 - self.rect.w
			self.rect.y = 900
			self.vie -= 1
			self.boost = 0

	def Boost(self, bonus):
		if self.collide(bonus):
			self.boost += 300

	def UpLife(self, uplife):
		if self.collide(uplife):
			self.vie += 1

	def Envie(self):
		if self.vie > 0:
			return True
		else:
			return False
