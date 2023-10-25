# TODO(创建 Pygame 窗口以及响应用户输入)

import sys
import pygame

from setting import Setting
from ship import Ship


def run_game():
	pygame.init()

	game_setting = Setting()
	screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
	pygame.display.set_caption(game_setting.caption)

	# 创建一个飞船
	ship = Ship(screen)

	while True:
	 	# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
	   			sys.exit() 
	   			
		# 每次循环时都重绘屏幕 
		screen.fill(game_setting.bg_color)
		ship.blitme()

	 	# 让最近绘制的屏幕可见
		pygame.display.flip() 


if __name__ == '__main__':
	run_game()