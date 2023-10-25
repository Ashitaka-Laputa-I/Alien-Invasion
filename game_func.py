import sys
import pygame


def check_events(ship):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		# 检测退出键
		if event.type == pygame.QUIT:
			sys.exit()

		# 检测左右键	
		elif event.type == pygame.KEYDOWN: 
			_check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP: 
			_check_keyup_events(event, ship)


def update_screen(setting, screen, ship):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(setting.bg_color)
	ship.update(setting)
	ship.blitme()

	# 让最近绘制的屏幕可见 
	pygame.display.flip()


def _check_keydown_events(event, ship):
	"""检测键盘按下事件(物理上D键优先于A键)"""
	if event.key == pygame.K_d: 
		ship.moving_right = True 
	elif event.key == pygame.K_a: 
		ship.moving_left = True 


def _check_keyup_events(event, ship):
	"""检测键盘松开事件(物理上D键优先于A键)"""
	if event.key == pygame.K_d: 
		ship.moving_right = False 
	elif event.key == pygame.K_a: 
		ship.moving_left = False 