import pygame
import random
import time

import pygame.draw
pygame.init()
sc=pygame.display.set_mode((1000,800))
pygame.display.set_caption('Buổi 1')
white=(255,255,255)
yellow=(255,255,0)
gray=(128,128,128)
cyan=(0,255,255)
red=(255,0,0)
black=(0,0,0)
navy=	(0,0,128)
sc_w=1000
sc_h=800
ground_y=700
nv_w=100
nv_h=200
nv_y=ground_y-nv_h
nv_x=sc_w//2
car = pygame.Surface((nv_w, nv_h))


clock = pygame.time.Clock()



running = True
while running:
    sc.fill(white)

    pygame.draw.rect(sc,black,pygame.Rect(0,700,1000,100))
    car=pygame.draw.rect(sc,navy,pygame.Rect(nv_x,nv_y,nv_w,nv_h))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        nv_y-=1
        

        


        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()

