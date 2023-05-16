import pygame
import random

# 游戏窗口的大小
WIDTH = 800
HEIGHT = 600

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 初始化Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("枪战游戏")

# 加载玩家角色图像
player_img = pygame.image.load("player.png")
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

# 加载敌人图像
enemy_img = pygame.image.load("enemy.png")

# 创建子弹的类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# 创建敌人的类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 5)

# 创建精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 添加玩家角色到精灵组
player = pygame.sprite.Sprite()
player.image = player_img
player.rect = player_img.get_rect()
player.rect.centerx = WIDTH // 2
player.rect.bottom = HEIGHT - 10
all_sprites.add(player)

# 生成敌人
for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏循环
running = True
clock = pygame.time.Clock()

while running:
    # 控制游戏运行的帧率
    clock.tick(60)

    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 创建一颗子弹并将其添加到精灵组
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

# 获取键盘按键状态
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.rect.x -= 5
if keys[pygame.K_RIGHT]:
    player.rect.x += 5

# 更新所有精灵
all_sprites.update()

# 检测子弹是否击中敌人
hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
for hit in hits:
    # 生成新的敌人
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 检测敌人是否与玩家角色碰撞
hits = pygame.sprite.spritecollide(player, enemies, False)
if hits:
    running = False

# 清空屏幕
screen.fill(BLACK)

# 绘制所有精灵
all_sprites.draw(screen)

# 更新屏幕
pygame.display.flip()
pygame.quit()

