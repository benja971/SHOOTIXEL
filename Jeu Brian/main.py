from Joueur import Perso
from Bonus import *
from Fonction import *
from ElementGraphique import ElementGraphique
import pygame

pygame.init()

largeur, hauteur = 600, 1000
fenetre = pygame.display.set_mode((largeur, hauteur))
horloge = pygame.time.Clock()
images = loadImage()

continuer = True
i = 0
Bonus_l = []
Enemys_l = []

Fond = ElementGraphique(images["fond_niveau1"], fenetre, 0, 0)
Perso = Perso(images["perso"], fenetre, 0, 0, 10, 4)
Perso.Centre(largeur)

while continuer:
	i += 1
	horloge.tick(30)
	touches = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False

	if touches[pygame.K_ESCAPE]:
		continuer = False

	New_Enemy(i, Enemys_l, images, largeur, fenetre)
	New_Bonus(i, Bonus_l, images, fenetre)

	Fond.afficher()

	for enemy in Enemys_l:
		enemy.afficher(fenetre)
		enemy.deplacer()

	for bonus in Bonus_l:
		bonus.afficher()
		bonus.deplacer(largeur, hauteur)
		bonus.alive(i, Bonus_l)

	Perso.afficher()
	Perso.deplacer(touches, largeur)

	pygame.display.update()
pygame.quit()