import pygame
from random import choice, randint
from math import cos, sin

class ElementGraphique:
	"""
	Tout est élément graphique
	"""
	def __init__(self, x, y, img, fenetre):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.fenetre = fenetre

	def Collide(self, other):
		if self.rect.colliderect(other.rect):
			return True
		return False

	def Collisions(self, other):
		"""
		Fonction que gère lorsqu'un élément en touche un autre
		"""
		if self.Collide(other):

			if self.type == "Enemy" or self.type == "Boss":
				if other.type == "TirPerso":
					self.TakeDamages(other)
					other.Kill()

				elif other.type == "Perso":
					other.TakeDamages(self)
					self.Kill()

	def TakeDamages(self, other):
		"""
		Fonction qui retire de la vie à un élément en cas de collision
		"""
		self.vie -= other.degats

	def Kill(self):
		"""
		Fonction qui tue un élément
		"""
		self.vie = 0

	def Remove(self, list_conscernee):
		"""
		Fonction qui supprime les éléments qui n'ont plus lieu d'être
		"""
		if self.vie <= 0 and self in list_conscernee:
			list_conscernee.remove(self)

	def Afficher(self):
		self.fenetre.blit(self.image, self.rect)


class ElementGraphiqueAnimé(ElementGraphique):
	"""
	Animation des Elements Graphiques
	"""
	def __init__(self, x, y, img, fenetre):
		super().__init__(x, y, img[0], fenetre)
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


class ElementAnimeDir(ElementGraphiqueAnimé):
	def __init__(self, x, y, images_all_dir, fenetre):
		super().__init__(x, y, images_all_dir["Standing"], fenetre)
		self.images_all_dir = images_all_dir
		self.direction ="Standing"
		self.old_direction="Standing"


	def Afficher(self) :
		if self.old_direction != self.direction:
			self.images = self.images_all_dir[self.direction]
			self.numAnim=0
			self.old_direction = self.direction

		super().Afficher()


class Perso(ElementAnimeDir):
	"""
	Personnage qu'incarne le joueur
	"""
	def __init__(self, x, y, images_all_dir, fenetre, largeur, hauteur):
		super().__init__(x, y, images_all_dir, fenetre)
		self.type = "Perso"
		self.rect.x = largeur // 2 - self.rect.w // 2
		self.rect.y = hauteur - self.rect.h
		self.vie = 100
		self.vitesse = 4
		self.cooldown = 20
		self.money = 0
		self.kill = 0

	def Deplacer(self, touches, largeur):
		self.direction = "Standing"
		self.numAnim = 0

		if touches[pygame.K_d] and self.rect.x <= largeur - self.rect.w:
			self.rect.x += self.vitesse
			self.direction = "Right"

		if touches[pygame.K_a] and self.rect.x >= 0:
			self.rect.x -= self.vitesse
			self.direction = "Left"


	def Tir(self, tirs, img, touches, i):
		if touches[pygame.K_SPACE] and i%self.cooldown == 0:
			tirs.append(Tir(self.rect.x - 12 + self.rect.w//2, self.rect.y - 30, img, self.fenetre, 5, 15))

	def Bonus(self, bonus):
		if self.colliderect(bonus):
			if self.type == 'speed':
				self.vitesse = 4*2

	def Alive(self):
		if self.vie <= 0:
			print("Perdu")


class Enemy(ElementGraphiqueAnimé):
	"""
	Ennemis animés arrivant en face du personnage
	"""
	def __init__(self, x, y, img, fenetre, pv, v, d, largeur, hauteur, _type):
		super().__init__(x, y, img, fenetre)
		self.vie = pv
		self.vitesse = v
		self.degats = d
		self.t = 0
		self.type = _type
		self.trucx = randint(10, largeur -10)
		self.trucy = randint(-10, 0)
		self.trucx2 = randint(50, 550)
		self.trucy2 = randint(50, 550)
		self.centerx = x
		self.centery = y

	def DescenteLinéaire(self):
		"""
		Les ennemis descendent en ligne droite
		"""
		self.rect.y += self.vitesse

	def DescenteEnCercles(self):
		"""
		Les ennemis descendent en faisant des cercles de tailles différentes
		"""
		self.t += 1
		self.rect.x = 50*cos(self.t/20) + self.trucx
		self.rect.y = 50*sin(self.t/20) + self.trucy + self.t

	def DescenteSinusoïdale(self):
		"""
		Les ennemis descendent en suivant des trajectoires sinusoîdales
		"""
		self.t += 1
		self.rect.x = self.trucx2*cos(self.t/20) + self.trucx2
		self.rect.y = self.t
	
class Tir(ElementGraphique):
	"""
	Tirs du personnage
	"""
	def __init__(self, x, y, img, fenetre, v, d):
		super().__init__(x, y, img, fenetre)
		self.type = "TirPerso"
		self.vitesse = v
		self.degats = d
		self.vie = 1

	def Move(self):
		"""
		Fonction qui gère le déplacement des tirs du Perso
		"""
		self.rect.y -= self.vitesse

class Bonus(ElementGraphique):
	def __init__(self, x, y, img, fenetre, bonus, time):
		super(Bonus, self).__init__(img, fenetre, x,y)
		self.vx = choice([-5, 5])
		self.vy = choice([-5, 5])
		self.type = bonus
		self.time = time
	
	def Deplacer(self, largeur, hauteur):
		self.rect.x += self.vx
		if self.rect.x > largeur - self.rect.w:
			self.vx = -abs(self.vx)
		if self.rect.x < 0:
			self.vx = abs(self.vx)

		self.rect.y += self.vy
		if self.rect.y > hauteur - self.rect.h :
			self.vy = -abs(self.vy)
		if self.rect.y < 0 :
			self.vy = abs(self.vy)

	def alive(self, time, tabBonus):
		if time - self.time >= 250:
			if self in tabBonus:
				tabBonus.remove(self)
		
