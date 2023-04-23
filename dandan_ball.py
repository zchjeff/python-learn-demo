# -*- coding:utf-8 -*-
import pygame
import random

# 初始化Pygame库
pygame.init()

# 设置游戏窗口的宽度和高度
window_width = 800
window_height = 600

# 创建游戏窗口
game_window = pygame.display.set_mode((window_width, window_height))

# 设置游戏窗口的标题
pygame.display.set_caption('弹弹球')

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 定义球的初始位置、大小和移动速度
ball_position = [window_width // 2, window_height // 2]
ball_radius = 10
ball_speed = [random.randint(-5, 5), random.randint(-5, 5)]

# 定义挡板的初始位置、大小和移动速度
paddle_width = 80
paddle_height = 10
paddle_position = [window_width // 2 - paddle_width // 2, window_height - paddle_height - 10]
paddle_speed = 0


# 定义球的移动函数
def move_ball():
    global ball_position, ball_speed, game_running

    # 移动球的位置
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # 如果球碰到了窗口的边缘，反弹
    if ball_position[0] < ball_radius or ball_position[0] > window_width - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] < ball_radius:
        ball_speed[1] = -ball_speed[1]
    elif ball_position[1] > window_height - ball_radius:
        # 如果球落到了底部，游戏结束
        game_running = False


# 定义挡板的移动函数
def move_paddle():
    global paddle_position, paddle_speed

    # 移动挡板的位置
    paddle_position[0] += paddle_speed

    # 如果挡板碰到了窗口的边缘，停止移动
    if paddle_position[0] < 0:
        paddle_position[0] = 0
    elif paddle_position[0] > window_width - paddle_width:
        paddle_position[0] = window_width - paddle_width


# 定义游戏循环
game_running = True
while game_running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEMOTION:
            # 如果鼠标移动，移动挡板的位置
            paddle_position[0] = event.pos[0] - paddle_width // 2

    # 移动球和挡板
    move_ball()
    move_paddle()

    # 检测球和挡板是否碰撞
    if ball_position[1] + ball_radius >= paddle_position[1] and \
            ball_position[0] >= paddle_position[0] and \
            ball_position[0] <= paddle_position[0] + paddle_width:
        ball_speed[1] = -ball_speed[1]

    # 绘制游戏界面
    game_window.fill(white)
    pygame.draw.circle(game_window, red, ball_position, ball_radius)
    pygame.draw.rect(game_window, blue, (paddle_position[0], paddle_position[1], paddle_width, paddle_height))
    pygame.display.update()

    # 控制游戏帧率
    pygame.time.Clock().tick(60)

# 退出Pygame库
pygame.quit()
