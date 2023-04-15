from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sp_image, sp_x, sp_y, sp_speed, sp_size_x, sp_size_y):
        super().__init__()
        self.image = transform.scale(image.load(sp_image), (sp_size_x, sp_size_y))
        self.speed = sp_speed
        self.rect = self.image.get_rect()
        self.rect.x = sp_x
        self.rect.y = sp_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#1 - Q A
#2 - /\ \/

class Player(GameSprite):
    def update_L(self):
        keys_player = key.get_pressed()
        if keys_player[K_q] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_player[K_a] and self.rect.y < WinY - 60:
            self.rect.y += self.speed

    def update_R(self):
        keys_player = key.get_pressed()
        if keys_player[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_player[K_DOWN] and self.rect.y < WinY - 60:
            self.rect.y += self.speed

WinX = 700
WinY = 500
#игровая сцена

BACKGROUND = (200,255,255)
window = display.set_mode((WinX, WinY))
window.fill(BACKGROUND)
display.update()
display.set_caption("Pong Ping")

clock = time.Clock()
FPS = 60

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
