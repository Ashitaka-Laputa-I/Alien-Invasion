# 永远不要半夜找BUG(已修复)

- 现象: 分数第一次就被乘上了倍数
- 猜想: speedup方法被意外调用了
- 原因: 第一次子弹碰撞检测时,外星人还未创建



# Scoreboard

- 增加分数板相应属性
- 增加update与blitme方法



# Game-Func

- 扩充update_screen函数
  - 增加对分数板的更新与绘制



# Game-Stats

- 增加分数属性



# Setting

- 增加相应属性

