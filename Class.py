import pygame
from math import cos
from random import choice

class ElementGraphique():
	def __init__(self, img, fenetre, x=0, y=0):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = int(x)
		self.rect.y = int(y)
		self.fenetre = fenetre

		

	def afficher(self):
		self.fenetre.blit(self.image, self.rect)

	def collide(self, other):
		if self.rect.colliderect(other):
			return True
		return False


class ElementGraphiqueAnimee(ElementGraphique):
	def __init__(self, img=[],x=0,y=0,effect=None) :
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

	def afficher(self, fenetre) :
		self.fps += 0.5
		if (self.fps % 0.5 )== 0:
			self.numimage = (self.numimage + 1)%len(self.image)
			fenetre.blit(self.image[self.numimage],self.rect)



class Perso(ElementGraphique):
	def __init__(self, img, fenetre, x=0, y=0,effect=None):
		super(Perso, self).__init__(img, fenetre, x, y)
		self.vitesse = 10
		self.vie = 4
		self.boost = 0

	def deplacer(self, touches):

		l,h = self.fenetre.get_size()
		
		if touches[pygame.K_a] and self.rect.x > 0:
			if self.boost :
				self.rect.x -= self.vitesse * 2
			else :
				self.rect.x -= self.vitesse 


		if touches[pygame.K_d] and self.rect.x < l -self.rect.w :
			if self.boost :
				self.rect.x += self.vitesse * 2
			else : 
				self.rect.x += self.vitesse

		if self.boost :
			self.boost -= 1

	def Centre(self, balle, fenetre):
		if self.collide(balle):
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
		else :
			return False


class Balle(ElementGraphique):
	def __init__(self, img, fenetre, x=0, y=0):

		super(Balle, self).__init__(img, fenetre, x, y)
		self.vx = choice([-10, 10])
		self.vy = choice([-10, 10])

	def deplacer(self):
		l,h = self.fenetre.get_size()

		self.rect.x += self.vx
		if self.rect.x > l - self.rect.w:
			 self.vx = -abs(self.vx)
		if self.rect.x < 0:
			self.vx = abs(self.vx)

		self.rect.y += self.vy
		if self.rect.y > h - self.rect.h:
			 self.vy = -abs(self.vy)
		if self.rect.y < 0:
			self.vy = abs(self.vy)

class BalleAnimee(ElementGraphiqueAnimee):
		def __init__(self,img,x=0,y=0):
				ElementGraphiqueAnimee.__init__(self,img)
				self.t = 0.0
				self.truc = 10
				self.centerx = x
				self.centery = y


		def deplacer(self):
			self.t += 1.0

			self.rect.x = 50*cos(self.t/10) + 250
			self.rect.y = 2*self.t



class Bonus(ElementGraphique):
	def __init__(self, img, fenetre, x=0, y=0):
		super(Bonus, self).__init__(img, fenetre, x, y)

		self.vx = choice([-10, 10])
		self.vy = choice([-10, 10])

	def deplacer(self):

		l,h = self.fenetre.get_size()

		self.rect.x += self.vx
		if self.rect.x > l - self.rect.w:
			 self.vx = -abs(self.vx)
		if self.rect.x < 0:
			self.vx = abs(self.vx)

		self.rect.y += self.vy
		if self.rect.y > h - self.rect.h:
			 self.vy = -abs(self.vy)
		if self.rect.y < 0:
			self.vy = abs(self.vy)