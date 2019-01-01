import pygame, timeit, sys

def touch(surface):
        a = pygame.draw.rect(surface, (0, 0, 0), (24, 24, 24, 24), 0)
        b = pygame.draw.rect(surface, (0, 0, 0), (24, 48, 24, 24), 0)

        first, last = [(i[0], i[1] + 24) for i in ((24, 24), (24, 48))]
        try:
            pos_to_check = [surface.get_at(first), surface.get_at(last)]
        except IndexError:
            return True
        if [(0, 0, 0), (0, 0, 0)] != pos_to_check:
            return True
        return None

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

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        for i in range(2000):
            self._display_surf.fill((0, 0, 0))
            touch(self._display_surf)
            pygame.display.update()
        self._running = False

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


def run():
    theGame = Game()
    theGame.on_execute()

print(timeit.timeit("run()", setup="from __main__ import run", number=1))
