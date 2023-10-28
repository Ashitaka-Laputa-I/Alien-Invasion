class GameStats():
	"""游戏统计信息"""
	def __init__(self, setting):
		"""初始化"""
		self.setting = setting
		self.reset_stats()

		# 游戏运行标志
		self.game_active = False

		# 游戏最高分
		self.high_score = 0

		# 游戏难度等级
		self.level = 1


	def reset_stats(self):
		"""初始化游戏统计信息"""
		# 飞船剩余数量
		self.ship_left = self.setting.ship_limit
		# 得分
		self.score = 0
		