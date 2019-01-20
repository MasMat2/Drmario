import pygame, sys, math, time

class Animation:
    def __init__(self, surface):
        # Import pygame display surface and its width and height
        self.surface = surface
        self.width, self.height = [i//2for i in self.surface.get_size()]

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
        self.pos = [
        [1,-1,1],
        [1,-1,-1],
        [-1,-1,-1],
        [-1,-1,1],
        [1,1,1],
        [1,1,-1],
        [-1,1,-1],
        [-1,1,1]
        ]
        # Tell the program how to link each coordinate, this list is created based on self.pos
        self.join = [
        [0,1], [1,2], [2,3], [3,0],
        [4,5], [5,6], [6,7], [7,4],
        [0,4], [1,5], [2,6], [3,7]
        ]

        self.faces = {
        (0,1,2,3): (0, 255, 255),
        (4,5,6,7): (255, 0, 255),
        (0,1,5,4): (255, 255, 0),
        (1,2,6,5): (0, 255, 0),
        (2,3,7,6): (0, 0, 255),
        (3,0,4,7): (255, 0, 0)
        }

    def input_events(self):
        for event in self.events:
            if event[1] == pygame.K_a:
                self.left = not self.left
            if event[1] == pygame.K_w:
                self.up = not self.up
            if event[1] == pygame.K_d:
                self.right = not self.right
            if event[1] == pygame.K_s:
                self.down = not self.down
            if event[1] == pygame.K_RIGHT:
                self.rot_right = not self.rot_right
            if event[1] == pygame.K_LEFT:
                self.rot_left = not self.rot_left
            if event[1] == pygame.K_UP:
                self.rot_up = not self.rot_up
            if event[1] == pygame.K_DOWN:
                self.rot_down = not self.rot_down

        self.events = set()

    def move_cam(self):
        self.input_events()
        if self.left:
            self.cam[0] -= 2
        if self.right:
            self.cam[0] += 2
        if self.up:
            self.cam[1] -= 2
        if self.down:
            self.cam[1] += 2
        if self.rot_left:
            self.counterx -= 1
        if self.rot_right:
            self.counterx+= 1
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

    def get_xy(self, x, y, z):
        zero_z = 500

        planex = self.width + 400*x/(z + zero_z)
        planey = self.height + 400*y/(z + zero_z)

        return (planex, planey)

    def get_2d(self, cord_3d):
        points = []
        for cord in cord_3d:
            x, y = self.get_xy(cord[0], cord[1], cord[2])
            points.append((x,y))
        return points

    def update(self):
        self.clock.tick(60)

        self.move_cam()

        self.cord_3d = self.get_xyz()

        self.points = self.get_2d(self.cord_3d)

    def draw_polygons(self):
        depth_dict = {}
        for cord in self.cord_3d:
            depth_dict[cord[2]] = cord

        sort_cord = list(depth_dict.keys())
        sort_cord.sort()
        closest_point = self.cord_3d.index(depth_dict[sort_cord[0]])

        selected_faces = {}
        for face in self.faces:
            if closest_point in face:
                f = [self.points[i] for i in face]
                z = sum([self.cord_3d[i][2] for i in face])
                selected_faces[z] = [f, self.faces[face]]
        sort_cord = list(selected_faces.keys())
        sort_cord.sort()
        sort_cord.reverse()
        for face in sort_cord:
            pygame.draw.polygon(self.surface, selected_faces[face][1], selected_faces[face][0])


        # sort_cord = []
        # for key in sorted(depth_dict.iterkeys()):
        #     sort_cord.append([key,depth_dict[key]])
        # sort_cord.reverse()
        # closest_point = self.cord_3d.index(sort_cord[0][1])

        # selected_faces = {}
        # for face in self.faces:
        #     if closest_point in face:
        #         f = [self.points[i] for i in face]
        #         z = sum([self.cord_3d[i][2] for i in face])
        #         selected_faces[z] = [f, self.faces[face]]
        # sort_cord = list(selected_faces.keys())
        # sort_cord.sort()
        # sort_cord.reverse()
        # for face in sort_cord:
        #     pygame.draw.polygon(self.surface, selected_faces[face][1], selected_faces[face][0])



    def draw(self):
        self.draw_polygons()
        for j in self.join:
            pygame.draw.line(self.surface, (255,255,255), self.points[j[0]], self.points[j[1]])

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

if __name__ == "__main__":
    theApp = Main()
    theApp.on_execute()
