import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义屏幕尺寸和颜色
screen_width = 600
screen_height = 400
bg_color = (0, 0, 0)

# 定义蛇和食物的尺寸和颜色
snake_size = 20
snake_color = (0, 255, 0)
food_size = 20
food_color = (255, 0, 0)

# 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("贪吃蛇")

clock = pygame.time.Clock()

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, snake_color, (block[0], block[1], snake_size, snake_size))

def draw_food(food_x, food_y):
    pygame.draw.rect(screen, food_color, (food_x, food_y, food_size, food_size))

def game_loop():
    # 初始化蛇的位置和速度
    snake_x = screen_width // 2
    snake_y = screen_height // 2
    snake_speed_x = 0
    snake_speed_y = 0

    # 初始化蛇的身体
    snake_body = []
    snake_length = 1

    # 初始化食物位置
    food_x = random.randint(0, (screen_width - food_size) // food_size) * food_size
    food_y = random.randint(0, (screen_height - food_size) // food_size) * food_size

    # 游戏结束标志
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_speed_x != snake_size:
                    snake_speed_x = -snake_size
                    snake_speed_y = 0
                elif event.key == pygame.K_RIGHT and snake_speed_x != -snake_size:
                    snake_speed_x = snake_size
                    snake_speed_y = 0
                elif event.key == pygame.K_UP and snake_speed_y != snake_size:
                    snake_speed_x = 0
                    snake_speed_y = -snake_size
                elif event.key == pygame.K_DOWN and snake_speed_y != -snake_size:
                    snake_speed_x = 0
                    snake_speed_y = snake_size

        # 更新蛇的位置
        snake_x += snake_speed_x
        snake_y += snake_speed_y

        # 边界检测
        if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
            game_over = True

        # 更新蛇的身体
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # 检测蛇是否吃到
    # 检测蛇是否撞到自己
    for block in snake_body[:-1]:
        if block[0] == snake_x and block[1] == snake_y:
            game_over = True

    # 清空屏幕
    screen.fill(bg_color)

    # 绘制蛇和食物
    draw_snake(snake_body)
    draw_food(food_x, food_y)

    # 刷新屏幕
    pygame.display.update()
    clock.tick(10)  # 控制游戏帧率

