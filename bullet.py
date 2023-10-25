import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""子弹类"""

	def __init__(self, setting, screen, ship):
		"""初始化"""
		# 继承Sprite类
		super().__init__()

		# 屏幕
		self.screen = screen

		# 外接矩阵
		self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)

		# 位置
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 精确位置
		self.y = float(self.rect.y)

		# 颜色
		self.color = setting.bullet_color

		# 速度
		self.speed = setting.bullet_speed_factor

	def update(self):
		"""更新子弹位置"""
		self.y -= self.speed
		self.rect.y = int(self.y)


	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)