import pygame.font

class Button():
	"""按钮"""
	def __init__(self, setting, screen, message):
		"""初始化"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# 按钮大小
		self.width = 150
		self.height = 40

		#按钮字体颜色
		self.button_color = (210, 210, 210)
		self.text_color = (255, 255, 255)

		# 字体与大小
		self.font = pygame.font.SysFont(None, 32)

		# 按钮位置
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# 按钮内容
		self._present_message(message)


	def draw_button(self):
		"""绘制按钮(包含内容)"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.message_image, self.message_image_rect)


	def _present_message(self, message):
		"""把message渲染为图像,在按钮中央显示"""
		self.message_image = self.font.render(message, True, self.text_color, self.button_color)
		self.message_image_rect = self.message_image.get_rect()
		self.message_image_rect.center = self.rect.center
