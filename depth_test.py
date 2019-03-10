import pygame, sys, math, time, operator
from figures import *

class Physics():

    counterx, countery, counterz = 0, 0, 0
    width, height = [256,256]

    # Set a counter for the automatic rotation of the cube
    counterx, countery, counterz = 0, 0, 0

    # Set the amount of time the circle will take to turn around (seconds)
    period = 8
    speed = period*60

    # Event queue
    events = set()

    # Camera pos x, y, z
    cam = [0,0,0]

    left, right, up, down, front, back = [False for i in range(6)]
    rot_right, rot_left, rot_up, rot_down, rot_barrell= [False for i in range(5)]

    m_side = 10
    m_deep = 30
    ratio = width/(m_side/m_deep)
    zero_z = 50/((1/3)/8) + 50

    def input_events(self):
        for event in self.events:
            if event[1] == pygame.K_a: self.left = not self.left
            if event[1] == pygame.K_w: self.up = not self.up
            if event[1] == pygame.K_d: self.right = not self.right
            if event[1] == pygame.K_s: self.down = not self.down
            if event[1] == pygame.K_RIGHT: self.rot_right = not self.rot_right
            if event[1] == pygame.K_LEFT: self.rot_left = not self.rot_left
            if event[1] == pygame.K_UP: self.rot_up = not self.rot_up
            if event[1] == pygame.K_DOWN: self.rot_down = not self.rot_down
            if event[1] == pygame.K_SPACE: self.rot_barrell = not self.rot_barrell

            if event[1] == pygame.K_p: self.front = not self.front
            if event[1] == pygame.K_l: self.back = not self.back

        self.events = set()
        # print([self.left, self.right, self.up, self.down, self.front, self.back,self.rot_right, self.rot_left, self.rot_up, self.rot_down, self.rot_barrell])

    def move_cam(self):
        self.input_events()
        if self.left: self.cam[0] -= 2
        if self.right: self.cam[0] += 2
        if self.up: self.cam[1] -= 2
        if self.down: self.cam[1] += 2
        if self.front: self.cam[2] -= 2
        if self.back: self.cam[2] += 2
        if self.rot_up: self.counterx -= 1
        if self.rot_down: self.counterx += 1
        if self.rot_left: self.countery -= 1
        if self.rot_right: self.countery+= 1
        if self.rot_barrell: self.counterz += 1

        # Increase the counter vale to increase the anglexx the cube has
        if self.counterx == self.speed:
            self.counterx = 0
        # Increase the self.counter vale to increase the anglexy the cube has
        if self.countery == self.speed:
            self.countery = 0
        if self.counterz == self.speed:
            self.counterz = 0

    def rot_algor(self, x, y, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        axis_1 = (cos*x - sin*y)
        axis_2 = (cos*y + sin*x)

        return axis_1, axis_2

    def get_xyz(self, pos):
        # Create a list with the x,y and z values of each vertice
        points = []
        anglex = 2*self.counterx*math.pi/self.speed
        angley = 2*self.countery*math.pi/self.speed
        anglez = 2*self.counterz*math.pi/self.speed

        for i in pos:
            x,y,z = i
            x, z = self.rot_algor(x, z, angley)
            y, z = self.rot_algor(y, z, anglex)
            x, y = self.rot_algor(x, y, anglez)

            x = self.cam[0] + 50*x
            y = self.cam[1] + 50*y
            z = self.cam[2] + 50*z

            points.append((x, y, z))
        return points


    def get_xy(self, x, y, z):
        planex = self.width + self.ratio*(x)/(z+self.zero_z)
        planey = self.height + self.ratio*(y)/(z+self.zero_z)
        return (planex, planey)

    def get_face_vertex(self, faces, cord_3d):
        face_tuple = ()
        for face in faces:
            face_vertex = []
            for index in face:
                face_vertex.append(tuple(cord_3d[index]))
            face_tuple += tuple(face_vertex),
        return face_tuple

    def get_2d(self, cord_3d):
        points = []
        for cord in cord_3d:
            x, y = self.get_xy(cord[0], cord[1], cord[2])
            points.append((x,y))
        return points

class Figure(Physics):
    def __init__(self, surface, figure):
        # Cubes coordinates x, y, z
        self.pos = figure.pos
        # Tell the program how to link each coordinate, this list is created based on self.pos
        self.faces = figure.faces
        self.colors = figure.colors


    def update(self):
        self.cord_3d = self.get_xyz(self.pos)
        self.face_point_array = self.get_face_vertex(self.faces, self.cord_3d)
        self.cord_2d = self.get_2d(self.cord_3d)

    def draw_polygons(self):
        depths = []
        for face in self.faces:
            depths.append([sum([self.cord_3d[point][cor]**2  for point in face for cor in range(3)])])
        return depths

class Animation(Physics):

    def __init__(self, surface, *args):
        self.surface = surface
        self.figures = args

    def update_all(self):
        self.move_cam()
        for figure in self.figures:
            figure.update()

    def draw_all(self):
        face_color = []
        depths = []
        face_list = []
        point_list = []
        for figure in self.figures:
            for i in range(len(figure.faces)):
                point_list.append((point) for point in figure.faces[i])
                face_list.append([figure.cord_2d[point] for point in figure.faces[i]])
                face_color.append(figure.colors[i])
                depths.append([sum([figure.cord_3d[point][2]*abs(figure.cord_3d[point][2])  for point in figure.faces[i]])])
        ordered = depths[:]
        ordered.sort()
        ordered.reverse()
        for i in ordered:
            p = depths.index(i)
            pygame.draw.polygon(self.surface, face_color[p], face_list[p])

    # def draw_all(self):
    #     # Needs to create the set directly instead of first creating the tuple
    #     face_color = []
    #     face_tuple = ()
    #     for figure in self.figures: face_tuple += (figure.face_point_array)
    #     face_set = {(tup) for tup in face_tuple}
    #     del face_tuple
    #     # for figure in self.figures: face_set.add(figure.face_point_array); print(figure.face_point_array, end="\n\n")
    #     point_list = sorted([point for figure in self.figures for point in figure.cord_3d], key=operator.itemgetter(2))
    #
    #     # face_dict = {}
    #     # for point in point_list:
    #     #     face_dict[point] = []
    #     #     # looop tru faces
    #     #     for face in face_list:
    #     #     # if face has point
    #     #
    #     #     #     face_dict[point].append(face3dcord)



class Main():

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        # Set the clock to keep a frame rate of 60 hertz
        self.clock = pygame.time.Clock()
        a = Figure(self._display_surf, Piram)
        b = Figure(self._display_surf, Piram1)
        c =  Figure(self._display_surf, Cube)
        self.Animation = Animation(self._display_surf, a, b, c)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            Physics.events.add((event.type, event.key))

    def on_loop(self):
        self.Animation.update_all()

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.Animation.draw_all()
        pygame.display.update()
        self.clock.tick(60)

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
