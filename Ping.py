from pygame import *
from random import randint

win_w = 1200
win_h = 800        
windi = display.set_mode((win_w,win_h))
display.set_caption('PingPong')
back = ( 177, 33, 55)
windi.fill(back)
#zadniFon = transform.scale(image.load(''),(1200,800))
#Амир молодец!!!!!!
clock = time.Clock()
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__ (self, p_Image, X, Y, Speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(p_Image),(100,100))
        self.speed = Speed
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
    def reset(self):
        windi.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        but = key.get_pressed()
        if but[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if but[K_d] and self.rect.x  < win_w - 110:
            self.rect.x += self.speed
class Enemy(GameSprite):
    direction = 'nalevo'
    def update(self):
        self.rect.y += self.speed
        global proshlo
        if self.rect.y > win_h:
            self.rect.y = 0
            self.rect.x = randint( 80,620)
            self.speed = randint(1, 5)
game = True            
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    