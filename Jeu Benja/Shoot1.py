import pygame
import os
from random import randint
from Class import *
from Fonctions import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

largeur, hauteur = 600, 900
fenetre = pygame.display.set_mode((largeur, hauteur))
bank = images()
fond = ElementGraphique(bank["fond"], 0, 0)
vaisseau = Perso(bank["vaisseau"], 0, 0, largeur, hauteur)

balles = []
tirs = []

i = 0
continuer = True
state = "jeu"
horloge = pygame.time.Clock()

vbmin, vbmax = 4, 6
delais = 50

while continuer:
    horloge.tick(30)
    i += 1
    touches = pygame.key.get_pressed()

    if touches[pygame.K_ESCAPE]:
        continuer = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    if state == "jeu":
        fond.Afficher(fenetre)
        vaisseau.Afficher(fenetre)
        vaisseau.Deplacer(touches, largeur)

        vbmin, vbmax = SpeedUp(i, vbmin, vbmax)

        if i % 50 == 0:
            delais -= 1

        if i % delais == 0:
            for i in range(randint(1, 4)):
                New_Balle(bank, balles, largeur, hauteur, vbmin, vbmax)

        for balle in balles:
            balle.Afficher(fenetre)
            balle.DeplacerE()
            vaisseau.Collisions(balle, balles)

        for tir in tirs:
            tir.Afficher(fenetre)
            print("test")
            tir.DeplacerT()

        if touches[pygame.K_SPACE]:
            vaisseau.NewTir(bank, tirs, vaisseau)

    pygame.display.update()

pygame.quit()
