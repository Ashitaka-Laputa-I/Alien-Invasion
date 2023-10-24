# TODO(创建 Pygame 窗口以及响应用户输入)

import sys
import pygame


def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))
	pygame.display.set_caption('Alien Invasion')

	while True:
	 	# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
	   			sys.exit() 
	 	# 让最近绘制的屏幕可见
		pygame.display.flip() 


if __name__ == '__main__':
	run_game()