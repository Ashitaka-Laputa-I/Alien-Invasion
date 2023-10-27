class Setting(): 
   """存储《外星人入侵》的所有设置的类""" 

   def __init__(self): 
      """初始化游戏的设置""" 
      # 屏幕设置 
      self.screen_width = 960-64
      self.screen_height = 960
      self.bg_color = (230, 230, 230) 

      # 标题设置
      self.caption = 'Alien Invasion'

      # 飞船设置
      self.ship_speed_factor = 0.25
      self.ship_limit = 3

      # 子弹设置
      self.bullet_speed_factor = 0.45
      self.bullet_width = 3000
      self.bullet_height = 15
      self.bullet_color = (60, 60, 60)
      self.bullets_allowed = 3

      # 星人设置
      self.fleet_speed_factor = 0.4
      self.fleet_drop_speed_factor = 0.03
      self.fleet_direction = 1 # 移动方向<1右移:-1左移>

