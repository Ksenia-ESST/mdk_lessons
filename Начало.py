import pygame
import random
import os

screen_width = 1200
screen_height = 800
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First game by Nightwalker')
my_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(my_icon)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 300
        self.velocity_y = 0
        self.on_ground = False
        self.speed = 5
    
    def update(self):
        self.rect.y += self.velocity_y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
        if not self.on_ground:
            self.velocity_y += 1

    def jump(self):
        if self.on_ground:
            self.velocity_y = -15

    def reset(self):
        self.rect.x = 100
        self.rect.y = screen_height - 150

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('platform.jfif').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

try:
    background = pygame.image.load('back.jpg').convert()
except pygame.error as e:
    print(f"Не удалось загрузить фон: {e}")
    pygame.quit()
    exit()
background = pygame.transform.scale(background, (screen_width, screen_height))

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

ground = Platform(0, screen_height - 50, screen_width, 50)
platforms.add(ground)
all_sprites.add(ground)

for _ in range(5):
    p_width = random.randint(50, 150)
    p_height = 20
    p_x = random.randint(0, screen_width - p_width)
    p_y = random.randint(50, screen_height - 100)
    platform = Platform(p_x, p_y, p_width, p_height)
    platforms.add(platform)
    all_sprites.add(platform)

from pygame import mixer 
mixer.init() 
mixer.music.load("song.mp3") 
mixer.music.set_volume(5) 

running = True
while running: 
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.jump()
            if event.key == pygame.K_e:
                mixer.music.play() 
            if event.key == pygame.K_r:
                mixer.music.stop()
    all_sprites.update()
    player.on_ground = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y >=0:
            player.rect.bottom = platform.rect.top
            player.velocity_y = 0
            player.on_ground = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    









import pygame

pygame.init()
i=0
clock=pygame.time.Clock()
while i<5:
    clock.tick(1)
    print(clock.get_time())
    print(clock.get_fps())
    i=i+1









# pygame.quit() 
# COLOR = (255, 100, 98)
# SURFACE_COLOR = (167, 255, 100)
# WIDTH = 500
# HEIGHT = 500

# class Sprite(pygame.sprite.Sprite):
# 	def __init__(self, color, height, width):
# 		super().__init__()

# 		self.image = pygame.Surface([width, height])
# 		self.image.fill(SURFACE_COLOR)
# 		self.image.set_colorkey(COLOR)

# 		pygame.draw.rect(self.image,
# 						color,
# 						pygame.Rect(0, 0, width, height))

# 		self.rect = self.image.get_rect()

# 	def moveRight(self, pixels):
# 		self.rect.x += pixels

# 	def moveLeft(self, pixels):
# 		self.rect.x -= pixels

# 	def moveForward(self, speed):
# 		self.rect.y += speed * speed/10

# 	def moveBack(self, speed):
# 		self.rect.y -= speed * speed/10


# import random
# import pygame

# # Global Variables
# COLOR = (255, 100, 98)
# SURFACE_COLOR = (167, 255, 100)
# WIDTH = 500
# HEIGHT = 500

# # Object class
# class Sprite(pygame.sprite.Sprite):
# 	def __init__(self, color, height, width):
# 		super().__init__()

# 		self.image = pygame.Surface([width, height])
# 		self.image.fill(SURFACE_COLOR)
# 		self.image.set_colorkey(COLOR)

# 		pygame.draw.rect(self.image,
# 						color,
# 						pygame.Rect(0, 0, width, height))

# 		self.rect = self.image.get_rect()

# 	def moveRight(self, pixels):
# 		self.rect.x += pixels

# 	def moveLeft(self, pixels):
# 		self.rect.x -= pixels

# 	def moveForward(self, speed):
# 		self.rect.y += speed * speed/10

# 	def moveBack(self, speed):
# 		self.rect.y -= speed * speed/10


# pygame.init()


# RED = (255, 0, 0)


# size = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Creating Sprite")


# all_sprites_list = pygame.sprite.Group()

# playerCar = Sprite(RED, 20, 30)
# playerCar.rect.x = 200
# playerCar.rect.y = 300


# all_sprites_list.add(playerCar)

# exit = True
# clock = pygame.time.Clock()

# while exit:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			exit = False
# 		elif event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_x:
# 				exit = False

# 	keys = pygame.key.get_pressed()
# 	if keys[pygame.K_LEFT]:
# 		playerCar.moveLeft(10)
# 	if keys[pygame.K_RIGHT]:
# 		playerCar.moveRight(10)
# 	if keys[pygame.K_DOWN]:
# 		playerCar.moveForward(10)
# 	if keys[pygame.K_UP]:
# 		playerCar.moveBack(10)

# 	all_sprites_list.update()
# 	screen.fill(SURFACE_COLOR)
# 	all_sprites_list.draw(screen)
# 	pygame.display.flip()
# 	clock.tick(60)

# pygame.quit()
