import pygame, random, sys, copy
from pygame.locals import   *

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)
COLORS = [BLUE,GREEN,YELLOW,PURPLE]

class Player:

    def __init__(self):

        self.speed = 24

        self.rect_left, self.rect_top = 0, 0
        self.width, self.height = self.size = 24, 24

        self.color = random.choice(COLORS)
        self.color_tail = random.choice(COLORS)

        self.block_configs = ['up', 'right', 'down', 'left']


    def draw(self, tail_pos):
        if tail_pos == 'up':
            left, top = 0, -1
        elif tail_pos == 'right':
            left, top = 1, 0
        elif tail_pos == 'down':
            left, top = 0, 1
        elif tail_pos == 'left':
            left, top = -1, 0
        pygame.draw.rect(theGame._display_surf, self.color, (self.rect_left, self.rect_top, self.width, self.height), 0)
        pygame.draw.rect(theGame._display_surf, self.color_tail, (  (self.rect_left + left*self.width) , (self.rect_top + top*self.height) , self.width, self.height), 0)

class Game:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 512, 512

    def on_init(self):
        # Pygame parameters
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 31)
        self._running = True

        # Player objects
        self.player = Player()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # Gameplay input
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                self.player.rect_top -= self.player.speed

            if event.key == pygame.K_DOWN:
                self.player.rect_top += self.player.speed

            if event.key == pygame.K_RIGHT:
                self.player.rect_left += self.player.speed

            if event.key == pygame.K_LEFT:
                self.player.rect_left -= self.player.speed

            if event.key == pygame.K_SPACE:
                self.player.rect_left -= self.player.speed





    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(WHITE)
        self.player.draw('right')
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == '__main__' :
    theGame = Game()
    theGame.on_execute()
