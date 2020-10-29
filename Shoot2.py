import pygame
from Class import *
from Fonctions import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

largeur, hauteur = 600, 900
fenetre = pygame.display.set_mode((largeur, hauteur))
font = pygame.font.Font(None, 30)

bank = images(font)

horloge = pygame.time.Clock()

# Variables du Jeu
continuer = True
time = 0
state = "Jeu"
enemys = []
tirs = []
couldown = 40

# print(bank["perso"][0])
perso = Perso(250, 800, bank["perso"], fenetre, largeur, hauteur)
fondJeu = ElementGraphique(0, 0, bank["fond"], fenetre)
score = ElementGraphique(0, 0, bank["score"], fenetre)

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
		
		# couldown = Difficulty(time, couldown)
		if time%couldown == 0:
			New_Enemy(bank["enemys"], enemys, largeur, hauteur, fenetre)

		for enemy in enemys:
			enemy.deplacer()
			enemy.difficulte(time)
			enemy.Afficher()
			perso.Collisions(enemy, enemys)

		for tir in tirs:
			tir.Afficher()
			tir.Move()
			tir.Alive(tirs, tir)
			for enemy in enemys:
				tir.Collisions(enemy, enemys, tirs, perso)

		perso.Afficher()
		perso.Deplacer(touches, largeur)
		perso.Tir(tirs, bank["tirs"], touches, time)
		# perso.Alive()
		bank["kill"] = font.render(str(perso.kill), 1, (255, 0, 0)).convert_alpha()
		kill = ElementGraphique(70, 0, bank["kill"], fenetre)
		print(perso.kill)
		score.Afficher()
		kill.Afficher()

	pygame.display.update()

pygame.quit()