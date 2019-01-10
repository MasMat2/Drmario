import pygame, sys


class Piano():

    def __init__(self, surface):
        self.surface = surface
        self.events = set()

    def input_events(self):
        for event in self.events:
            if event == pygame.K_a:
                print("a")
            if event == pygame.K_s:
                print("s")
            if event == pygame.K_d:
                print("d")
            if event == pygame.K_f:
                print("f")
            if event == pygame.K_g:
                print("g")
            if event == pygame.K_h:
                print("h")
            if event == pygame.K_j:
                print("j")
            if event == pygame.K_k:
                print("k")
            if event == pygame.K_l:
                print("l")
            if event == pygame.K_SEMICOLON:
                print(";")
            if event == pygame.K_QUOTE:
                print("'")
            if event == pygame.K_BACKSLASH:
                print("\\")

        self.events = set()
        
    def update(self):
        self.input_events()

class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True

        self.piano = Piano(self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            self.piano.events.add(event.key)


    def on_loop(self):
        self.piano.update()

    def on_render(self):
        pass
        self._display_surf.fill((0, 0, 0))
        pygame.display.flip()

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
    thePiano = main()
    thePiano.on_execute()
