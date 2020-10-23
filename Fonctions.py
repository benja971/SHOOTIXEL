import pygame
from random import randint
from math import sqrt
from Class import *


def images():
	files = ["ennemy.png", "balle.png", "fond.jpg", "BgIntroG.png", "bullet_red.png", "2.png", "Play.png", "Exit.png", "Buy.png"]

	bank = {
		file.split('.')[0]:
		pygame.image.load('Images/' + file).convert_alpha()
		for file in files
	}

	return bank


def New_Balle(img, enemys, largeur, hauteur, tirs, i):
	done = True
	x = randint(50, largeur - 50)
	y = randint(-hauteur//2, 0)

	while not done:
		for enemy in enemys:
			dist = ((x - enemy.rect.x)**2 + (y - enemy.rect.y)**2)

			if dist < 25:
				done = False
				x = randint(50, largeur - 50)
				y = randint(-hauteur//2, 0)
				break

	enemys.append(Balle(img, x, y, 15, 5, 20, "enemy"))