import pygame, sys, time


class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        self.clock = pygame.time.get_ticks()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        time.sleep(2)
        print(pygame.time.get_ticks() - self.clock)
        pass

    def on_render(self):
        pass

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
