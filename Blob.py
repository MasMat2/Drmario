import pygame, sys



class blob:

    def __init__(self, pos, r):
        self.mw, self.mh = pos
        self.r = r

    def collide(self, new):
        return ((self.mw-new[0])**2 + (self.mh-new[1])**2)< self.r**2

    def draw(self):
        mw = self.mw
        mh = self.mh
        for x in range(mw - self.r, mw + self.r, theThing.step):
            for y in range(mh - self.r, mh + self.r, theThing.step):
                d = ((mw - x)**2 + (mh - y)**2)**(1/2)
                if d > self.r:
                    continue
                try:
                    colors = [i for i in theThing._display_surf.get_at((x,y))]
                except IndexError:
                    continue

                cop = [i for i in colors]
                colors[2] = 255 - (255*d)//self.r
                for index in range(len(colors)):
                    if colors[index] > 255:
                        colors[index] = 255
                    elif colors[index] < 0:
                        colors[index] = 0 #cop[index]
                theThing._display_surf.set_at((x,y), (colors[0], colors[1], colors[2]))


class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        self.blobs = [blob((100, 100), 100)]
        self.selected = None
        self.step = 1

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for blob in self.blobs:
                if blob.collide(event.pos): self.selected = blob; self.step = 4; break

        if event.type == pygame.MOUSEBUTTONUP:
            self.selected = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.step = 1



    def on_loop(self):
        if self.selected: self.selected.mw, self.selected.mh = pygame.mouse.get_pos()

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        for blob in self.blobs:
            blob.draw()
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
    theThing = main()
    theThing.on_execute()
