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

# class iterator:
#
#     def cycle(iterable):
#
#         saved = []
#
#         for element in iterable:
#             yield element
#             saved.append(element)
#
#         while saved:
#             for element in saved:
#                 yield element


# class Blocks:
#
#     def on_notify(self, subject, event):
#         if event == "touch bottom":
#             if subject  == theGame.player:
#                 self.array.append((theGame.player.top_left))
#                 self.array.append((theGame.playerrect_left + theGame.player.tail_left*theGame.width, self.rect_top + self.tail_top*self.height + self.height))

class Physics:
    pass
class Player:

    def __init__(self):

        self.speed = 24

        self.rect_left, self.rect_top = 0, 0

        self.width, self.height = 24, 24

        self.window_width, self.window_height = pygame.display.get_surface().get_size()

        self.color = BLUE
        self.color_tail = YELLOW

        self.events = set()

        self.tail_config = self.change_tail()
        next(self.tail_config)

    def update(self):
        for event in self.events:
            if event == pygame.K_UP:
                self.rect_top -= self.speed

            if event == pygame.K_DOWN:
                self.rect_top += self.speed

            if event == pygame.K_RIGHT:
                self.rect_left += self.speed

            if event == pygame.K_LEFT:
                self.rect_left -= self.speed

            if event == pygame.K_SPACE:
                next(self.tail_config)

        if self.rect_left < 0:
            self.rect_left = 0
        if self.rect_left > self.window_width - self.width:
            self.rect_left = self.window_width - self.width

        if self.rect_top < 0:
            self.rect_top = 0
        if self.rect_top > self.window_height - self.height:
            self.rect_top = self.window_height - self.height

        self.tail_pos = [self.rect_left + self.tail_configx*self.width, self.rect_top + self.tail_configy*self.height]

        if self.tail_pos[0] < 0:
            self.tail_pos[0] = 0
        elif self.tail_pos[0] > self.window_width - self.width:
            self.tail_pos[0] = self.window_width - self.width

        elif self.tail_pos[1] < 0:
            self.tail_pos[1] = 0
        if self.tail_pos[1] > self.window_height - self.height:
            self.tail_pos[1] = self.window_height - self.height

        self.rect_left, self.rect_top = self.tail_pos[0] - self.tail_configx*self.width, self.tail_pos[1] - self.tail_configy*self.height

        self.events = set()

    def change_tail(self):
        while True:
            for i in range(4):
                if  i == 0:  #'right'
                    self.tail_configx, self.tail_configy = 1, 0
                elif i == 1:  #'down'
                    self.tail_configx, self.tail_configy = 0, 1
                elif i == 2:  #'left'
                    self.tail_configx, self.tail_configy = -1, 0
                elif i == 3:  #'up'
                    self.tail_configx, self.tail_configy = 0, -1
                yield None

    def inside_block(self):
        head = theGame._display_surface.get_at(self.rect_left, self.rect_top + self.height) != WHITE
        tail = theGame._display_surface.get_at(self.tail_pos[0], self.tail_pos[1] + self.height) != WHITE
        if head or tail:
            return True
        else:
            return False

    def draw(self):
        pygame.draw.rect(theGame._display_surf, self.color, (self.rect_left, self.rect_top, self.width, self.height), 0)
        pygame.draw.rect(theGame._display_surf, self.color_tail, (self.tail_pos[0], self.tail_pos[1], self.width, self.height), 0)

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
        self.player = Player()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # Gameplay input
        if event.type == pygame.KEYDOWN:
            self.player.events.add(event.key)

    def on_loop(self):
        self.player.update()

    def on_render(self):
        self._display_surf.fill(WHITE)
        self.player.draw()
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
