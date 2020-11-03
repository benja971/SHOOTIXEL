import pygame
from Class import *
from Fonctions import *

pygame.init()

largeur, hauteur = 600, 700
fenetre = pygame.display.set_mode((largeur, hauteur))
font = pygame.font.Font(None, 30)

bank = images(font)

horloge = pygame.time.Clock()

# Variables du Jeu
continuer = True
time = 0
state = "Jeu"
enemys = []
tirsPerso = []
couldown = 40

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
		
		if time%couldown == 0:
			New_Enemy(bank["enemys"], enemys, largeur, hauteur, fenetre)

		for enemy in enemys:
			enemy.deplacer()
			enemy.difficulte(time)
			enemy.Afficher()
			enemy.Remove(enemys)
			enemy.Collisions(perso)
			for tir in tirsPerso:
				enemy.Collisions(tir)

		for tir in tirsPerso:
			tir.Afficher()
			tir.Move()
			tir.Remove(tirsPerso)

		perso.Afficher()
		perso.Deplacer(touches, largeur)
		perso.Tir(tirsPerso, bank["tirs"], touches, time)

		bank["kill"] = font.render(str(perso.kill), 1, (255, 0, 0)).convert_alpha()
		kill = ElementGraphique(70, 0, bank["kill"], fenetre)

		score.Afficher()
		kill.Afficher()

	pygame.display.update()

pygame.quit()