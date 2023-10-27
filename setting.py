class Setting(): 
   """存储《外星人入侵》的所有设置的类""" 

   def __init__(self): 
      """初始化游戏的设置""" 
      # 屏幕设置 
      self.screen_width = 960-64
      self.screen_height = 960

      # 颜色设置
      self.bg_color = (230, 230, 230) 

      # 标题设置
      self.caption = 'Alien Invasion'

      # 飞船设置
      self.ship_limit = 3

      # 子弹设置
      self.bullet_width = 3
      self.bullet_height = 15
      self.bullet_color = (60, 60, 60)
      self.bullets_allowed = 30

      # 加倍设置
      self.speedup_scale = 1.08
      self.speedup_scale_only_for_drop = 1.02
      self.points_scale = 2

      # 初始化速度
      self.initialize_dynamic_setting()


   def increase_speed(self):
      """提升速度"""
      self.ship_speed_factor *= self.speedup_scale
      self.bullet_speed_factor *= self.speedup_scale
      self.fleet_speed_factor *= self.speedup_scale
      self.fleet_drop_speed_factor *= self.speedup_scale_only_for_drop
      self.alien_points = int(self.alien_points * self.points_scale)


   def initialize_dynamic_setting(self):
      """初始化随游戏进行而变化的设置"""
      # 飞船速度
      self.ship_speed_factor = 0.25
      # 子弹速度
      self.bullet_speed_factor = 0.45
      # 外星人水平速度
      self.fleet_speed_factor = 0.4
      # 外星人垂直速度
      self.fleet_drop_speed_factor = 0.03
      # 外星人方向
      self.fleet_direction = 1
      # 外星人击杀得分
      self.alien_points = 50






