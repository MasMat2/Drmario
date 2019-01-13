import pygame, sys, math, time


class Animation:
    def __init__(self, surface):
        self.points = []
        self.surface = surface
        self.width, self.height = [i//2 for i in self.surface.get_size()]
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.period = 5
        self.speed = self.period*60
        self.f = 0
        self.pos = [
        [0,0,-1],
        [0,0,1]
        ]

        self.join = [
        [0,1]
        ]

        self.xmove = 0

    def draw(self):
        # angle = math.atan(2/(2-(i[2])))
        for i in self.pos:
            z = i[2]
            xa = self.xmove/(2-(i[2]))
            x = int(self.width + 200*xa/(3+z))
            y = int(self.width + 200*i[1]/(3+z))
            self.surface.set_at((x, y), (255,255,255))
        self.xmove += 0.001

class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        self.animation = Animation(self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.animation.draw()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while ( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = main()
    theApp.on_execute()
