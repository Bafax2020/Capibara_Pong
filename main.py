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
end = False

#спрайты и тэкст
racketa1 = Player("rak.png",13,250,3,50,120)
racketa2 = Player("rak.png",640,250,3,50,120)
ball = GameSprite("ball.png",100, 100, 0, 50, 50)

speeeed_x = 2
speeeed_y = 2

font.init()

Loser1 = font.SysFont("Arial", 30).render("Ты проиграл, 1 игрок!", True, (255,0,0))
Loser2 = font.SysFont("Arial", 30).render("Ты проиграл, 2 игрок!", True, (255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if end != True:
        ball.rect.x += speeeed_x
        ball.rect.y += speeeed_y
        window.fill(BACKGROUND)
        ball.reset()
        racketa1.update_L()
        racketa2.update_R()
        racketa1.reset()
        racketa2.reset()
    if ball.rect.y > WinY - 50 or ball.rect.y < 0:
        speeeed_y *= -1
    if sprite.collide_rect(racketa1 , ball) or sprite.collide_rect(racketa2 , ball):
        speeeed_x *= -1
    if ball.rect.x < 0:
        window.blit(Loser1,(WinX // 2 - 250, WinY // 2))
        end = True
    if ball.rect.x > WinX:
        window.blit(Loser2,(WinX // 2, WinY // 2))
        end = True

    display.update()
    clock.tick(FPS)
