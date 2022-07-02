import pygame

FPS = 60
COLOR = (255, 255, 255)
SIZE= (800, 600)

# 游戏初始化
pygame.init()
screen = pygame.display.set_mode(size=SIZE)    # 创建窗口
pygame.display.set_caption("游戏")          # 设置窗口标题
clock = pygame.time.Clock() # 设置时钟

# 游戏主循环
running = True
while running:
    clock.tick(FPS)    # 设置帧率(每秒刷新的次数)
    # 取得输入
    for event in pygame.event.get():    # 取得事件 pygame.event.get 是一个列表
        if event.type == pygame.QUIT:   # 如果点击关闭按钮，则退出游戏
            running = False # 关闭游戏
    # 更新游戏

    # 页面展示
    screen.fill(color=COLOR)
    pygame.display.update() # 更新屏幕

pygame.quit()   # 关闭游戏
