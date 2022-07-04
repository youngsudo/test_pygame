import pygame

# 背景
FPS = 60    # 帧率
BCK = (255, 255, 255) # 背景色
BCKWIDTH = 500      # 背景宽度
BCKHEIGHT = 600     # 背景高度

# player
PLAYERSIZE = (50, 40)   # 玩家大小
PLAYERCOLOR = (255, 0, 0)   # 玩家颜色

# 游戏初始化
pygame.init()
screen = pygame.display.set_mode(size=(BCKWIDTH,BCKHEIGHT))    # 创建窗口
pygame.display.set_caption("游戏")          # 设置窗口标题
clock = pygame.time.Clock() # 设置时钟

class Player(pygame.sprite.Sprite): # 玩家类
    def __init__(self): # 初始化
        super().__init__()  # 调用父类的构造函数
        self.image = pygame.Surface(PLAYERSIZE)   # 创建精灵图片
        self.image.fill(PLAYERCOLOR)    # 填充颜色
        self.rect = self.image.get_rect()   # 获取矩形
        # self.rect.x = 200 # 设置矩形的x坐标
        # self.rect.y = 200 # 设置矩形的y坐标
        self.rect.center = (BCKWIDTH/2, BCKHEIGHT/2)   # 设置矩形的中心位置
        # self.speed = [0, 0] # 设置移动速度
    def update(self):
        self.rect.x += 2
        if self.rect.left > BCKWIDTH:   # 判断是否超出边界
            self.rect.right = 0         # 如果超出边界，则重新回到边界

all_sprites = pygame.sprite.Group() # 创建精灵组
player = Player() # 创建玩家
all_sprites.add(player) # 添加玩家到精灵组

# 游戏主循环
running = True
while running:
    clock.tick(FPS)    # 设置帧率(每秒刷新的次数)
    # 取得输入
    for event in pygame.event.get():    # 取得事件 pygame.event.get 是一个列表
        if event.type == pygame.QUIT:   # 如果点击关闭按钮，则退出游戏
            running = False # 关闭游戏
    # 更新游戏
    all_sprites.update()    # 执行这个all_sprites群组的update方法

    # 页面展示
    screen.fill(color=BCK)
    all_sprites.draw(screen) # 绘制精灵
    pygame.display.update() # 更新屏幕

pygame.quit()   # 关闭游戏