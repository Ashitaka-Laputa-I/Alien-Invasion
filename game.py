import sys
import pygame

from setting import Setting
from ship import Ship

import game_func


def run_game():
	pygame.init()

	game_setting = Setting()
	screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
	pygame.display.set_caption(game_setting.caption)

	# 创建一个飞船
	ship = Ship(screen)

	while True:
	 	# 监视键盘和鼠标事件
		game_func.check_events(ship)
	   			
		# 每次循环时都重绘屏幕,让最近绘制的屏幕可见
		game_func.update_screen(game_setting, screen, ship)


if __name__ == '__main__':
	run_game()