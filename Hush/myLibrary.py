# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 0017 上午 8:32
# @Author  : silents
# @FileName: myLibrary.py
# @Software: PyCharm
# @Blog    ：http://blog.csdn.net/chq1005613740
import pygame
from pygame.locals import *


class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.X = 0
        self.Y = 0
        # 新增了velocity属性，他是一个point
        self.velocity = Point(0.0, 0.0)

    def load(self, filename, position, bg_size):
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        # 苹果的位置
        self.rect.left, self.rect.top = position
        # self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def load_column(self, filename, position, bg_size, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = bg_size[0]
        self.frame_height = bg_size[1]
        self.position = position
        self.rect = self.master_image.get_rect()
        self.ori_frame_width = self.rect.width
        self.ori_frame_height = self.rect.height
        self.rect.left, self.rect.top = position
        self.rect.width, self.rect.height = bg_size[0], bg_size[1]
        self.columns = columns
        self.last_frame = (self.ori_frame_width // bg_size[0]) * (self.ori_frame_height // bg_size[1]) - 1

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            # rect = ( self.X, self.Y, self.frame_width, self.frame_height )
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.rect.left, self.rect.top = self.X, self.Y
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame