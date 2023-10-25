import sys
import pygame

from bullet import Bullet


def check_events(setting, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		# 检测退出键
		if event.type == pygame.QUIT:
			sys.exit()

		# 检测左右键	
		elif event.type == pygame.KEYDOWN: 
			_check_keydown_events(event, setting, screen, ship, bullets)
		elif event.type == pygame.KEYUP: 
			_check_keyup_events(event, ship)


def update_screen(setting, screen, ship, bullets):
	"""更新屏幕中的元素(先绘制屏幕,再绘制子弹,再绘制飞船,再显示)"""
	screen.fill(setting.bg_color)
	_update_bullets(bullets)
	_update_ship(setting, ship)
	pygame.display.flip()


def _check_keydown_events(event, setting, screen, ship, bullets):
	"""检测键盘按下事件(物理上D键优先于A键)"""
	if event.key == pygame.K_d: 
		ship.moving_right = True 
	elif event.key == pygame.K_a: 
		ship.moving_left = True 
	elif event.key == pygame.K_SPACE:
		_fire_bullet(setting, screen, ship, bullets)


def _check_keyup_events(event, ship):
	"""检测键盘松开事件(物理上D键优先于A键)"""
	if event.key == pygame.K_d: 
		ship.moving_right = False 
	elif event.key == pygame.K_a: 
		ship.moving_left = False 


def _update_bullets(bullets):
	# 更新子弹位置
	bullets.update()

	# 删除飞出边缘子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()


def _update_ship(setting, ship):
	# 更新飞船位置
	ship.update(setting)

	# 绘制飞船
	ship.blitme()


def _fire_bullet(setting, screen, ship, bullets):
	# 创建一枚子弹,并且加入子弹组中
	if len(bullets) < setting.bullets_allowed:
		new_bullet = Bullet(setting, screen, ship)
		bullets.add(new_bullet)