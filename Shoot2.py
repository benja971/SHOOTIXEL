import pygame
from Class import ElementGraphiqueAnimé
from Class import ElementGraphique
from Class import Perso 
from Fonctions import * 


pygame.init()

font_menu = pygame.font.Font('Text/Positive System.otf', 60)
font_intro = pygame.font.Font('./Text/Retro Gaming.ttf', 30)
font_jeu = pygame.font.Font('./Text/Retro Gaming.ttf', 20)
font_standart = pygame.font.Font(None, 30)

largeur, hauteur = 750, 800
fenetre = pygame.display.set_mode((largeur, hauteur))
bank = images(font_jeu, font_intro, font_menu, font_standart)

horloge = pygame.time.Clock()

# Variables du Jeu
continuer = True
time = 0
state = "Menu"
selection_menu = 1
selection_menu1 = 1
enemys = []
tabBonus = []
explosions = []
cooldownEn = 40
cooldownBoss = 1000
boss = False
couldown = 40

xs, ys = 0, 0 #flag test*********

# ============= Intro =============

barDeProgression = ElementGraphiqueAnimé(largeur/2 - 160, 350, bank["progression"], fenetre) 
loading = ElementGraphique(largeur/2 - 160, 290, bank["loading"], fenetre)

# ============= Menu =============
menu_fond = ElementGraphique(0 , 0, bank['Main'], fenetre)
interface = ElementGraphique(largeur/2-325 , 70, bank['interface'], fenetre)
play_Bouton = ElementGraphique(largeur / 2 - 120, 225, bank['Play'], fenetre)
text_presentation = ElementGraphique(largeur/2 - 160, 95, bank["text_menu"], fenetre)
exit_Bouton = ElementGraphique(largeur / 2 - 120, 480, bank['Exit'], fenetre)
pointeur1 = ElementGraphique(largeur / 2 - 175, 235, bank['Pointeur'], fenetre)
pointeur2 = ElementGraphique(largeur / 2 - 175, 490, bank['Pointeur'], fenetre)
pointeur_settings = ElementGraphique(125, 520, bank['Psettings'], fenetre)
pointeur_Shop = ElementGraphique(580, 520, bank['Pshop'], fenetre)
Settings = ElementGraphique(125, 520, bank['settings'], fenetre)
Shop = ElementGraphique(580, 520, bank['shop'], fenetre)

# ============= Son Menu =============
son_menu = pygame.mixer.Sound("./son Effect/Menu/Menu.wav")
# ============= Son Menu =============
# ============= Menu =============

# ============= Jeu =============
perso = Perso(0, 0, bank["perso"], fenetre, largeur, hauteur)
fondJeu = ElementGraphique(0, 0, bank["fond"], fenetre)
score = ElementGraphique(0, 0, bank["score"], fenetre)
tir_son = pygame.mixer.Sound("./son Effect/Menu/tir-son.wav")

lose_text = ElementGraphique(largeur/2 - 160, 95, bank["lose"], fenetre) #flag ****
# ============= Jeu =============

while continuer:
	horloge.tick(60)
	time += 1
	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE]:
		# state = "Menu"
		continuer = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False

	if state == "Intro":
		horloge.tick(10)
		loading.Afficher()
		barDeProgression.Afficher()
		if time == 50:
			state = "Menu"
			son_menu.play()

	if state == "Lose" :

		menu_fond.Afficher()
		interface.Afficher()
		lose_text.Afficher()    
		play_Bouton.Afficher()    
		exit_Bouton.Afficher()
		
# ============================ Mouse Gestion ============================
		select = pygame.Rect(xs, ys, 1, 1)

		select_collide_1(select, play_Bouton, pointeur1, exit_Bouton, pointeur2)
	
		for event in pygame.event.get() :
			if event.type == pygame.MOUSEMOTION :
				xs = event.pos[0]
				ys = event.pos[1]
				
			if select.colliderect(play_Bouton.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				boss = False
				time = 0
				perso.vie = 100
				perso.tirs = []
				enemys = []
				tabBonus = []
				explosions = []
				perso.kill = 0
				Enemy.Deplacer = Enemy.DescenteLinéaire
				son_menu.stop()
				state = "Jeu"
			
			if select.colliderect(exit_Bouton.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				continuer = False
# ============================ Mouse Gestion ============================

	if state == "Menu":
	
		horloge.tick(30)
		
		menu_fond.Afficher()
		interface.Afficher()
		text_presentation.Afficher()
		play_Bouton.Afficher()
		exit_Bouton.Afficher()
		Settings.Afficher()
		Shop.Afficher()
# ============================ Mouse Gestion ============================
		select = pygame.Rect(xs, ys, 1, 1)

		select_collide_1(select, play_Bouton, pointeur1, exit_Bouton, pointeur2)
		select_collide_2(select, pointeur_settings, Settings, pointeur_Shop, Shop)

		for event in pygame.event.get() :
			if event.type == pygame.MOUSEMOTION :
				xs = event.pos[0]
				ys = event.pos[1]
			if select.colliderect(play_Bouton.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				horloge.tick(60)
				son_menu.stop()
				state = "Jeu"
			
			if select.colliderect(exit_Bouton.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				continuer = False


	if state == "Jeu":
		
		state = perso.Alive()

		fondJeu.Afficher()
		# HUD.Afficher()

		if time % 333 == 0 and len(tabBonus) <= 1:
			New_Bonus(tabBonus, bank, fenetre, largeur, time)

		if time%250 == 0:
			cooldownEn -= 1

		if time%cooldownEn == 0 and not boss:
			New_Enemy(bank, enemys, largeur, hauteur, fenetre, time)

		if time % cooldownBoss == 0:
			boss = True
			New_Boss(bank, enemys, largeur, fenetre, time)

		if len(enemys) > 0 and boss and enemys[-1].vie <= 0 and enemys[-1].object == "Boss":
			boss = False

		if len(enemys) > 0:
			if enemys[-1].object == "Enemy" and boss:
				boss = False
		
		for enemy in enemys:

			enemy.tir(bank["tirsE"], fenetre, time)
			enemy.deplacerAfficherTirs()
			enemy.Deplacer()
			enemy.Afficher()
			enemy.Collisions(perso, enemy, time)
				
			for tir in perso.tirs:
				enemy.Collisions(tir, enemy, time)
			
			for tirE in enemy.tirs:
				tirE.Collisions(perso, perso, time)
				p, enemy.tirs = SupprTrucs(enemy.tirs, explosions, bank, fenetre)
			
			for explosion in explosions:
				explosion.Afficher()
				explosion.killExplode()
		
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
		perso.Tir(bank["tirsP"], touches, time, tir_son)
		x, enemys = SupprTrucs(enemys, explosions, bank, fenetre)
		p, perso.tirs = SupprTrucs(perso.tirs, explosions, bank, fenetre)
		p, tabBonus = SupprTrucs(tabBonus, explosions, bank, fenetre)
		p, explosions = SupprTrucs(explosions, explosions, bank, fenetre)
		
		perso.kill += x

		if perso.kill > 0:
			bank["kill"] = font_standart.render(str(perso.kill), 1, (255, 0, 0)).convert_alpha()
			kill = ElementGraphique(95, 0, bank["kill"], fenetre)
			kill.Afficher()

		score.Afficher()

	pygame.display.update()

pygame.quit()