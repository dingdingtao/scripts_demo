'''
Author: dingdingtao
Date: 2021-01-18 17:54:53
LastEditTime: 2021-01-18 18:02:01
LastEditors: dingdingtao
Description: 
'''
import sys, pygame
import time

pygame.init()
 
size = width, height = 640, 480
dx = 1
dy = 1
x= 163
y = 120
black = (0,0,0)
white = (255,255,255)
 
screen = pygame.display.set_mode(size)
 
while 1:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
 
    x += dx
    y += dy
 
    if x < 0 or x > width:  
        dx = -dx
 
    if y < 0 or y > height:
        dy = -dy
 
    screen.fill(black)
 
    pygame.draw.circle(screen, white, (x,y), 8)
 
    pygame.display.flip()
    time.sleep(0.003)