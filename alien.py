import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""外星人类"""
	def __init__(self, setting, screen):
		"""初始化"""
		# 继承Sprite类
		super().__init__()

		# 设置
		self.setting = setting

		# 屏幕
		self.screen = screen

		# 图像
		self.image = pygame.image.load('images/alien.bmp')

		# 外界矩阵
		self.rect = self.image.get_rect()

		# 位置
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 精确位置
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def update(self):
		pass	

	def blitme(self):
		"""绘制外星人"""
		self.screen.blit(self.image, self.rect)



