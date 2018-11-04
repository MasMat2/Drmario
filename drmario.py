import pygame, random, sys, copy, time
from pygame.locals import   *

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)
COLORS = [BLUE,GREEN,YELLOW,PURPLE]



class Blocks:

    def __init__(self, player):
        self.blocks = []
        self.player = player

    def update(self):
        self.delete_blocks()
        self.add_block()


    def delete_blocks(self):
        count = 0
        current_color = 0
        for x in range(0, self.player.window_width, self.player.width):
            for y in range(0, self.player.window_height, self.player.height):
                color = theGame._display_surf.get_at((x,y))[:3]
                if color == WHITE:
                    count = 0
                    current_color = 0
                elif color != current_color:
                    # if count > 3:
                    #     for i in range(x, x-self.player.height*(count), -self.player.height):
                    #         tarx = x - self.player.height
                    current_color = color
                    count = 1
                else:
                    count += 1



    def touch_player(self):
        if self.player.window_height - self.player.height in (self.player.first_top, self.player.last_top):
            return True
        y = sorted([self.player.first_top, self.player.last_top])[-1] + self.player.height
        for x in self.player.first_left, self.player.last_left:
            if theGame._display_surf.get_at((x,y)) in COLORS:
                return True

    def add_block(self):
        if self.touch_player():
            self.blocks.append(list(self.player.first) + [self.player.color[0]])
            self.blocks.append(list(self.player.last) + [self.player.color[1]])
            self.player.on_init()

    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(theGame._display_surf, COLORS[block[-1]], (block[0], block[1], self.player.width, self.player.height), 0)


class Player:

    def __init__(self, window_size):

        self.speed = 24

        self.width, self.height = 24, 24

        self.window_width, self.window_height = window_size[0], window_size[0]
        self.width_limit = self.window_width - self.width
        self.height_limit = self.window_height - self.height

        self.events = set()

        self.on_init()

    def on_init(self):
        self.rect_left, self.rect_top = 0, 0
        self.color = (int(random.random()*4), int(random.random()*4))
        self.config = self.change_config()
        self.rect_config = next(self.config)


    def input_events(self):
        for event in self.events:
            if event == pygame.K_s or event == pygame.K_DOWN:
                self.rect_top += self.speed

            if event == pygame.K_d or event == pygame.K_RIGHT:
                self.rect_left += self.speed

            if event == pygame.K_a or event == pygame.K_LEFT:
                self.rect_left -= self.speed

            if event == pygame.K_SPACE:
                self.rect_config = next(self.config)

    def change_config(self):
        while True:
                yield [(0,0),(1,0)]
                yield [(0,0),(0,-1)]
                yield [(1,0),(0,0)]
                yield [(0,-1),(0,0)]

    def get_pos(self):
        self.first_left = self.rect_left + self.rect_config[0][0] * self.width
        self.first_top = self.rect_top + self.rect_config[0][1] * self.height
        self.last_left = self.rect_left + self.rect_config[1][0] * self.width
        self.last_top = self.rect_top + self.rect_config[1][1] * self.height

        self.first = (self.first_left, self.first_top)
        self.last = (self.last_left, self.last_top)

    def correct_pos(self):
            self.get_pos()

            if self.first_left < 0 or self.last_left < 0:
                self.rect_left += self.width
            elif self.first_left > self.width_limit or self.last_left > self.width_limit:
                self.rect_left -= self.width

            if self.first_top < 0 or self.last_top < 0:
                self.rect_top += self.height
            elif self.first_top > self.height_limit or self.last_top > self.height_limit:
                self.rect_top -= self.height

            self.get_pos()

            self.events = set()

    def update(self):
        self.input_events()
        self.correct_pos()

    def draw(self):
        pygame.draw.rect(theGame._display_surf, COLORS[self.color[0]], (self.first_left, self.first_top, self.width, self.height), 0)
        pygame.draw.rect(theGame._display_surf, COLORS[self.color[1]], (self.last_left, self.last_top, self.width, self.height), 0)

class Game:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 480, 480

    def on_init(self):
        # Pygame parameters
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

        # Player objects
        self.player = Player(self.size)
        self.blocks = Blocks(self.player)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # Gameplay input
        if event.type == pygame.KEYDOWN:
            self.player.events.add(event.key)

    def on_loop(self):
        self.player.update()
        self.blocks.update()

    def on_render(self):
        self._display_surf.fill(WHITE)
        self.player.draw()
        self.blocks.draw()
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
