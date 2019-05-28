import itertools, sys, time, random, math, pygame
from pygame.locals import *
from game_go.myLibrary import *


def calc_velocity(direction, vel=1.0):
    velocity = Point(0, 0)
    if direction == 0:  # 上
        velocity.Y = -vel
    elif direction == 2:  # 右
        velocity.X = vel
    elif direction == 4:  # 下
        velocity.Y = vel
    elif direction == 6:  # 左
        velocity.X = -vel
    return velocity


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("吃苹果")
font = pygame.font.SysFont('arial', 36)
timer = pygame.time.Clock()

# 创建精灵组
player_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

# 初始化玩家精灵组
# def load_column(self, filename, position, bg_size, columns):
position = 800 / 2 - 10, 600 / 2 + 10
bg_size = 62.5, 62.5
player = MySprite()
player.load_column("./you.jpg", position, bg_size, 8)
# player.position = 80, 80
player.direction = 4
player_group.add(player)

# 初始化food精灵组

for n in range(1, 40):
    food = MySprite();
    position = random.randint(0, 750), random.randint(0, 550)
    bg_size = 50, 48
    food.load("./squirrel.jpg", position, bg_size)
    food_group.add(food)

game_over = False
player_moving = False
player_health = 0

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    else:
        player_moving = False

    if not game_over:
        # 根据角色的不同方向，使用不同的动画帧
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns - 1
        if player.frame != player.first_frame:
            player.frame = player.first_frame

        if not player_moving:
            # 当停止按键（即人物停止移动的时候），停止更新动画帧
            player.frame = player.first_frame = player.last_frame
        else:
            player.velocity = calc_velocity(player.direction, 2)
            player.velocity.X *= 2
            player.velocity.Y *= 2

        # 更新玩家精灵组
        player_group.update(ticks, 50)

        # 移动玩家
        if player_moving:
            player.X += player.velocity.X
            player.Y += player.velocity.Y
            if player.X < 0:
                player.X = 0
            elif player.X > 700:
                player.X = 700
            if player.Y < 0:
                player.Y = 0
            elif player.Y > 500:
                player.Y = 500
        myfont = pygame.font.SysFont('arial', 36)
        white = 255, 255, 255
        textImage = myfont.render("Hello Pygame:%i-%i" % (player.X, player.Y), True, white)

        # 检测玩家是否与食物冲突，是否吃到果实
        attacker = None
        attacker = pygame.sprite.spritecollide(player, food_group, False, pygame.sprite.collide_circle)
        if len(attacker) != 0:
            for atta in attacker:
                # if pygame.sprite.collide_circle(player, atta):
                if pygame.sprite.collide_circle_ratio(0.65)(player, atta):
                    player_health += 2;
                    food_group.remove(atta);
        if player_health > 100: player_health = 100
        # 更新食物精灵组
        # food_group.update(ticks, 50)

        if len(food_group) == 0:
            game_over = True
    # 清屏
    screen.fill((50, 50, 100))

    # 绘制精灵
    food_group.draw(screen)
    player_group.draw(screen)

    # 绘制玩家血量条
    pygame.draw.rect(screen, (50, 150, 50, 180), Rect(300, 570, player_health * 2, 25))
    pygame.draw.rect(screen, (100, 200, 100, 180), Rect(300, 570, 200, 25), 2)

    if game_over:
        textImage = font.render("G A M E   O V E R", True, (0, 0, 0))
        screen.blit(textImage, (100, 100))
    # print_text(font, 300, 100, "G A M E   O V E R")

    screen.blit(textImage, (300, 500))
    pygame.display.update()