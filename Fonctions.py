import pygame
from random import randint, choice
from Class import Enemy
from Class import Bonus


def images(font_jeu, font_intro, font_menu, font_standart):
	"""
	Fonction qui recupère les images dans le dossier
	"""
	bank = {}

	bank["fond"] = pygame.image.load("./Images/fond.jpg")

	vaisseaux = {}
	vaisseaux["red"] = [pygame.image.load("./Images/Vaisseaux/Enemy02Red1.png")]
	vaisseaux["green"] = [pygame.image.load("./Images/Vaisseaux/Enemy02Green.png")]
	bank["vaisseaux"] = vaisseaux

	explosions = {}
	explosions["red"] = []
	explosions["green"] = []
	bank["explosions"] = explosions
	
	boss = {}
	boss["red"] = [pygame.image.load("./Images/Vaisseaux/Enemy01_Red_Frame_1_png_processed.png")]
	boss["green"] = [pygame.image.load("./Images/Vaisseaux/Enemy01_Green_Frame_1_png_processed.png")]
	boss["blue"] = [pygame.image.load("./Images/Vaisseaux/Enemy01_Teal_Frame_1_png_processed.png")]
	boss["explosion"] = []

	for i in range(23):
		if i > 9:
			boss["explosion"].append(pygame.image.load("./Images/Explosions/tile0" + str(i) + ".png"))
		else:
			boss["explosion"].append(pygame.image.load("./Images/Explosions/tile00" + str(i) + ".png"))
		
	bank["boss"] = boss
	bank["speed"] = pygame.image.load("./Images/Bonus/Powerup_Energy.png")
	bank["damages"] = pygame.image.load("./Images/Bonus/Powerup_Rocket.png")
	bank["shield"] = pygame.image.load("./Images/Bonus/Powerup_Shields.png")
	bank["heal"] = pygame.image.load("./Images/Bonus/Powerup_Health.png")
	bank["cooldown"] = pygame.image.load("./Images/Bonus/Powerup_Ammo.png")

	bank["tirsE"] = []
	bank["tirsP"] = []

	bank["HUD"] = pygame.image.load("./Images/Hud.png")

	for i in range(1, 6):
		bank["tirsE"].append(pygame.transform.rotate(pygame.image.load("./Images/Tirs/Exhaust_Frame_0" + str(i) + "_png_processed.png"), 180))
		bank["tirsP"].append(pygame.image.load("./Images/Tirs/Exhaust_Frame_0" + str(i) + "_png_processed.png"))

	for i in range(2 ,9):
		bank["explosions"]["red"].append(pygame.image.load("./Images/Explosions/Explosion01_Frame_0"+ str(i)+"_png_processed.png"))
		bank["explosions"]["green"].append(pygame.image.load("./Images/Explosions/Explosion02_Frame_0" + str(i) + "_png_processed.png"))

	# ============= Intro =============	
	bank["progression"] = []
	for i in range(1, 6):
		bank["progression"].append(pygame.image.load("./Images/progress" + str(i) + ".png"))

	bank["loading"] = font_intro.render("loading...", True, (255, 255, 255))

	# ============= Menu =============
	bank['Main'] = pygame.image.load("./Images/Menu/Main.png").convert_alpha()
	bank['interface'] = pygame.image.load("./Images/Menu/Interface.png")
	bank['Play'] = pygame.image.load("./Images/Menu/Start.png")
	bank['Exit'] = pygame.image.load("./Images/Menu/Exit.png")
	bank['Pointeur'] = pygame.image.load("./Images/Menu/Pointeur.png")
	bank['settings'] = pygame.image.load("./Images/Menu/Settings.png")
	bank['shop'] = pygame.image.load("./Images/Menu/Shop.png")
	bank['Psettings'] = pygame.image.load("./Images/Menu/Psettings.png")
	bank['Pshop'] = pygame.image.load("./Images/Menu/Pshop.png")
	bank["text_menu"] = font_menu.render('SHOOTIXEL', True, (255, 255, 255))
	# ============= Menu =============

	# ============= Life =============
	bank['Vie25'] = pygame.image.load("./Images/Life25.png").convert_alpha()
	bank['Vie50'] = pygame.image.load("./Images/Life50.png").convert_alpha()
	bank['Vie75'] = pygame.image.load("./Images/Life75.png").convert_alpha()
	bank['Vie100'] = pygame.image.load("./Images/Life100.png").convert_alpha()
	# ============= Life =============

	imgPerso = {}
	imgPerso["Right"] = []
	imgPerso["Left"] = []
	imgPerso["Standing"] = []
	bank["msgKillB"] = font_intro.render("Boss vaincue, félicitation champion !!", True, (255, 255, 255))

	for i in range(1, 3):
		imgPerso["Right"].append(pygame.image.load(
			"./Images/Vaisseaux/PlayerRight" + str(i) + ".png"))
		imgPerso["Left"].append(pygame.image.load(
			"./Images/Vaisseaux/PlayerLeft" + str(i) + ".png"))

	imgPerso["Standing"].append(pygame.image.load(
		"./Images/Vaisseaux/Standing.png"))

	bank["perso"] = imgPerso
	bank["score"] = font_standart.render("Score :", 1, (255, 0, 0))

	bank["lose"] = font_menu.render('Game Over ...', True, (255, 255, 255))
	bank["current_life"] = font_standart.render('Vie :', True, (255, 0, 0))

	return bank

