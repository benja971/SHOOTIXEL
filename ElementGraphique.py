class ElementGraphique():
	def __init__(self, img, fenetre, x=0, y=0):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = int(x)
		self.rect.y = int(y)
		self.fenetre = fenetre

	def afficher(self):
		self.fenetre.blit(self.image, self.rect)

	def collide(self, other):
		if self.rect.colliderect(other):
			return True
		return False
