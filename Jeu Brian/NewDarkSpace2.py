import pygame, os, time
from random import*
from pygame.locals import*
import math

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def loadImage():
	images = {}
	images['avant-plan'] = pygame.image.load("images/avant-plan.png").convert()
	images['fond_niveau1'] = pygame.image.load("images/bg.png").convert()
	images['perso'] = pygame.image.load("images/DurrrSpaceShip.png").convert_alpha()
	images['balle'] = pygame.image.load("images/1.png").convert_alpha()
	images['Main'] = pygame.image.load("images/BgM.jpg").convert_alpha()
	images['Vie25'] = pygame.image.load("images/Life25.png").convert_alpha()
	images['Vie50'] = pygame.image.load("images/Life50.png").convert_alpha()
	images['Vie75'] = pygame.image.load("images/Life75.png").convert_alpha()
	images['Vie100'] = pygame.image.load("images/Life100.png").convert_alpha()
	images['Play'] = pygame.image.load("images/Play.png").convert_alpha()
	images['Option'] = pygame.image.load("images/Option.png").convert_alpha()
	images['Exit'] = pygame.image.load("images/Exit.png").convert_alpha()
	images['pointeur'] = pygame.image.load("images/Pointeur.png").convert_alpha()
	images['list_bonus'] = pygame.image.load("images/boost.png").convert_alpha()
	images['uplife'] = pygame.image.load("images/UpLife.png").convert_alpha()


	font = pygame.font.Font('Text/Kemco Pixel Bold.ttf', 90)
	images['Text'] = font.render('DarkSpace2', True, (255,255,255))
	images['Text_avant_plan'] = font.render('Obersian presents...', True, (255,255,255))


	images["PersoAnimee"] = []
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi1.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi2.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi3.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi4.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi5.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi6.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi7.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi8.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi9.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi10.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi11.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi12.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi13.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi14.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi15.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi16.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi17.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi18.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi19.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi20.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi21.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi22.png").convert_alpha())
	images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi23.png").convert_alpha())

	return images



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

	def Boost(self):
		if self.collide(bonus):
			self.boost += 300

	def UpLife(self):
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

			self.rect.x = 50*math.cos(self.t/10) + 250
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


	 
# def ajouterBalles(list_balles,fenetre):
# 	if (i%300) == 0 and len(list_balles) < 3:
# 		list_balles.append(BalleAnimee(images["PersoAnimee"],fenetre, largeur/2, hauteur/2))

def ajouterBalles(list_balles,i,largeur,hauteur):
	if (i%100) == 0 and len(list_balles) < 3:
		list_balles.append(BalleAnimee(images["PersoAnimee"],randint(0,largeur),randint(0,hauteur)))

def ajouterBonus(list_bonus, fenetre):
	if (i%800) == 0 and len(list_bonus) < 1 :
		list_bonus.append(Bonus(images["list_bonus"],fenetre, largeur/2-30, hauteur/2-600))

def ajouterUpLife(list_uplife, fenetre):
	if (i%1500) == 0 and len(list_uplife) < 1: 
		list_uplife.append(Bonus(images["uplife"],fenetre, largeur/2-30, hauteur/2-600))

def lireTextes():
	textes = {}
	return textes

		
pygame.init()

state = 'jeu'
largeur = 600
hauteur = 1000
fenetre = pygame.display.set_mode((largeur, hauteur))
rectFenetre = fenetre.get_rect()
pygame.display.set_caption('DarkSpace2.0')
horloge = pygame.time.Clock()
white = (255,255,255)
images = loadImage()


#intro
img_intro = ElementGraphique(images['avant-plan'], fenetre, 0,0)
Text_intro = ElementGraphique(images['Text_avant_plan'], fenetre, largeur/2-650, hauteur/2)
intro_son = pygame.mixer.Sound("Son/Lancement.wav")
		
