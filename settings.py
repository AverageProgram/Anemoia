import os
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

'''
pygame.init()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
'''

# Player settings
PLAYER_SPEED = 300
PLAYER_IMGDOWN = 'default(3)down.png'
PLAYER_IMGUP = 'default(3)up.png'
PLAYER_IMGRIGHT = 'default(3)right.png'
PLAYER_IMGLEFT = 'default(3)left.png'

#wall settings
WALL_IMG = 'wall2.png'

FLOOR_IMG = 'wall1.png'

#start sreen
#START_IMG = pygame.image.load(os.path.join(img_folder,'AnemoiaStart1.png')).convert()

#text function
font_name = pygame.font.match_font('arial')
def draw_tex(surf,text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface =font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.miptop = (x, y)
    surf.blit(text_surface, text_rect)
