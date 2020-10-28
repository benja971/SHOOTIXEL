import pygame
from ElementGraphique import *

class Perso(ElementGraphique):
	def __init__(self, img, fenetre, x, y, v, pv):
		super(Perso, self).__init__(img, fenetre, x, y)
		self.vitesse = v
		self.vie = pv
		self.boost = 0
		self.effect = None

	def deplacer(self, touches, largeur):
		if touches[pygame.K_d] and self.rect.x <= largeur - self.rect.w:
			if self.Boost:
				self.rect.x += 2*self.vitesse
			else:
				self.rect.x -= self.vitesse

		if touches[pygame.K_a] and self.rect.x >= 0:
			if self.Boost:
				self.rect.x -= 2*self.vitesse
			else:
				self.rect.x -= self.vitesse

		if touches[pygame.K_LEFT] and self.rect.x <= largeur - self.rect.w:
			if self.Boost:
				self.rect.x += 2*self.vitesse
			else:
				self.rect.x -= self.vitesse

		if touches[pygame.K_RIGHT] and self.rect.x >= 0:
			if self.Boost:
				self.rect.x -= 2*self.vitesse
			else:
				self.rect.x -= self.vitesse

		if self.boost:
			self.boost -= 1

	def Centre(self, largeur):
			self.rect.x = largeur//2 - self.rect.w//2
			self.rect.y = 900

	def Bonus(self, bonus):
		if self.colliderect(bonus):
			if self.type == 'speed':
				self.boost += 300
			if self.type == 'uplife':
				self.vie += 1

	def Envie(self):
		if self.vie > 0:
			return True
		else:
			return False
