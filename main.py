from settings import *
import pygame as pg
import sys
from os import path
from sprites import *
from tilemap import *

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        
        
        

        
    #LOAD IMAGES/FOLDERS
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder= path.join(game_folder, 'img')
        self.map = Map(path.join(game_folder, 'map2.txt'))
        
        #Player images
        self.player_imgdown = pg.image.load(path.join(img_folder, PLAYER_IMGDOWN)).convert_alpha()  
        self.player_imgup = pg.image.load(path.join(img_folder, PLAYER_IMGUP)).convert_alpha()
        self.player_imgright = pg.image.load(path.join(img_folder, PLAYER_IMGRIGHT)).convert_alpha()
        self.player_imgleft = pg.image.load(path.join(img_folder, PLAYER_IMGLEFT)).convert_alpha()
        
        #Walls/start screen
        self.floor_img = pg.image.load(path.join(img_folder, FLOOR_IMG)).convert_alpha()
        self.floor_img = pygame.transform.scale(self.floor_img,(TILESIZE, TILESIZE))
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.start_img = pg.image.load(path.join(img_folder, "AnemoiaStart1.png")).convert_alpha()
        self.start_img = pygame.transform.scale(self.start_img, (WIDTH, HEIGHT))
        self.wall_img = pygame.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        self.player_imgup = pygame.transform.scale(self.player_imgup, (64, 96))
        self.player_imgright = pygame.transform.scale(self.player_imgright, (64, 96))
        self.player_imgleft = pygame.transform.scale(self.player_imgleft, (64, 96))
        self.player_imgdown = pygame.transform.scale(self.player_imgdown, (64, 96))
        #End screen
        self.end_img =pg.image.load(path.join(img_folder, "gameOver.png")).convert_alpha()
        self.end_img = pygame.transform.scale(self.end_img, (WIDTH, HEIGHT))
        #Sounds
        self.sound=0
        self.sounds=['Betrayal.wav','Dark room.wav', 'Split perspective.wav']

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'F':
                    Floor(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def show_end_screen(self):
      self.screen.blit(self.end_img,(0,0))
      pygame.display.flip()
      waiting = True
      while waiting:
          for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: #CHANGE THIS KEY????
                    self.quit()
                    
    def changeMusic(self, track):
        game_folder = path.dirname(__file__)
        self.snd_folder= path.join(game_folder, 'snd')
        if track == 9:
            pg.mixer.music.stop()
        else:
            pg.mixer.music.load(os.path.join(self.snd_folder, self.sounds[track]))
            pg.mixer.music.play(loops=-1) 
        

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_k:
                    self.show_end_screen()
                if event.key==pg.K_1:
                    self.changeMusic(0)
                if event.key==pg.K_2:
                    self.changeMusic(1)
                if event.key==pg.K_3:
                    self.changeMusic(2)
                if event.key==pg.K_9:
                    self.changeMusic(9)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        goscreen = True
        self.screen.blit(self.start_img,(0,0))
        pygame.display.flip()
        
        while goscreen:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    goscreen = False
 

    
        

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.show_go_screen()
    g.run()
