import pygame, sys, math, time
from figures import *


class Manage_events:

        # Set a counter for the automatic rotation of the cube
        counterx, countery, counterz = 0, 0, 0

        # Import pygame display surface and its width and height
        surface = surface
        width, height = [i//2for i in surface.get_size()]

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

        def input_events(self):
            for event in events:
                if event[1] == pygame.K_a: left = not left
                if event[1] == pygame.K_w: up = not up
                if event[1] == pygame.K_d: right = not right
                if event[1] == pygame.K_s: down = not down
                if event[1] == pygame.K_RIGHT: rot_right = not rot_right
                if event[1] == pygame.K_LEFT: rot_left = not rot_left
                if event[1] == pygame.K_UP: rot_up = not rot_up
                if event[1] == pygame.K_DOWN: rot_down = not rot_down
                if event[1] == pygame.K_SPACE: rot_barrell = not rot_barrell

                if event[1] == pygame.K_p: front = not front
                if event[1] == pygame.K_l: back = not back

            events = set()

        def move_cam(self):
            input_events()
            if left: cam[0] -= 2
            if right: cam[0] += 2
            if up: cam[1] -= 2
            if down: cam[1] += 2
            if front: cam[2] -= 2
            if back: cam[2] += 2
            if rot_up: counterx -= 1
            if rot_down: counterx += 1
            if rot_left: countery -= 1
            if rot_right: countery+= 1
            if rot_barrell: counterz += 1

            # Increase the counter vale to increase the anglexx the cube has
            if counterx == speed:
                counterx = 0
            # Increase the counter vale to increase the anglexy the cube has
            if countery == speed:
                countery = 0
            if counterz == speed:
                counterz = 0

        def rot_algor(self, x, y, angle):
            cos = math.cos(angle)
            sin = math.sin(angle)
            axis_1 = (cos*x - sin*y)
            axis_2 = (cos*y + sin*x)

            return axis_1, axis_2

        def get_xyz(self):
            # Create a list with the x,y and z values of each vertice
            points = []
            anglex = 2*counterx*math.pi/speed
            angley = 2*countery*math.pi/speed
            anglez = 2*counterz*math.pi/speed

            for i in self.pos:
                x,y,z = i
                x, z = self.rot_algor(x, z, angley)
                y, z = self.rot_algor(y, z, anglex)
                x, y = self.rot_algor(x, y, anglez)

                x = cam[0] + 50*x
                y = cam[1] + 50*y
                z = cam[2] + 50*z

                points.append((x, y, z))
            return points

        def get_xy(self, x, y, z):
            planex = width + 400*(x)/(z+1000)
            planey = height + 400*(y)/(z+1000)
            return (planex, planey)

        def get_2d(self, cord_3d):
            points = []
            for cord in cord_3d:
                x, y = get_xy(cord[0], cord[1], cord[2])
                points.append((x,y))
            return points
            
class Figure(Manage_events):
    def __init__(self, surface, figure):
        # Cubes coordinates x, y, z
        self.pos = figure.pos
        # Tell the program how to link each coordinate, this list is created based on self.pos
        self.join = figure.join

        self.faces = figure.faces

        self.colors = figure.colors



    def update(self):
        self.cord_3d = self.get_xyz()
        self.cord_2d = self.get_2d(self.cord_3d)

    def draw_polygons(self):
        depths = []
        for face in self.faces:
            depths.append([sum([self.cord_3d[point][cor]**2  for point in face for cor in range(3)])])
        return depths
        # for cord in self.cord_3d:
        #     depth_dict[cord[2]] = cord
        #
        # sort_cord = list(depth_dict.keys())
        # sort_cord.sort()
        # closest_point = self.cord_3d.index(depth_dict[sort_cord[0]])
        #
        # selected_faces = {}
        # for face in self.faces:
        #     if closest_point in face:
        #         f = [self.cord_2d[i] for i in face]
        #         z = sum([self.cord_3d[i][2] for i in face])
        #         selected_faces[z] = [f, self.faces[face]]
        # sort_cord = list(selected_faces.keys())
        # sort_cord.sort()
        # sort_cord.reverse()
        # for face in sort_cord:
        #     pygame.draw.polygon(self.surface, selected_faces[face][1], selected_faces[face][0])


        # sort_cord = []
        # for key in sorted(depth_dict.iterkeys()):
        #     sort_cord.append([key,depth_dict[key]])
        # sort_cord.reverse()
        # closest_point = self.cord_3d.index(sort_cord[0][1])

        # selected_faces = {}
        # for face in self.faces:
        #     if closest_point in face:
        #         f = [self.cord_2d[i] for i in face]
        #         z = sum([self.cord_3d[i][2] for i in face])
        #         selected_faces[z] = [f, self.faces[face]]
        # sort_cord = list(selected_faces.keys())
        # sort_cord.sort()
        # sort_cord.reverse()
        # for face in sort_cord:
        #     pygame.draw.polygon(self.surface, selected_faces[face][1], selected_faces[face][0])
    #
    #
    #
    # def draw(self):
    #     self.draw_polygons()
    #     for j in self.join:
    #         pygame.draw.line(self.surface, (255,255,255), self.cord_2d[j[0]], self.cord_2d[j[1]])
    #



class Animation():

    def __init__(self, surface, *args):
        self.surface = surface
        self.figures = args

    def update_all(self):
        for figure in self.figures:
            figure.update()

    def draw_all(self):
        face_color = []
        depths = []
        face_list = []
        for figure in self.figures:
            for i in range(len(figure.faces)):
                face_list.append([figure.cord_2d[point] for point in figure.faces[i]])
                face_color.append(figure.colors[i])
                depths.append([sum([figure.cord_3d[point][2]**3  for point in figure.faces[i]])])
        ordered = depths[:]
        ordered.sort()
        ordered.reverse()
        for i in ordered:
            p = depths.index(i)
            pygame.draw.polygon(self.surface, face_color[p], face_list[p])



class Main:

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

        self.piram = Figure(self._display_surf, Piram)
        self.piram1 = Figure(self._display_surf, Piram1)
        self.cube = Figure(self._display_surf, Cube)
        self.Animation = Animation(self._display_surf, self.piram, self.piram1, self.cube)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            for figure in self.Animation.figures:
                figure.events.add((event.type, event.key))

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
