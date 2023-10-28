import sys
import pygame
from pygame.sprite import Group

from setting import Setting
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_func

def run_game():
	# 初始化pygame
	pygame.init()

	# 创建设置
	game_setting = Setting()

	# 创建信息
	game_stats = GameStats(game_setting)

	# 创建屏幕并添加标题
	game_screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
	pygame.display.set_caption(game_setting.caption)

	# 创建按钮
	game_button = Button(game_setting, game_screen, 'Play')

	# 创建一个飞船
	game_ship = Ship(game_setting, game_screen)

	# 创建一组子弹
	game_bullets = Group()

	# 创建一群外星组
	game_aliens = Group()
	game_func.create_fleet(game_setting, game_screen, game_ship, game_aliens)

	# 创建得分板
	game_scoreboard = Scoreboard(game_setting, game_stats, game_screen)		

	while True:
	 	# 监视键盘和鼠标事件
		game_func.check_events(game_setting, game_stats, game_screen, game_ship, game_bullets, game_aliens, game_button, game_scoreboard)

		# 每次循环时都重绘屏幕,让最近绘制的屏幕可见
		game_func.update_screen(game_setting, game_stats, game_screen, game_ship, game_bullets, game_aliens, game_button, game_scoreboard)


if __name__ == '__main__':
	run_game()