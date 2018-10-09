import pygame
from GameSprite import *
pygame.init()
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load('/home/shenrunze/桌面/08高级/1808/plan/images/background.png')
screen.blit(bg,(0,0))
hero = pygame.image.load('/home/shenrunze/桌面/08高级/1808/plan/images/hero.gif')
time = pygame.time.Clock()#游戏时钟
rect = pygame.Rect(200,200,100,126)
enemy = GameSprite('/home/shenrunze/桌面/plan/images/enemy1_hit.png')
enemy1 = GameSprite('/home/shenrunze/桌面/plan/images/enemy1_hit.png',2)
enemy1.rect.x = 200
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:
    time.tick(100)#每秒刷新100次
    rect.y -=20
    screen.blit(bg,(0,0))#贴图像
    screen.blit(hero,rect)#贴图像
    if rect.bottom <= 0:
        rect.top = 700
    for event in pygame.event.get():
    # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            exit()
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
