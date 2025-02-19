import pygame
import random
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

score=0
sc_w=1000
sc_h=800
speed=5
car_w=50
car_h=100
car_x=sc_w//2-(car_w//2)
car_y=sc_h-car_h
obstacles=[]
obstacle_w=50
obstacle_h=100
obstacle_y=-obstacle_h


car=pygame.image.load('IMG/car.png')
car=pygame.transform.scale(car,(car_w,car_h))
# car = pygame.Surface((175, 100))
# car.fill(navy)
car=pygame.image.load('IMG/enermy.png')
car=pygame.transform.scale(car,(car_w,car_h))

enermy_img=pygame.image.load('IMG/car.png')
enermy_img=pygame.transform.scale(enermy_img,(obstacle_w,obstacle_h))

road_w=300
road_h=sc_h
road_img=pygame.image.load('IMG/road.png')
road_img=pygame.transform.scale(road_img,(road_w,road_h))
bg_y=0

clock = pygame.time.Clock()

score=0
font = pygame.font.Font(None, 36)



def draw_score(score):
    score_text = font.render(f"Điểm: {score}", True, black)
    sc.blit(score_text, (10, 10))

def draw_obstacle():
    for obstacle in obstacles:
        sc.blit(enermy_img,obstacle)



def check_collision(car_rect):
    for obostacle in obstacles:
        if car_rect.colliderect(obstacle):
            return True
        return False

running = True
while running:
    sc.fill(gray)
    road_x=sc_w//2-(road_w//2)
    sc.blit(road_img,(sc_w//2-(road_w//2),bg_y-sc_h+10))
    sc.blit(road_img,(sc_w//2-(road_w//2),bg_y))


    bg_y+=speed
    if bg_y>sc_h:
        bg_y=0


    if random.random()<0.01:
        obstacle_x=random.randint(road_x,road_x+road_w-50)
        obstacles.append(pygame.Rect(obstacle_x,obstacle_y,obstacle_w,obstacle_h))

    for obstacle in obstacles:
        obstacle.y+=speed
        if obstacle.y>sc_h:
            obstacles.remove(obstacle)
            score+=1




    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x-speed>road_x:
        car_x -= speed
    if keys[pygame.K_RIGHT] and car_x+speed<road_x+road_w-50:
        car_x += speed

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    car_rect=pygame.Rect(car_x,car_y,car_w,car_h)
    sc.blit(car,(car_x,car_y))

    if check_collision(car_rect):
        print('Game Over')
        running=False
    draw_obstacle()
    draw_score(score)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

