import pygame#游戏屏幕大小
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
PRAME_PER__SEC = 60
#敌机添加事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
#子弹事件
CREATE_BULLET_EVENT = pygame.USEREVENT+1


#爆炸销毁图片
bg1 = pygame.image.load('/home/shenrunze/桌面/plan/images/enemy1_down1.png' )
bg2 = pygame.image.load('/home/shenrunze/桌面/plan/images/enemy1_down2.png' )
bg3 = pygame.image.load('/home/shenrunze/桌面/plan/images/enemy1_down3.png' )
bg4 = pygame.image.load('/home/shenrunze/桌面/plan/images/enemy1_down4.png' )
#爆炸的精灵组
enemy1_down_group=pygame.sprite.Group()



#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,imagename,speed = 1):
        super().__init__()#调用父类
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()#获取围栏
        self.speed = speed
    def update(self):
        self.rect.y +=self.speed
class EnemySprite(GameSprite):#敌机精灵
    def __init__(self):
        imagename = '/home/shenrunze/桌面/plan/images/enemy1_hit.png'
        super().__init__(imagename,random.randint(1,5))
        self.rect.bottom = 0
        self.rect.x = random.randint(1,480-self.rect.width)
        self.down_index = 0
        #self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
    def update(self):
        super().update()
        if self.rect.top >= 600:
            self.kill()
    def __del__(self):
        pass
class BackGroundSprint(GameSprite):#背景精灵
    def __init__(self,isalt = True):
        imagename = '/home/shenrunze/桌面/plan/images/background.png'
        super().__init__(imagename,5)
        if not isalt:
            self.rect.bottom = 0
    def update(self):
        super().update()
        if self.rect.top >= 600:#判断移出屏幕
            self.rect.bottom = 0#挪到屏幕上方
class HeroSprint(GameSprite):
    def __init__(self):
        imagename = ('/home/shenrunze/桌面/plan/images/hero.gif')
        super().__init__(imagename,0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-20
    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        self.rect.y += self.speed1
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
class BulletSprite(GameSprite):
    def __init__(self):
        imagename = '/home/shenrunze/桌面/plan/images/bullet.png'
        super().__init__(imagename,-25)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
class Soruce(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
