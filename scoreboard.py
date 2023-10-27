import pygame.font


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

		# 初始化得分图像
		self.update()


	def blitme(self):
		"""在屏幕上显示分数"""
		self.screen.blit(self.score_image, self.score_rect)


	def update(self):
		"""将得分信息渲染成图像"""
		# 获取分数的字符串形式
		score_str = str(self.stats.score)
		# 转化为图像
		self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
		# 设置得分信息的位置(右上角)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20


