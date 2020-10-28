#!/usr/bin/env python3
import pygame
from random import*
from pygame.locals import*
from Bonus import *
from Animation import *
from Joueur import *
from Monster import *
from Fonction import *


def ajouterMonstres(list_monstres, i, largeur, hauteur):
	if (i % 100) == 0 and len(list_monstres) < 3:
		list_monstres.append(MonstreAnimee(
			images["PersoAnimee"], randint(0, largeur), randint(0, hauteur)))


def ajouterBonus(list_bonus, fenetre):
	if (i % 800) == 0 and len(list_bonus) < 1:
		list_bonus.append(
			Bonus(images["list_bonus"], fenetre, largeur/2-30, hauteur/2-600))


def ajouterUpLife(list_uplife, fenetre):
	if (i % 1500) == 0 and len(list_uplife) < 1:
		list_uplife.append(
			Bonus(images["uplife"], fenetre, largeur/2-30, hauteur/2-600, None))




pygame.init()

state = 'jeu'
largeur = 600
hauteur = 1000
fenetre = pygame.display.set_mode((largeur, hauteur))
rectFenetre = fenetre.get_rect()
pygame.display.set_caption('DarkSpace2.0')
horloge = pygame.time.Clock()
white = (255, 255, 255)
images = loadImage()


#intro
img_intro = ElementGraphique(images['avant-plan'], fenetre, 0, 0)
Text_intro = ElementGraphique(
images['Text_avant_plan'], fenetre, largeur/2-230, hauteur/2)
intro_son = pygame.mixer.Sound("Son/Lancement_1.wav")

#Menu
main = ElementGraphique(images['Main'], fenetre, 0, 0)
play = ElementGraphique(images['Play'], fenetre, largeur/2-75, 300)
option = ElementGraphique(images['Option'], fenetre, largeur/2-75, 500)
exit = ElementGraphique(images['Exit'], fenetre, largeur/2-75, 700)
pointeur1 = ElementGraphique(images['pointeur'], fenetre, largeur/2-200, 300)
pointeur2 = ElementGraphique(images['pointeur'], fenetre, largeur/2-200, 500)
pointeur3 = ElementGraphique(images['pointeur'], fenetre, largeur/2-200, 700)
text_menu = ElementGraphique(images['Text'], fenetre, largeur/2-270, 100)
son_menu = pygame.mixer.Sound("Son/Intro.wav")
bruit_pointeur = pygame.mixer.Sound("Son/pointeur.wav")
son_jeu = pygame.mixer.Sound("Son/Jeu.wav")


#jeu
fond = ElementGraphique(images['fond_niveau1'], fenetre, 0, 0)
perso = Perso(images['perso'], fenetre, 275, 850)
Vie25 = ElementGraphique(images['Vie25'], fenetre, largeur-75, 50)
Vie50 = ElementGraphique(images['Vie50'], fenetre, largeur-75, 50)
Vie75 = ElementGraphique(images['Vie75'], fenetre, largeur-75, 50)
Vie100 = ElementGraphique(images['Vie100'], fenetre, largeur-75, 50)
hit_sound = pygame.mixer.Sound("Son/Hit.wav")
list_monstres = []
list_bonus = []
list_uplife = []

i = 0
tour = 0
select = 1
continuer = 1
# intro_son.play()
son_menu.play()

while continuer:
	i += 1
	tour += 1
	touches = pygame.key.get_pressed()
	if touches[pygame.K_ESCAPE]:
		continuer = 0

	if state == "Intro":
		horloge.tick(10)
		img_intro.afficher()
		Text_intro.afficher()
		if i == 30:
			i = 0
			state = "Menu"
			# intro_son.stop()
			# son_menu.play()

	if state == 'Menu':
		perso.vie = 4
		son_jeu.stop()
		list_monstres.clear()
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
				i = 1
				son_menu.stop()
				son_jeu.play()
				state = 'jeu'

		if select == 2:
			pointeur2.afficher()
			if touches[pygame.K_RETURN]:
				state = 'option'

		if select == 3:
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
		ajouterBonus(list_bonus, fenetre)
		ajouterMonstres(list_monstres, i, largeur, hauteur)
		ajouterUpLife(list_uplife, fenetre)

		aSuppr = []

		for monstre in list_monstres:
			if perso.collide(monstre):
				perso.Centre(monstre, largeur)
				aSuppr.append(monstre)
				hit_sound.play()


		for monstre in aSuppr:
			list_monstres.remove(monstre)

		aSuppr.clear()

		for bonus in list_bonus:
			if perso.collide(bonus):
				perso.Boost(bonus)
				aSuppr.append(bonus)
			if bonus.rect.y > hauteur:
				aSuppr.append(bonus)

		for bonus in aSuppr:
			list_bonus.remove(bonus)

		aSuppr.clear()


		for uplife in list_uplife:
			if perso.collide(uplife):
				perso.UpLife(uplife)
				aSuppr.append(uplife)
			elif uplife.rect.y > hauteur:
				aSuppr.append(uplife)

		# for bonus in aSuppr: 
		# 	list_uplife.remove(uplife)

		if perso.Envie():
			state = 'jeu'
		else:
			state = 'Menu'
			son_menu.play()

		fond.afficher()
		perso.afficher()
		# Vie100.afficher()

		if perso.vie == 4 :
			Vie100.afficher()

		if perso.vie == 3 :
			Vie75.afficher()
		
		if perso.vie == 2:
			Vie50.afficher()

		if perso.vie == 1:
			Vie25.afficher()

		for monstre in list_monstres:
			monstre.afficher(fenetre)
			monstre.deplacer(i)

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
