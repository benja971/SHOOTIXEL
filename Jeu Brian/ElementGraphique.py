class ElementGraphique():
	def __init__(self, img, fenetre, x, y):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.fenetre = fenetre

	def afficher(self):
		self.fenetre.blit(self.image, self.rect)

