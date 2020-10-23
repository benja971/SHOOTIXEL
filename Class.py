import pygame
from random import randint


class ElementGraphique:
	def __init__(self, img, x, y):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def Afficher(self, window):
		window.blit(self.image, self.rect)


class Perso(ElementGraphique):
	def __init__(self, img, x, y, largeur, hauteur):
		super(Perso, self).__init__(img, x, y)
		self.rect.x = largeur // 2 - self.rect.w // 2
		self.rect.y = hauteur - self.rect.h
		self.vie = 100
		self.vitesse = 10

	def Deplacer(self, touches, largeur):
		if touches[pygame.K_d] and self.rect.x <= largeur - self.rect.w:
			self.rect.x += self.vitesse
		if touches[pygame.K_a] and self.rect.x >= 0:
			self.rect.x -= self.vitesse

	def Collisions(self, balle, balles):
		if balle.rect.colliderect(self.rect):
			self.vie -= balle.degats
			balle.alive = False

	def Tir(self, tirs, img, i, touches):
		# if i % 7 == 0:
		if touches[pygame.K_SPACE]:
			tirs.append(Balle(img, self.rect.x + self.rect.w // 2,self.rect.y - self.rect.h // 2, 1, 5, 15, "tir"))

	def Alive(self):
		if self.vie <= 0:
			print("Perdu")

class Balle(ElementGraphique):
	def __init__(self, img, x, y, pv, v, d, _type):
		super(Balle, self).__init__(img, x, y)
		self.type = _type
		self.vie = pv
		self.vitesse = v
		self.degats = d
		self.alive = True

	def Move(self):
		self.rect.y += self.vitesse

	def MoveTirs(self):
		self.rect.y -= self.vitesse

	def Collisions(self, projectil, enemys):
		if projectil.type == "enemy":
			if projectil.rect.colliderect(self.rect):
				projectil.vie -= self.degats	
				self.alive = False
			if projectil.vie <= 0:
				projectil.alive = False
				if not projectil.alive and projectil in enemys:
					enemys.remove(projectil)