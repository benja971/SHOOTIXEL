import pygame
from random import choice, randint
from math import cos, sin


class ElementGraphique:
    """
    Tout est élément graphique
    """

    def __init__(self, x, y, img, fenetre):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fenetre = fenetre

    def Collide(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False

    def Collisions(self, other, perso, time):
        """
        Fonction que gère lorsqu'un élément en touche un autre
        """
        if self.Collide(other):

            if self.object == "Enemy" or self.object == "Boss":
                if other.object == "TirPerso":
                    self.TakeDamages(other)
                    other.Kill()

                elif other.object == "Perso":
                    self.Kill()
                    if other.invinsible == False:
                        other.TakeDamages(self)

            if self.object == "Bonus":
                if other.object == "TirPerso":
                    other.Kill()
                    self.Kill()
                    self.apllyBonus(perso, time)

    def TakeDamages(self, other):
        """
        Fonction qui retire de la vie à un élément en cas de collision
        """
        self.vie -= other.degats

    def Kill(self):
        """
        Fonction qui tue un élément
        """
        self.vie = 0

    def Afficher(self):
        self.fenetre.blit(self.image, self.rect)


class ElementGraphiqueAnimé(ElementGraphique):
    """
    Animation des Elements Graphiques
    """

    def __init__(self, x, y, img, fenetre):
        super().__init__(x, y, img[0], fenetre)
        self.images = img
        self.timer = 0
        self.numAnim = 0

    def Afficher(self):
        self.timer += 1
        if self.timer > 10:
            self.timer = 0
            self.numAnim += 1
            if self.numAnim >= len(self.images):
                self.numAnim = 0
            self.image = self.images[self.numAnim]

        super().Afficher()


class ElementAnimeDir(ElementGraphiqueAnimé):
    def __init__(self, x, y, images_all_dir, fenetre):
        super().__init__(x, y, images_all_dir["Standing"], fenetre)
        self.images_all_dir = images_all_dir
        self.direction = "Standing"
        self.old_direction = "Standing"

    def Afficher(self):
        if self.old_direction != self.direction:
            self.images = self.images_all_dir[self.direction]
            self.numAnim = 0
            self.old_direction = self.direction

        super().Afficher()


class Perso(ElementAnimeDir):
    """
    Personnage qu'incarne le joueur
    """

    def __init__(self, x, y, images_all_dir, fenetre, largeur, hauteur):
        super().__init__(x, y, images_all_dir, fenetre)
        self.object = "Perso"
        self.rect.x = largeur // 2 - self.rect.w // 2
        # self.rect.y = 250
        self.rect.y = hauteur - self.rect.h - 20
        self.tirs = []
        self.vie = 100
        self.vitesse = 4
        self.cooldown = 30
        self.money = 0
        self.kill = 0
        self.boosted = False
        self.speed = False
        self.invinsible = False
        self.plusVie = False
        self.plusdamges = False
        self.bcooldown = False

    def Deplacer(self, touches, largeur):
        self.direction = "Standing"
        self.numAnim = 0

        if touches[pygame.K_d] and self.rect.x <= largeur - self.rect.w:
            self.rect.x += self.vitesse
            self.direction = "Right"

        if touches[pygame.K_a] and self.rect.x >= 150:
            self.rect.x -= self.vitesse
            self.direction = "Left"

# Second set game

        if touches[pygame.K_RIGHT] and self.rect.x <= largeur - self.rect.w:
            self.rect.x += self.vitesse
            self.direction = "Right"

        if touches[pygame.K_LEFT] and self.rect.x >= 150:
            self.rect.x -= self.vitesse
            self.direction = "Left"

    def Tir(self, img, touches, i, son_tir):
        if touches[pygame.K_SPACE] and i % self.cooldown == 0:
            self.tirs.append(Tir(self.rect.x - 12 + self.rect.w//2,
                                 self.rect.y - 30, img, self.fenetre, 7, 15, self, "TirPerso"))
            son_tir.play()

    def Alive(self):
        """
        """
        if self.vie <= 0:
            print("Perdu")

    def speedUp(self):
        """
        """
        self.vitesse += 4
        self.speed = True

    def godMod(self):
        """
        """
        self.invinsible = True

    def heal(self):
        """
        """
        self.vie += 10

    def normalSpeed(self):
        """
        """
        self.vitesse -= 4
        self.speed = False

    def normalMod(self):
        """
        """
        self.invinsible = False

    def mitraille(self):
        """
        """
        if self.boosted == False:
            self.boosted = True
            self.cooldown /= 2
            self.bcooldown = True

    def noMitraille(self):
        """
        """
        if self.boosted == True:
            self.boosted = False
            self.cooldown *= 2
            self.bcooldown = False


class Enemy(ElementGraphiqueAnimé):
    """
    Ennemis animés arrivant en face du personnage
    """

    def __init__(self, x, y, img, fenetre, pv, v, d, largeur, objext, ptir):
        super().__init__(x, y, img, fenetre)
        self.vie = pv
        self.vitesse = v
        self.degats = d
        self.t = 0
        self.object = objext
        self.trucy = randint(-10, 0)
        self.truc2 = randint(200, largeur - 50)
        self.Deplacer = self.DescenteLinéaire
        self.cooldown = 100
        self.peutire = ptir
        self.tirs = []

    def Choix(self, i):
        """
        Déplacements
        """
        if 1000 < i < 2500:
            self.Deplacer = choice(
                [self.DescenteLinéaire, self.DescenteEnCercles])
        elif 2501 < i:
            self.Deplacer = choice(
                [self.DescenteLinéaire, self.DescenteEnCercles, self.DescenteSinusoïdale])

    def DescenteLinéaire(self):
        """
        Les ennemis descendent en ligne droite
        """
        self.rect.y += self.vitesse

    def DescenteEnCercles(self):
        """
        Les ennemis descendent en faisant des cercles de tailles différentes
        """
        self.t += 1
        self.rect.x = 50*cos(self.t/20) + self.truc2
        self.rect.y = 50*sin(self.t/20) + self.trucy + self.t

    def DescenteSinusoïdale(self):
        """
        Les ennemis descendent en suivant des trajectoires sinusoîdales
        """
        self.t += 1
        self.rect.x = 200*cos(self.t/20) + 300
        self.rect.y = self.t

    def tir(self, img, fenetre, i):
        """
        """
        if self.peutire and i % self.cooldown == 0:
            self.tirs.append(Tir(self.rect.x + self.rect.w//2, self.rect.y +
                                 self.rect.h + 10, img, fenetre, -5, 15, self, "TirEnnemy"))

    def deplacerAfficherTirs(self):
        """
        """
        for tir in self.tirs:
            tir.Deplacer()
            tir.Afficher()


class Tir(ElementGraphiqueAnimé):
    """
    Tirs
    """

    def __init__(self, x, y, img, fenetre, v, d, pere, o):
        super().__init__(x, y, img, fenetre)
        self.object = o
        self.vitesse = v
        self.degats = d
        self.vie = 1
        self.pere = pere
        self.boosted = False

    def Deplacer(self):
        """
        Fonction qui gère le déplacement des tirs du Perso
        """
        self.rect.y -= self.vitesse

    def normalDamages(self):
        if self.boosted == True:
            self.pere.plusdamges = False
            self.boosted = False
            self.degats = 15

    def damagesUp(self):
        if self.boosted == False:
            self.boosted = True
            self.pere.plusdamges = True
            self.degats += 5


class Bonus(ElementGraphique):
    def __init__(self, x, y, img, fenetre, t, time):
        super(Bonus, self).__init__(x, y, img, fenetre)
        self.vx = choice([-5, 5])
        self.vy = choice([-5, 5])
        self.object = "Bonus"
        self.name = t
        self.vie = 1
        self.apparition = time
        self.debBonus = 0

    def Deplacer(self, largeur, hauteur):
        self.rect.x += self.vx
        if self.rect.x > largeur - self.rect.w:
            self.vx = -abs(self.vx)
        if self.rect.x < 150:
            self.vx = abs(self.vx)

        self.rect.y += self.vy
        if self.rect.y > hauteur - self.rect.h:
            self.vy = -abs(self.vy)
        if self.rect.y < 150:
            self.vy = abs(self.vy)

    def alive(self, time):
        if time - self.apparition >= 250:
            self.Kill()

    def apllyBonus(self, perso, time):
        """
        """
        self.debBonus = time
        if self.name == "speed":
            perso.speedUp()
        if self.name == "shield":
            perso.godMod()
        if self.name == "cooldown":
            perso.mitraille()
        if self.name == "damages":
            perso.plusdamges = True
        if self.name == "heal":
            perso.heal()

    def resetBonus(self, perso, time):
        """
        """
        if time - self.debBonus >= 100:
            if self.name == "speed" and perso.speed:
                perso.normalSpeed()
            if self.name == "shield" and perso.godMod:
                perso.normalMod()
            if self.name == "cooldown":
                perso.noMitraille()
