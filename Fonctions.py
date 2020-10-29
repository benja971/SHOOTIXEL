import pygame
from random import randint
from Class import *


def images(font):

	bank = {}

	bank["fond"] = pygame.image.load("./Images/fond.jpg")
	bank["enemys"] = []
	bank["tirs"] = pygame.image.load("./Images/Tirs/bullet_blue.png")

	for i in range(1, 23):
		bank["enemys"].append(pygame.image.load("./Images/Enemy/ennemi" + str(i) + ".png"))

	imgPerso = {}
	imgPerso["Right"] = []
	imgPerso["Left"] = []
	imgPerso["Standing"] = []

	for i in range(1,3):
		imgPerso["Right"].append(pygame.image.load("./Images/Vaisseaux/PlayerRight" + str(i) + ".png"))
		imgPerso["Left"].append(pygame.image.load("./Images/Vaisseaux/PlayerLeft" + str(i) + ".png"))

	imgPerso["Standing"].append(pygame.image.load("./Images/Vaisseaux/Standing.png"))

	bank["perso"] = imgPerso
	bank["score"] = font.render("Score :", 1, (255, 0, 0)).convert_alpha()


	return bank


def New_Enemy(img, enemys, largeur, hauteur, fenetre):
	enemys.append(Enemy(randint(50, largeur - 50), randint(-hauteur//2, 0), img, fenetre, 15, 2, 20, largeur, hauteur))
	enemys[-1].ChoixDeplacement()

def Difficulty(time, couldown):
	if time%100 == 0:
		couldown = couldown - couldown*0.1
		return couldown
		