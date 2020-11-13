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
enemys_keep = []
tirsPerso = []
tirsPerso_keep = []
cooldownEn = 40
cooldownBoss = 1000
countBoss = 0
boss = False

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
		
		if time%cooldownEn == 0 and not boss:
			New_Enemy(bank["enemys"], enemys, largeur, hauteur, fenetre, deplacements)

		if time%cooldownBoss == 0:
			boss = True
			New_Boss(bank["boss"], enemys, largeur, hauteur, fenetre, deplacements)

		if len(enemys)>0:
			boss = BossTimer(enemys[-1])

		for enemy in enemys:
			enemy.DescenteLinéaire()
			enemy.Afficher()
			enemy.Collisions(perso)
			for tir in tirsPerso:
				enemy.Collisions(tir)

		for tir in tirsPerso:
			tir.Afficher()
			tir.Move()

		perso.Afficher()
		perso.Deplacer(touches, largeur)
		perso.Tir(tirsPerso, bank["tirs"], touches, time)

		enemys = SupprTrucs(enemys)
		tirsPerso = SupprTrucs(tirsPerso)

		bank["kill"] = font.render(str(perso.kill), 1, (255, 0, 0)).convert_alpha()
		kill = ElementGraphique(70, 0, bank["kill"], fenetre)
		score.Afficher()
		kill.Afficher()

	pygame.display.update()

pygame.quit()