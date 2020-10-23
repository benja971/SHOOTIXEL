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
i = 0
continuer = True
state = "Jeu"

enemys = []
tirs = []

fondIntro = ElementGraphique(bank["BgIntroG"], -700, -500)
Play = ElementGraphique(bank["Play"], largeur//2, hauteur//5)
Play.rect.x -= Play.rect.w//2
Buy = ElementGraphique(bank["Buy"], largeur//2, 3 *hauteur//5 )
Buy.rect.x -= Play.rect.w//2
Quit = ElementGraphique(bank["Exit"], largeur//2, 2 *hauteur//5 )
Quit.rect.x -= Play.rect.w//2
perso = Perso(bank["ennemy"], 250, 800, largeur, hauteur)
fondJeu = ElementGraphique(bank["fond"], 0, 0)

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
		
		fondIntro.Afficher(fenetre)
		Play.Afficher(fenetre)
		Quit.Afficher(fenetre)
		# Buy.Afficher(fenetre)

	if state == "Jeu":

		fondJeu.Afficher(fenetre)

		if i%5 == 0:
			New_Balle(bank["2"], enemys, largeur, hauteur, tirs, i)

		for enemy in enemys:
			enemy.Move()
			enemy.Afficher(fenetre)
			# Alive(enemys, enemy)
			# perso.Collisions(enemy, enemys)

		for tir in tirs:
			tir.Afficher(fenetre)
			tir.MoveTirs()
			for enemy in enemys:
				tir.Collisions(enemy, enemys)

		perso.Afficher(fenetre)
		perso.Deplacer(touches, largeur)
		perso.Tir(tirs, bank["bullet_red"], i, touches)
		perso.Alive()
		
	tirs = list(filter(lambda tir: tir.alive, tirs))
	enemys = list(filter(lambda eneny: enemy.alive, enemys))


	pygame.display.update()

pygame.quit()