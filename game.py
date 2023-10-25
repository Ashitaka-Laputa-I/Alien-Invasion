# TODO(设置背景色)

import sys
import pygame


def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))
	pygame.display.set_caption('Alien Invasion')

	# 设置背景色(灰色) 
	bg_color = (230, 230, 230) 

	while True:
	 	# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
	   			sys.exit() 
	   			
		# 每次循环时都重绘屏幕 
		screen.fill(bg_color) 

		# 让最近绘制的屏幕可见
		pygame.display.flip()


if __name__ == '__main__':
	run_game()