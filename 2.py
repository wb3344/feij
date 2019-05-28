from random import randint,randrange
import pygame
from math import sqrt,pi


class Ball(object):
    def __init__(self, center, color, radius, sx, sy):
        self._center = center
        self._color = color
        self._radius = radius
        self._sx = sx
        self._sy = sy

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,radius):
        self._radius = radius

    def move(self):
        x, y = self._center[0], self._center[1]
        x += self._sx
        y += self._sy
        self._center = (x, y)
        # if x + self._radius > 800:
        #     self._sx = -abs(self._sx)
        # elif x + self._radius < 0:
        #     self._sx = abs(self._sx)
        # elif y +self._radius > 800:
        #     self._sy = -abs(self._sy)
        # elif y +self._radius < 0:
        #     self._sy = abs(self._sy)
        if x + self._radius >= 800 or x - self._radius <= 0 or x <= 0:
            self._sx = -self._sx
        if y +self._radius >= 800 or y - self._radius <= 0 or y <= 0:
            self._sy = -self._sy

    def draw(self,screen):
        pygame.draw.circle(screen, self._color, self._center, self._radius, 0)

    def eat(self, other):
        a = sqrt((self._center[0] - other.center[0]) ** 2 + (self._center[1] - other.center[1]) ** 2)
        if a < self._radius + other.radius and self._radius < other.radius:
            other.radius = self._radius + other.radius
            self.radius = 0
        elif a < self._radius + other.radius and self._radius > other.radius:
            self._radius = self._radius + other.radius
            other.radius = 0


def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode([800,800])
    pygame.display.set_caption('大球吃小球')
    c = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                 event.button == 1:
                color = random_color()
                radius = randint(10,100)
                sx, sy = randint(-10,10), randint(-10,10)
                ball = Ball(event.pos, color, radius, sx, sy)
                balls.append(ball)
        refresh(screen,balls)
        c.tick(20)  # 50帧
        for ball in balls:
            ball.move()
        balls_len = len(balls)
        for i in range(balls_len):
            for x in range(balls_len):
                balls[i].eat(balls[x])
        for ball in balls:
            if ball.radius == 0:
                balls.remove(ball)


    pygame.quit()


def refresh(screen,balls):
    bg_color = [255, 255, 255]
    screen.fill(bg_color)
    for ball in balls:
        ball.draw(screen)
    pygame.display.flip()


def random_color():
    return [randint(1,255), randint(1,255), randint(1,255)]


if __name__ == '__main__':
    main()