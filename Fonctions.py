import pygame
from random import randint
from Class import *


def images(font):
	"""
	Fonction qui recupère les images dans le dossier
	"""
	bank = {}

	bank["fond"] = pygame.image.load("./Images/fond.jpg")
	bank["enemys"] = []
	bank["tirs"] = pygame.image.load("./Images/Tirs/bullet_blue.png")
	bank["boss"] = []

	# for i in range(1, 23):
	# 	bank["enemys"].append(pygame.image.load("./Images/Enemy/ennemi" + str(i) + ".png"))

	bank["enemys"].append(pygame.image.load("./Images/Vaisseaux/Enemy02Red1.png"))
	bank["boss"].append(pygame.image.load("./Images/Vaisseaux/Enemy01_Red_Frame_1_png_processed.png"))

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


def New_Enemy(img, enemys, largeur, hauteur, fenetre, deplacements):
	"""
	Fonction qui ajoute 1 ennemi à la liste d'ennemis
	"""
	enemys.append(Enemy(randint(50, largeur - 50), randint(-hauteur//2, 0), img, fenetre, 15, 2, 20, largeur, hauteur))
	
def New_Boss(img, enemys, largeur, hauteur, fenetre, deplacements):
	"""
	Fonction qui ajoute 1 boss à la liste des boss

	"""	
	enemys.append(Enemy(largeur//2 -15, -10, img, fenetre, 200, 1, 0, largeur, hauteur))
	enemys[-1].type = "Boss"

def BossTimer(boss):
	"""
	Fonction qui détermine lorsque le boss est terminé
	"""
	if boss.vie >= 0 and boss.type == "Boss":
		return True
	return False
