import sys
import pygame
import time

from bullet import Bullet
from alien import Alien


def check_events(setting, stats, screen, ship, bullets, aliens, button):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		# 检测退出键
		if event.type == pygame.QUIT:
			sys.exit()

		# 检测鼠标点击
		elif event.type == pygame.MOUSEBUTTONDOWN:
			_check_mousedown_events(setting, stats, ship, bullets, aliens, button)

		# 检测左右与空格键	
		elif event.type == pygame.KEYDOWN: 
			_check_keydown_events(setting, screen, ship, bullets, event)
		elif event.type == pygame.KEYUP: 
			_check_keyup_events(ship, event)


def update_screen(setting, stats, screen, ship, bullets, aliens, button, scoreboard):
	"""更新屏幕中的元素(先绘制屏幕,再绘制子弹,再绘制飞船,再显示)"""
	
	if stats.game_active:
		# 屏幕填充背景
		screen.fill(setting.bg_color)
		
		# 更新得分板,并且绘制在屏幕上
		_update_scoreboard(scoreboard)
		# 更新飞船位置,并且绘制在屏幕上
		_update_ship(ship)
		# 更新外星人群位置,并且绘制在以上屏幕上
		_update_aliens(setting, stats, screen, ship, bullets, aliens)
		# 更新子弹位置,并且绘制在以上屏幕上
		_update_bullets(setting, stats, screen, ship, bullets, aliens, scoreboard)


	if not stats.game_active: 
		# 绘制按钮
		button.draw_button()
	# 将屏幕打印在窗口里
	pygame.display.flip()


def create_fleet(setting, screen, ship, aliens):
	""""创建外星人群"""
	# 获取外星人创建的行列容量
	alien = Alien(setting, screen)
	number_row = _get_number_aliens_row(alien, ship) 
	number_clown = _get_number_aliens_clown(alien)

	# 将外星人初始化,并且加入外星人群中
	for row_number in range(number_row):
		for clown_number in range(number_clown):
			_create_alien(setting, screen, aliens, clown_number, row_number)


def _check_mousedown_events(setting, stats, ship, bullets, aliens, button):
	"""检测鼠标点击按钮"""
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		# 隐藏光标
		pygame.mouse.set_visible(False)
		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		# 重置游戏参数
		setting.initialize_dynamic_setting()
		# 清空外星人与子弹
		aliens.empty()
		bullets.empty()
		# 创建外星人,初始化废飞船


def _check_keydown_events(setting, screen, ship, bullets, event):
	"""检测键盘按下事件(物理上D键优先于A键)"""
	if event.key == pygame.K_d: 
		ship.moving_right = True 
	elif event.key == pygame.K_a: 
		ship.moving_left = True 
	elif event.key == pygame.K_SPACE:
		_fire_bullet(setting, screen, ship, bullets)


def _check_keyup_events(ship, event):
	"""检测键盘松开事件(物理上D键优先于A键)"""
	if event.key == pygame.K_d: 
		ship.moving_right = False 
	elif event.key == pygame.K_a: 
		ship.moving_left = False 


def _update_ship(ship):
	# 更新飞船位置
	ship.update()

	# 绘制飞船
	ship.blitme()


def _update_bullets(setting, stats, screen, ship, bullets, aliens, scoreboard):
	# 更新子弹位置
	bullets.update()

	# 删除飞出边缘子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	_check_bullet_alien_collision(setting, stats, screen, ship, bullets, aliens, scoreboard)

	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()


def _update_aliens(setting, stats, screen, ship, bullets,  aliens):
	# 检测外星人是否触碰屏幕边缘,并且由此更改方向
	_check_fleet_edges(setting, aliens)

	# 更新外星人位置
	aliens.update(setting)


	# 检测外星人与飞船是否碰撞:
	if pygame.sprite.spritecollideany(ship, aliens):
		_you_die(setting, stats, screen, ship, bullets, aliens)

	# 检测外星人是否到达了底端:
	_check_fleet_bottom(setting, stats, screen, ship, bullets, aliens)

	# 绘制外星人
	for alien in aliens.sprites():
		alien.blitme()

def _update_scoreboard(scoreboard):
	scoreboard.blitme()


def _get_number_aliens_clown(alien):
	available_space_x = alien.setting.screen_width - 2 * alien.rect.width
	number_clown = int(available_space_x / (2 * alien.rect.width))

	return number_clown


def _get_number_aliens_row(alien, ship):
	available_space_y = (alien.setting.screen_height - (3 * alien.rect.height) - 1.5 * ship.rect.height)
	number_row = int(available_space_y / (2 * alien.rect.height))

	return number_row


def _create_alien(setting, screen, aliens, clown, row):
	# 初始化外星人
	alien = Alien(setting, screen)

	# 设置外星人精确位置
	alien.x = alien.rect.width + 2 * alien.rect.width * clown
	alien.y = alien.rect.height + 2 * alien.rect.height * row

	#设置外星人位置
	alien.rect.x = int(alien.x)
	alien.rect.y = int(alien.y)

	# 添加至外星人组
	aliens.add(alien)


def _check_fleet_edges(setting, aliens):
	"""当有外星人到达边缘时切换外星人群水平移动方向"""
	for alien in aliens.sprites():
		if alien.check_edges():
			setting.fleet_direction *= -1
			break


def _check_fleet_bottom(setting, stats, screen, ship, bullets, aliens):
	"""检测外星人是否到达屏幕底端"""
	screen_rect = screen.get_rect()

	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			_you_die(setting, stats, screen, ship, bullets, aliens)
			break


def _you_die(setting, stats, screen, ship, bullets, aliens):
	"""响应外星人撞到飞船"""
	# 飞船剩余量减一
	stats.ship_left -= 1
	# 飞船剩余量为0而再"死"则Game-Over
	if stats.ship_left <= 0:
		stats.game_active = False
		pygame.mouse.set_visible(True)
	else:
		# 清空外星人与子弹
		aliens.empty()
		bullets.empty()

		# 创建新的外星人群, 并且将飞船初始化
		create_fleet(setting, screen, ship, aliens)
		ship.center_it()

		# 暂停1s
		time.sleep(1)


def _fire_bullet(setting, screen, ship, bullets):
	"""创建一枚子弹,并且加入子弹组中"""
	if len(bullets) < setting.bullets_allowed:
		new_bullet = Bullet(setting, screen, ship)
		bullets.add(new_bullet)


def _check_bullet_alien_collision(setting, stats, screen, ship, bullets, aliens, scoreboard):
	# 检测子弹是否击中外星人,如此删除对应子弹与外星人
	collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collision:
		for alien in collision.values():
			stats.score += setting.alien_points
			scoreboard.update()

	if len(aliens) == 0:
		bullets.empty()
		create_fleet(setting, screen, ship, aliens)
		
		if collision:
			setting.increase_speed()