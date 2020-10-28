import pygame
from random import randint
from Class import *


def images():

	bank = {}
	bank["fond"] = pygame.image.load("./Images/fond.jpg")
	bank["perso"] = pygame.image.load("./Images/Vaisseaux/vaisseaubleu.png")
	bank["tirs"] = pygame.image.load("./Images/Tirs/bullet_blue.png")

	bank["enemys"] = []
	for i in range(1, 23):
		bank["enemys"].append(pygame.image.load("./Images/Enemy/ennemi" + str(i) + ".png"))
	


	return bank


def New_Enemy(img, enemys, largeur, hauteur, fenetre):
	enemys.append(Enemy(randint(50, largeur - 50), randint(-hauteur//2, 0), img, fenetre, 15, 5, 20, largeur, hauteur))
