import pygame
from random import randint


class ElementGraphique:
	def __init__(self, x, y, img):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def Afficher(self, window):
		window.blit(self.image, self.rect)


class Perso(ElementGraphique):
	"""
	Personnage qu'incarne le joueur
	"""
	def __init__(self, img, x, y, largeur, hauteur):
		super(Perso, self).__init__(x, y, img)
		self.rect.x = largeur // 2 - self.rect.w // 2
		self.rect.y = hauteur - self.rect.h
		self.vie = 100
		self.vitesse = 10
		self.couldown = 20
		self.money = 0

	def Deplacer(self, touches, largeur):
		if touches[pygame.K_d] and self.rect.x <= largeur - self.rect.w:
			self.rect.x += self.vitesse
		if touches[pygame.K_a] and self.rect.x >= 0:
			self.rect.x -= self.vitesse

	def Collisions(self, enemy, enemys):
		if enemy.rect.colliderect(self.rect):
			self.vie -= enemy.degats
			if enemy in enemys:
				enemys.remove(enemy)

	def Tir(self, tirs, img, touches, i):
		if touches[pygame.K_SPACE] and i%self.couldown == 0:
			tirs.append(Tir(self.rect.x - 12 + self.rect.w//2, self.rect.y - 30, img, 5, 15))

	def Alive(self):
		if self.vie <= 0:
			print("Perdu")


class Enemy(ElementGraphique):
	"""
	Ennemis arrivant en face du personnage
	"""
	def __init__(self, x, y, img, pv, v, d):
		super(Enemy, self).__init__(x, y, img)
		self.vie = pv
		self.vitesse = v
		self.degats = d


	def Move(self):
		"""
		Fonction qui gère le déplacement des ennemis
		"""
		self.rect.y += self.vitesse







class Tir(ElementGraphique):
	"""
	Tirs du personnage
	"""
	def __init__(self, x, y, img, v, d):
		super(Tir, self).__init__(x, y, img)
		self.vitesse = v
		self.degats = d
		self.alive = True

	def Move(self):
		"""
		Fonction qui gère le déplacement des tirs
		"""
		self.rect.y -= self.vitesse

	def Collisions(self, enemy, enemys, perso):
		"""
		Fonction qui gère lorsqu'un tir et un ennemi se touchent
		"""
		if self.rect.colliderect(enemy.rect):
			self.alive = False
			enemy.vie -= self.degats
			if enemy in enemys and enemy.vie <= 0:
				enemys.remove(enemy)
				perso.money +=  randint(0, 1)
				print(perso.money)