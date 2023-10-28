import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
	"""显示得分信息的类"""
	def __init__(self, setting, stats, screen):
		"""初始化"""
		# 设置
		self.setting = setting

		# 状态
		self.stats = stats

		# 屏幕
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# 显示得分信息的字体
		self.text_color = (20, 20, 20)
		self.font = pygame.font.SysFont(None, 32)

		# 初始化计分板图像
		self.score_update()
		self.high_score_update()
		self.level_update()
		self.ship_update()


	def blitme(self):
		"""在屏幕上显示分数与最高分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)


	def score_update(self):
		"""将得分信息渲染成图像"""
		# 规整化分数
		rounded_score = int(round(self.stats.score, -1))
		# 获取规整化后分数的字符形式
		score_str = "{:,}".format(rounded_score)
		# 转化为图像
		self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
		# 设置得分信息的位置(右上角)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20


	def high_score_update(self):
		"""将最高分渲染成图像"""
		# 规整化最高分
		high_score = int(round(self.stats.high_score))
		# 获取规整化字符串
		high_score_str = "{:,}".format(high_score)
		# 转化为图像
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.setting.bg_color)
		# 设置最高分的显示位置(中顶)
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top 


	def level_update(self):
		"""将游戏等级渲染成图像"""
		# 转化为图像
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, self.setting.bg_color)

		# 设置等级显示位置(得分的下方)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10


	def ship_update(self):
		"""更新剩余飞船图像"""
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.setting, self.screen)
			ship.rect.x = 10 + 10 * ship_number + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)






