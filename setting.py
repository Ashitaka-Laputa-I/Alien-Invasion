class Setting(): 
   """存储《外星人入侵》的所有设置的类""" 

   def __init__(self): 
      """初始化游戏的设置""" 
      # 屏幕设置 
      self.screen_width = 720
      self.screen_height = 640
      self.bg_color = (230, 230, 230) 

      # 标题设置
      self.caption = 'Alien Invasion'

      # 飞船设置
      self.ship_speed_factor = 0.2
