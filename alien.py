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


	def update(self, setting):
		# 计算外星人准确的坐标
		self.x += setting.fleet_speed_factor * setting.fleet_direction
		self.y += setting.fleet_drop_speed_factor

		# 设置外星人位置
		self.rect.x = int(self.x)
		self.rect.y = int(self.y)
		

	def blitme(self):
		"""绘制外星人"""
		self.screen.blit(self.image, self.rect)


	def check_edges(self):
		"""检测外星人是否处于屏幕边缘"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True





