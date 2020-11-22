import pygame
from Class import ElementGraphique
from Class import Perso 
from Fonctions import * 


pygame.init()

largeur, hauteur = 750, 800
fenetre = pygame.display.set_mode((largeur, hauteur))
font = pygame.font.Font(None, 30)

bank = images(font)

horloge = pygame.time.Clock()

# Variables du Jeu
continuer = True
time = 0
state = "Jeu"
selection_menu = 1
enemys = []
tabBonus = []
cooldownEn = 40
cooldownBoss = 1000
countBoss = 0
boss = False
couldown = 40

# ============= Menu =============
menu_fond = ElementGraphique(0, 0, bank['Main'], fenetre)
text_presentation = ElementGraphique(largeur / 2 - 240, 50, bank['text_menu'], fenetre)
play_Bouton = ElementGraphique(largeur / 2 - 75, 150, bank['Play'], fenetre)
option_Bouton = ElementGraphique(largeur / 2 - 75, 350, bank['Option'], fenetre)
exit_Bouton = ElementGraphique(largeur / 2 - 75, 550, bank['Exit'], fenetre)
pointeur1 = ElementGraphique(largeur / 2 - 200, 150, bank['Pointeur'], fenetre)
pointeur2 = ElementGraphique(largeur / 2 - 200, 350, bank['Pointeur'], fenetre)
pointeur3 = ElementGraphique(largeur / 2 - 200, 550, bank['Pointeur'], fenetre)

# ============= Son Menu =============
son_menu = pygame.mixer.Sound("./Son Effect/Menu/Intro.wav")
son_pointeur_menu = pygame.mixer.Sound("./Son Effect/Menu/pointeur.wav")
son_menu.play()  # Lancement du son_menu hors de la boucle, pour éviter le ralentissement sur le son
# ============= Son Menu =============
# ============= Menu =============

# ============= Jeu =============
perso = Perso(250, 800, bank["perso"], fenetre, largeur, hauteur)
fondJeu = ElementGraphique(150, 0, bank["fond"], fenetre)
score = ElementGraphique(0, 0, bank["score"], fenetre)
tir_son = pygame.mixer.Sound("./son Effect/1/Laser_Shoot.wav")
BLACK = (0, 0, 0)
# ============= Jeu =============

while continuer:
	horloge.tick(60)
	time += 1
	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE]:
		continuer = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False

	if state == "Menu":
		menu_fond.Afficher()
		text_presentation.Afficher()
		play_Bouton.Afficher()
		option_Bouton.Afficher()
		exit_Bouton.Afficher()
		horloge.tick(10)

		selection_menu = move_Pointeur(selection_menu, touches, son_pointeur_menu)

		if selection_menu == 1:
			pointeur1.Afficher()
			if touches[pygame.K_RETURN]:
				son_menu.stop()
				state = 'Jeu'

		if selection_menu == 2:
			pointeur2.Afficher()
			if touches[pygame.K_RETURN]:
				state = 'Option'

		if selection_menu == 3:
			pointeur3.Afficher()
			if touches[pygame.K_RETURN]:
				continuer = False

	if state == "Jeu":

		fenetre.fill(BLACK)
		fondJeu.Afficher()


		if time % 333 == 0 and len(tabBonus) <= 1:
			New_Bonus(tabBonus, bank, fenetre, largeur, time)

		if time%250 == 0:
			cooldownEn -= 1

		if time%cooldownEn == 0 and not boss:
			New_Enemy(bank["enemys"], enemys, largeur, hauteur, fenetre, time)

		if time % cooldownBoss == 0:
			boss = True
			New_Boss(bank["boss"], enemys, largeur, fenetre, time)

		if len(enemys) > 0:
			boss = BossTimer(enemys[-1])

		for enemy in enemys:
			enemy.tir(bank["tirsE"], fenetre, time)
			enemy.deplacerAfficherTirs()
			enemy.DescenteEnCercles()
			enemy.Afficher()
			Boss = enemy.Remove(enemys)
			enemy.Collisions(perso, perso, time)
			for tir in perso.tirs:
				enemy.Collisions(tir, perso, time)

		for bonus in tabBonus:
			bonus.Afficher()
			bonus.Deplacer(largeur, hauteur)
			bonus.alive(time)

		for tir in perso.tirs:
			if perso.plusdamges:
				tir.damagesUp()
			else:      
				tir.normalDamages()

			tir.Afficher()
			tir.Deplacer()
			for bonus in tabBonus:
				bonus.Collisions(tir, perso, time)
				bonus.resetBonus(perso, time)

		perso.Afficher()
		perso.Deplacer(touches, largeur)
		perso.Tir(bank["tirsE"], touches, time, tir_son)

		x, enemys = SupprTrucs(enemys)
		p, perso.tirs = SupprTrucs(perso.tirs)
		p, tabBonus = SupprTrucs(tabBonus)

		perso.kill += x

		if perso.kill > 0:
			print(perso.kill)
			bank["kill"] = font.render(str(perso.kill), 1, (255, 0, 0)).convert_alpha()
			kill = ElementGraphique(70, 0, bank["kill"], fenetre)
			kill.Afficher()

		score.Afficher()
		


	pygame.display.update()

pygame.quit()
