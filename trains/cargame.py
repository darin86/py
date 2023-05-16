import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义屏幕尺寸和颜色
screen_width = 800
screen_height = 600
bg_color = (255, 255, 255)

# 定义小车尺寸和颜色
car_width = 50
car_height = 100
car_color = (0, 0, 0)

# 定义障碍物尺寸和颜色
obstacle_width = 100
obstacle_height = 100
obstacle_color = (255, 0, 0)

# 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("赛车游戏")

clock = pygame.time.Clock()

def draw_car(x, y):
    pygame.draw.rect(screen, car_color, (x, y, car_width, car_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, obstacle_color, (x, y, obstacle_width, obstacle_height))

def game_loop():
    # 初始小车位置
    car_x = screen_width // 2 - car_width // 2
    car_y = screen_height - car_height - 10

    # 初始障碍物位置
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = -obstacle_height

    # 小车的移动速度
    car_speed = 6

    # 游戏结束标志
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed

        # 清空屏幕
        screen.fill(bg_color)

        # 更新障碍物位置
        obstacle_y += car_speed
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height

        # 检测碰撞
        if car_y < obstacle_y + obstacle_height:
            if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x:
                game_over = True

        # 绘制小车和障碍物
        draw_car(car_x, car_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # 刷新屏幕
        pygame.display.update()
        clock.tick(60)  # 限制帧率

game_loop()
