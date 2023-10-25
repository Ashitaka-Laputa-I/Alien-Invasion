# Ship

- 增加移动标志
- 增加updata方法,更新ship的x坐标
  - bug: 无法左移<已修复:原因在于centerx无法存储float数值>



# Game-Func

- 更新check_event方法,支持对KEY的检查,并且增加参数使用:ship
- 更改check_event方法,使ship移动化为A/D键