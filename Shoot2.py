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
time = 0
state = "Jeu"
enemys = []
tirs = []
couldown = 25

perso = Perso(250, 800, bank["perso"], fenetre, largeur, hauteur)
fondJeu = ElementGraphique(0, 0, bank["fond"], fenetre)

while continuer:
	horloge.tick(60)
	time += 1
	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE]:
		continuer = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False

	if state == "Jeu":

		fondJeu.Afficher()

		if time%couldown == 0:
			New_Enemy(bank["enemys"], enemys, largeur, hauteur, fenetre)

		for enemy in enemys:
			enemy.Move()
			enemy.Afficher()
			perso.Collisions(enemy, enemys)

		for tir in tirs:
			tir.Afficher()
			tir.Move()
			tir.Alive(tirs, tir)
			for enemy in enemys:
				tir.Collisions(enemy, enemys, perso)

		perso.Afficher()
		perso.Deplacer(touches, largeur)
		perso.Tir(tirs, bank["tirs"], touches, time)
		perso.Alive()
		
	pygame.display.update()

pygame.quit()