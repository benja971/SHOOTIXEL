import pygame
import os
from random import randint, random
from Class import *
from Fonctions import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

largeur, hauteur = 600, 900
fenetre = pygame.display.set_mode((largeur, hauteur))

bank = images()

horloge = pygame.time.Clock()

# Variables du Jeu
continuer = True
i = 0
state = "Jeu"
enemys = []
tirs = []
couldown = 25


# Menu
fondIntro = ElementGraphique(-700, -500, bank["BgIntroG"])
Play = ElementGraphique(largeur//2, hauteur//5, bank["Play"])
Play.rect.x -= Play.rect.w//2
Quit = ElementGraphique( largeur//2, 2 *hauteur//5, bank["Exit"])
Quit.rect.x -= Play.rect.w//2
Buy = ElementGraphique(largeur//2, 3 *hauteur//5, bank["Buy"])
Buy.rect.x -= Play.rect.w//2
perso = Perso(bank["ennemy"], 250, 800, largeur, hauteur)
fondJeu = ElementGraphique(0, 0, bank["fond"])

while continuer:
	horloge.tick(30)
	i += 1
	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE]:
		continuer = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False

	if state == "Menu":

		Play.Afficher(fenetre)
		Quit.Afficher(fenetre)
		# Buy.Afficher(fenetre)

	if state == "Jeu":

		fondJeu.Afficher(fenetre)

		if i%couldown == 0:
			New_Enemy(bank["2"], enemys, largeur, hauteur)

		if i%100 == 0:
			formation(enemys, largeur, bank["2"])

		for enemy in enemys:
			enemy.Move()
			enemy.Afficher(fenetre)
			perso.Collisions(enemy, enemys)

		for tir in tirs:
			tir.Afficher(fenetre)
			tir.Move()
			for enemy in enemys:
				tir.Collisions(enemy, enemys, perso)

		perso.Afficher(fenetre)
		perso.Deplacer(touches, largeur)
		perso.Tir(tirs, bank["bullet_blue"], touches, i)
		perso.Alive()
		
	pygame.display.update()

pygame.quit()