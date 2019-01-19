import pygame, sys, math, time

class Animation:
    def __init__(self, surface):
        # Import pygame display surface and its width and height
        self.surface = surface

        # Set the clock to keep a frame rate of 60 hertz
        self.clock = pygame.time.Clock()

        # Set a counter for the automatic rotation of the cube
        self.counterx, self.countery = 0, 0

        # Set the amount of time the circle will take to turn around (seconds)
        self.period = 8
        self.speed = self.period*60

        # Event queue
        self.events = set()

        # Camera pos x, y, z
        self.cam = [0,0,0]

        self.left, self.right, self.up, self.down, self.rot_right, self.rot_left, self.rot_up, self.rot_down= [False for i in range(8)]

        # Cubes coordinates x, y, z
        root3 = 1/(3**0.5)
        self.pos = [
        [0,-1,0],
        [root3,root3,root3],
        [root3,root3,-root3],
        [-root3,root3,-root3],
        [-root3,root3,root3]
        ]
        # Tell the program how to link each coordinate, this list is created based on self.pos
        self.join = [
        [0,1], [0,2], [0,3], [0,4],
        [1,2], [2,3], [3,4], [4,1]
        ]

        self.faces = {
        (0,1,2): (87, 199, 208),
        (0,2,3): (150, 253, 109),
        (0,3,4): (203, 103, 211),
        (0,4,1): (238, 226, 0),
        (1,2,3,4): (0, 0, 238)
        }

    def input_events(self):
        for event in self.events:
            if event[0] == pygame.KEYDOWN:
                if event[1] == pygame.K_a:
                    self.left = True
                if event[1] == pygame.K_w:
                    self.up = True
                if event[1] == pygame.K_d:
                    self.right = True
                if event[1] == pygame.K_s:
                    self.down = True
                if event[1] == pygame.K_RIGHT:
                    self.rot_right = True
                if event[1] == pygame.K_LEFT:
                    self.rot_left = True
                if event[1] == pygame.K_UP:
                    self.rot_up = True
                if event[1] == pygame.K_DOWN:
                    self.rot_down = True

            if event[0] == pygame.KEYUP:
                if event[1] == pygame.K_a:
                    self.left = False
                if event[1] == pygame.K_w:
                    self.up = False
                if event[1] == pygame.K_d:
                    self.right = False
                if event[1] == pygame.K_s:
                    self.down = False
                if event[1] == pygame.K_RIGHT:
                    self.rot_right = False
                if event[1] == pygame.K_LEFT:
                    self.rot_left = False
                if event[1] == pygame.K_UP:
                    self.rot_up = False
                if event[1] == pygame.K_DOWN:
                    self.rot_down = False
        self.events = set()

    def move_cam(self):
        self.input_events()
        if self.left:
            self.cam[0] -= 2
        if self.up:
            self.cam[1] -= 2
        if self.right:
            self.cam[0] += 2
        if self.down:
            self.cam[1] += 2
        if self.rot_right:
            self.counterx+= 1
        if self.rot_left:
            self.counterx-= 1
        if self.rot_up:
            self.countery -= 1
        if self.rot_down:
            self.countery += 1

        # Increase the counter vale to increase the anglexx the cube has
        if self.counterx == self.speed:
            self.counterx = 0
        # Increase the counter vale to increase the anglexy the cube has
        if self.countery == self.speed:
            self.countery = 0

    def get_xyz(self):
        # Create a list with the x,y and z values of each vertice
        points = []
        for i in self.pos:
            anglex = 2*self.counterx*math.pi/self.speed
            angley = 2*self.countery*math.pi/self.speed

            x = (math.cos(anglex)*i[0] - math.sin(anglex)*i[2])
            z = (math.cos(anglex)*i[2] + math.sin(anglex)*i[0])

            y = (math.cos(angley)*i[1] - math.sin(angley)*z)
            z = (math.cos(angley)*z + math.sin(angley)*i[1])


            x = self.cam[0] + 50*x
            y = self.cam[1] + 50*y
            z = self.cam[2] + 50*z

            points.append((x, y, z))
        return points

    def update(self):
        self.clock.tick(60)

        self.move_cam()

        self.points = self.get_xyz()

    def draw_polygons(self):
        face_hire = {}
        for face in self.faces.keys():
            z = 0
            for point in face:
                z += self.points[point][2]
            face_hire[z] = face

        depths = list(face_hire.keys())
        depths.sort()
        depths.reverse()
        for face in depths:
            f = [self.points[point][:2] for point in face_hire[face]]
            pygame.draw.polygon(self.surface, self.faces[face_hire[face]], f)

    def draw(self):
        # self.draw_polygons()
        for j in self.join:

            pygame.draw.line(self.surface, (255,255,255), self.points[j[0]][:2], self.points[j[1]][:2])

class Main:

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

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            self.animation.events.add((event.type, event.key))

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

theApp = Main()
theApp.on_execute()
