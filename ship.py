import pygame

class Ship():
    """飞船类"""
    
    def __init__(self, setting, screen):
        """初始化(设置, 屏幕)"""
        # 设置
        self.setting = setting

        # 屏幕
        self.screen = screen

        # 屏幕外接矩阵
        self.screen_rect = self.screen.get_rect()  

        # 图像
        self.image = pygame.image.load('images/ship.bmp')

        # 图像外接矩阵
        self.rect = self.image.get_rect()

        # 图像位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船移动标志位
        self.moving_right = False
        self.moving_left = False

        # 飞船速度
        self.speed = setting.ship_speed_factor
        
        #飞船精确位置
        self.center = float(self.rect.centerx)


    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.center += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left: 
            self.center -= self.speed

        self.rect.centerx = int(self.center)


    def blitme(self):
        """在屏幕midbottom位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        # 在屏幕的midbottom位置绘制飞船图像
