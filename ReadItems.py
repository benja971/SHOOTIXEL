import pygame


def loadImage():
    images = {}
    images['avant-plan'] = pygame.image.load("images/avant-plan.png").convert()
    images['fond_niveau1'] = pygame.image.load("images/bg.png").convert()
    images['perso'] = pygame.image.load("images/DurrrSpaceShip.png").convert_alpha()
    images['balle'] = pygame.image.load("images/1.png").convert_alpha()
    images['Main'] = pygame.image.load("images/BgM.jpg").convert_alpha()
    images['Vie25'] = pygame.image.load("images/Life25.png").convert_alpha()
    images['Vie50'] = pygame.image.load("images/Life50.png").convert_alpha()
    images['Vie75'] = pygame.image.load("images/Life75.png").convert_alpha()
    images['Vie100'] = pygame.image.load("images/Life100.png").convert_alpha()
    images['Play'] = pygame.image.load("images/Play.png").convert_alpha()
    images['Option'] = pygame.image.load("images/Option.png").convert_alpha()
    images['Exit'] = pygame.image.load("images/Exit.png").convert_alpha()
    images['pointeur'] = pygame.image.load( "images/Pointeur.png").convert_alpha()
    images['list_bonus'] = pygame.image.load("images/boost.png").convert_alpha()
    images['uplife'] = pygame.image.load("images/UpLife.png").convert_alpha()


    font = pygame.font.Font('Text/Kemco Pixel Bold.ttf', 70)
    font_Intro = pygame.font.Font('Text/Kemco Pixel Bold.ttf', 30)
    images['Text'] = font.render('DarkSpace2', True, (255, 255, 255))
    images['Text_avant_plan'] = font_Intro.render('Obersian presents...', True, (255, 255, 255))

    images["PersoAnimee"] = []
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi1.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi2.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi3.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi4.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi5.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi6.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi7.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi8.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi9.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi10.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi11.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi12.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi13.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi14.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi15.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi16.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi17.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi18.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi19.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi20.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi21.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi22.png").convert_alpha())
    images["PersoAnimee"].append(pygame.image.load("images/Enemy/ennemi23.png").convert_alpha())

    

    return images