#Menu
main = ElementGraphique(images['Main'],fenetre, 0,0)
play = ElementGraphique(images['Play'],fenetre, largeur/2-75, 300)
option = ElementGraphique(images['Option'],fenetre, largeur/2-75, 500)
exit = ElementGraphique(images['Exit'],fenetre, largeur/2-75,700)
pointeur1 = ElementGraphique(images['pointeur'],fenetre, largeur/2-200,300)
pointeur2 = ElementGraphique(images['pointeur'],fenetre, largeur/2-200,500)
pointeur3 = ElementGraphique(images['pointeur'],fenetre, largeur/2-200,700)
text_menu = ElementGraphique(images['Text'], fenetre,largeur/2-320, 100)
son_menu = pygame.mixer.Sound("Son/Intro.wav")
bruit_pointeur = pygame.mixer.Sound("Son/3543.wav")
son_jeu = pygame.mixer.Sound("Son/Jeu.wav")



#jeu
fond = ElementGraphique(images['fond_niveau1'], fenetre, 0,0)
perso = Perso(images['perso'], fenetre, 275, 850)
Vie25 = ElementGraphique(images['Vie25'], fenetre, largeur-75, 50)
Vie50 = ElementGraphique(images['Vie50'], fenetre, largeur-75, 50)
Vie75 = ElementGraphique(images['Vie75'], fenetre, largeur-75, 50)
Vie100 = ElementGraphique(images['Vie100'], fenetre, largeur-75, 50)
list_balles = []
list_bonus = []
list_uplife = []

i = 0
tour = 0
select = 1
continuer = 1
intro_son.play()

while continuer:
	i += 1
	tour += 1
	touches = pygame.key.get_pressed()
	if touches[pygame.K_ESCAPE] :
		continuer = 0

	if state == "Intro":
		horloge.tick(10)
		img_intro.afficher()
		Text_intro.afficher()
		if i == 30:
			i=0
			state = "Menu"
			son_menu.play()


	if state == 'Menu':
		perso.vie = 4
		son_jeu.stop()
		list_balles.clear()
		list_bonus.clear()
		list_uplife.clear()
		horloge.tick(10)
		main.afficher()
		text_menu.afficher()
		play.afficher()
		option.afficher()
		exit.afficher()

		if select == 1:
			pointeur1.afficher()
			if touches[pygame.K_RETURN]:
				i=1
				son_menu.stop()
				son_jeu.play()
				state = 'jeu'

		if select == 2:
			pointeur2.afficher()
			if touches[pygame.K_RETURN]:
				state = 'option'

		if select == 3 :
			pointeur3.afficher()
			if touches[pygame.K_RETURN]:
				continuer = False

		if select >= 4:
			select = 1
		if select == 0:
			select = 3

		if touches[pygame.K_DOWN]:
			bruit_pointeur.play()            
			select += 1

		if touches[pygame.K_UP]:
			bruit_pointeur.play()            
			select -= 1


	if state == 'jeu':
		horloge.tick(75)
		perso.deplacer(touches)
		textes = lireTextes()

		ajouterBonus(list_bonus, fenetre)
		ajouterBalles(list_balles,i,largeur,hauteur)
		ajouterUpLife(list_uplife, fenetre)

		aSuppr = []

		for balle in list_balles :
			if perso.collide(balle):
				perso.Centre(balle, fenetre)
				aSuppr.append(balle)

		for balle in aSuppr :
			list_balles.remove(balle)


		aSuppr.clear()

		for bonus in list_bonus :
			if perso.collide(bonus):
				perso.Boost()
				aSuppr.append(bonus) 
			if bonus.rect.y > hauteur :
				aSuppr.append(bonus)

		for bonus in aSuppr :
			list_bonus.remove(bonus)


		aSuppr.clear()

		for uplife in list_uplife :
			if perso.collide(uplife):
				perso.UpLife()
				aSuppr.append(uplife)
			elif uplife.rect.y > hauteur :
				aSuppr.append(uplife)

		for bonus in aSuppr :
			list_uplife.remove(uplife)


		if perso.Envie():
			state = 'jeu'
		else :
			state = 'Menu'

		fond.afficher()
		perso.afficher()
		Vie100.afficher()

		for balle in list_balles:
			balle.afficher(fenetre)
			balle.deplacer()


		for bonus in list_bonus:
			bonus.afficher()
			bonus.deplacer()

		for uplife in list_uplife:
			uplife.afficher()
			uplife.deplacer()                        


	for event in pygame.event.get():
		if event.type == pygame.QUIT:     
			continuer = 0

	pygame.display.update()
pygame.quit()