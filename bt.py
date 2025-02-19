import pygame
pygame.init()
sc=pygame.display.set_mode((800,600))
pygame.display.set_caption('Bài tập')
white=(255,255,255)
yellow=(255,255,0)
gray=(128,128,128)
cyan=(0,255,255)
red=(255,0,0)
black=(0,0,0)
navy=(0,0,128)
blue=(64,224,208)
green=(0,128,0)
brown=(139,69,19)
running=True
while running:
    pygame.draw.rect(sc,blue,pygame.Rect(0,0,800,400))
    pygame.draw.rect(sc,green,pygame.Rect(0,400,800,100))
    pygame.draw.rect(sc,gray,pygame.Rect(0,500,800,100))
    pygame.draw.circle(sc, yellow, (700,100),65, 300)
    pygame.draw.circle(sc, white, (100,100),50, 300)
    pygame.draw.circle(sc, white, (155,100),60, 300)
    pygame.draw.circle(sc, white, (210,100),50, 300)
    pygame.draw.circle(sc, white, (500,150),50, 300)
    pygame.draw.circle(sc, white, (555,150),60, 300)
    pygame.draw.circle(sc, white, (610,150),50, 300)
    pygame.draw.rect(sc,brown,pygame.Rect(325,250,200,200))
    point1=[(325,250),(525,250),(425,150)]
    pygame.draw.polygon(sc,red,point1)
    pygame.draw.rect(sc,black,pygame.Rect(400,350,60,100))
    pygame.draw.rect(sc,white,pygame.Rect(367,300,120,60))
    surface = pygame.Surface((100, 100))
    surface.fill(red)


    for event in pygame.event.get():
        # xét bấm nút tắt
        if event.type==pygame.QUIT:
            running=False   
    # cập nhật màn hình
    pygame.display.update()