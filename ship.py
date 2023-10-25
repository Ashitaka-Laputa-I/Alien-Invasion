import pygame

class Ship():
    """飞船类"""
    
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在屏幕midbottom位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        # 在屏幕的midbottom位置绘制飞船图像