def New_Enemy(bank, enemys, largeur, hauteur, fenetre, i):
	"""
	Fonction qui ajoute 1 ennemi à la liste d'ennemis
	"""
	c = choice(["red", "green"])
	enemys.append(Enemy(randint(200, largeur - 50), randint(-hauteur //2, 0), bank["vaisseaux"][c], fenetre, 2, 20, largeur, "Enemy", choice([0, 1, 2]), c))
	enemys[-1].Choix(i)


def New_Boss(bank, enemys, largeur, fenetre, i):
	"""
	Fonction qui ajoute 1 boss à la liste d'ennemis
	"""
	c = choice(["red", "green", "blue"])
	enemys.append(Enemy(largeur//2 + 150 - 15, -10, bank["boss"][c], fenetre, 1, 0, largeur, "Boss", choice([0, 1, 2]), c))
	
	enemys[-1].Choix(i)


def New_Bonus(tabBonus, bank, fenetre, largeur, time):
	t = choice(["speed", "shield", "heal", "damages", "cooldown"])
	tabBonus.append(Bonus(randint(150, largeur), randint(-20, -5), bank[t], fenetre, t, time))


def SupprTrucs(liste, explosions, bank, fenetre):
	"""
	Fonction qui supprime les éléments des listes qui ne doivent plus yêtre
	"""
	liste_keep = []
	for element in liste:
		if element.vie > 0:
			liste_keep.append(element)
		else:
			element.die(explosions, fenetre, bank)
	x = len(liste) - len(liste_keep)
	
	return x, liste_keep

def move_Pointeur(selection_menu, touches):
	"""
	Fonction qui gère le pointeur du Menu
	"""
	# évitons que le pointeur se barre trop loin
	if selection_menu >= 5:
		selection_menu = 1
	if selection_menu == 0:
		selection_menu = 4

	if touches[pygame.K_DOWN]:
		selection_menu += 1

	if touches[pygame.K_UP]:
		selection_menu -= 1

	return selection_menu

def select_collide_1(select, play_bouton, pointeur1, exit_bouton , pointeur2) :

    if select.colliderect(play_bouton.rect) :	
        pointeur1.Afficher()

    if select.colliderect(exit_bouton.rect) :
        pointeur2.Afficher()

    return select

def select_collide_2(select, pointeur_settings, settings, pointeur_shop, shop) :

    if select.colliderect(settings.rect) :
        pointeur_settings.Afficher()

    if select.colliderect(shop.rect) :
        pointeur_shop.Afficher()

    return select
