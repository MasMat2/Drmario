import pygame, sys, math, time


class Animation:
    def __init__(self, surface):
        self.points = []
        self.surface = surface
        self.width, self.height = [i/2 for i in self.surface.get_size()]
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.period = 5
        self.speed = self.period*60
        self.pos = [
        [1,-1,1],
        [-1,-1,1],
        [-1,-1,-1],
        [1,-1,-1],
        [1,1,1],
        [-1,1,1],
        [-1,1,-1],
        [1,1,-1],
        ]
        #xyz

        self.join = [
        [0,1],
        [1,2],
        [2,3],
        [3,0],
        [4,5],
        [5,6],
        [6,7],
        [7,4],
        [0,4],
        [1,5],
        [2,6],
        [3,7],
        ]

    def draw(self):
        self.points = []
        for i in self.pos:
            angle = 2*self.counter*math.pi/self.speed
            # z = math.cos(angle)*i[2] + math.sin(angle)*i[0]
            # y = int(self.width + 200*i[1]/(3+z))
            # xz = math.cos(angle)*i[0] - math.sin(angle)*i[2]
            # x = int(self.width + 200*xz/(3+z))

            x = (math.cos(angle)*i[0] - math.sin(angle)*i[2])
            z = (math.cos(angle)*i[2] + math.sin(angle)*i[0])

            y = (math.cos(0)*i[1] - math.sin(0)*z)
            z = (math.cos(0)*z + math.sin(0)*i[1])


            x = 200 + 50*x
            y = 200 + 50*y
            z = 200 + 50*z
            self.points.append((x, y))

        for j in self.join:
            pygame.draw.line(self.surface, (255,255,255), self.points[j[0]], self.points[j[1]])
        if self.counter == self.speed:
            self.counter = 0
        self.counter +=1

    def update(self):
        self.clock.tick(60)



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
        self.animation.update()

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
