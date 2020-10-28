import pygame
from random import randint
from Class import *


def images():
	files = ["joueur.png", "balle.png", "fond.jpg", "BgIntroG.png", "bullet_blue.png", "2.png", "Play.png", "Exit.png", "Buy.png"]

	bank = {
		file.split('.')[0]:
		pygame.image.load('Images/' + file).convert_alpha()
		for file in files
	}

	return bank


def New_Enemy(img, enemys, largeur, hauteur):
	enemys.append(Enemy(randint(50, largeur - 50), randint(-hauteur//2, 0), img, 15, 5, 20))


def formation(enemys, largeur, img):
	"""
	Groupe d'ennemis arrivant enssemble
	"""	
	enemys.append(Enemy(largeur// 2 - enemys[0].rect.w, -100, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 + enemys[0].rect.w, -100, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 - enemys[0].rect.w, -150, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 + enemys[0].rect.w, -150, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 - enemys[0].rect.w, -200, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 + enemys[0].rect.w, -200, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 - enemys[0].rect.w, -250, img, 20, 5, 15))
	enemys.append(Enemy(largeur// 2 + enemys[0].rect.w, -250, img, 20, 5, 15))