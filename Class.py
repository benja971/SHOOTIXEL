import pygame
from random import randint
from math import cos, sin

class ElementGraphique:
	"""
	Tous est élément graphique
	"""
	def __init__(self, x, y, img, fenetre):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.fenetre = fenetre

	def Afficher(self):
		self.fenetre.blit(self.image, self.rect)


class ElementGraphiqueAnimé(ElementGraphique):
	"""
	Animation des Elements Graphiques
	"""
	def __init__(self, x, y, img, fenetre):
		super(ElementGraphiqueAnimé, self).__init__(x, y, img[0], fenetre)
		self.images = img
		self.timer = 0
		self.numAnim = 0


	def Afficher(self):
		self.timer += 1
		if self.timer > 10:
			self.timer = 0
			self.numAnim += 1
			if self.numAnim >= len(self.images):
				self.numAnim = 0
			self.image = self.images[self.numAnim]
		super().Afficher()


class Perso(ElementGraphique):
	"""
	Personnage qu'incarne le joueur
	"""
	def __init__(self, x, y, img, fenetre, largeur, hauteur):
		super(Perso, self).__init__(x, y, img, fenetre)
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
			tirs.append(Tir(self.rect.x - 12 + self.rect.w//2, self.rect.y - 30, img, self.fenetre, 5, 15))

	def Alive(self):
		if self.vie <= 0:
			print("Perdu")


class Enemy(ElementGraphiqueAnimé):
	"""
	Ennemis animés arrivant en face du personnage
	"""
	def __init__(self, x, y, img, fenetre, pv, v, d, largeur, hauteur):
		super(Enemy, self).__init__(x, y, img, fenetre)
		self.vie = pv
		self.vitesse = v
		self.degats = d
		self.t = 0
		self.trucx = randint(10, largeur -10)
		self.trucy = randint(-10, 0)
		self.trucx2 = randint(50, 200)
		self.trucy2 = randint(50, 200)
		self.centerx = x
		self.centery = y


	def Move(self):
		"""
		Fonction qui gère le déplacement des ennemis
		"""
		self.t += 1
		self.rect.x = self.trucx2*cos(self.t/10) + self.trucx
		self.rect.y = self.trucy2*sin(self.t/10) + self.trucy + self.t


class DeplacementTordu(ElementGraphiqueAnimé):
    def __init__(self, window, img, x=0, y=0):
        ElementGraphique.__init__(self, window, img, x, y)
        self.t = 0.0
        self.truc = 10
        self.centerx = x
        self.centery = y


class Tir(ElementGraphique):
	"""
	Tirs du personnage
	"""
	def __init__(self, x, y, img, fenetre, v, d):
		super(Tir, self).__init__(x, y, img, fenetre)
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

	def Alive(self,tirs, tir):
		if tir.rect.y < -20 and tir in tirs:
			tirs.remove(tir)
			print(len(tirs))
