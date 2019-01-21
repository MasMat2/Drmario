class Physics():

    def __init__(self):
        self.counterx, self.countery, self.counterz = 0, 0, 0
        self.width, self.height = [256,256]

        # Set a counter for the automatic rotation of the cube
        self.counterx, self.countery, self.counterz = 0, 0, 0

        # Set the amount of time the circle will take to turn around (seconds)
        self.period = 8
        self.speed = self.period*60

        # Event queue
        self.events = set()

        # Camera pos x, y, z
        self.cam = [0,0,0]

        self.left, self.right, self.up, self.down, self.front, self.back = [False for i in range(6)]
        self.rot_right, self.rot_left, self.rot_up, self.rot_down, self.rot_barrell= [False for i in range(5)]

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

        events = set()

    def move_cam(self):
        self.input_events()
        if left: self.cam[0] -= 2
        if right: self.cam[0] += 2
        if up: self.cam[1] -= 2
        if down: self.cam[1] += 2
        if front: self.cam[2] -= 2
        if back: self.cam[2] += 2
        if rot_up: self.counterx -= 1
        if rot_down: self.counterx += 1
        if rot_left: self.countery -= 1
        if rot_right: self.countery+= 1
        if rot_barrell: self.counterz += 1

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

    def get_xyz(self):
        # Create a list with the x,y and z values of each vertice
        points = []
        anglex = 2*self.counterx*math.pi/self.speed
        angley = 2*self.countery*math.pi/self.speed
        anglez = 2*self.counterz*math.pi/self.speed

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
        planex = self.width + 400*(x)/(z+1000)
        planey = self.height + 400*(y)/(z+1000)
        return (planex, planey)

    def get_2d(self, cord_3d):
        points = []
        for cord in cord_3d:
            x, y = get_xy(cord[0], cord[1], cord[2])
            points.append((x,y))
        return points

class Figure():
    def __init__(self, surface, figure, physics):
        self.physics = physics
        # Cubes coordinates x, y, z
        self.pos = figure.pos
        # Tell the program how to link each coordinate, this list is created based on self.pos
        self.join = figure.join
        self.faces = figure.faces
        self.colors = figure.colors

    def update(self):
        self.cord_3d = self.physics.get_xyz()
        self.cord_2d = self.physics.get_2d(self.cord_3d)

    def draw_polygons(self):
        depths = []
        for face in self.faces:
            depths.append([sum([self.cord_3d[point][cor]**2  for point in face for cor in range(3)])])
        return depths

class Animation():

    def __init__(self, surface, physics, *args):
        self.surface = surface
        self.figures = args
        self.physics = physics

    def update_all(self):
        self.physics.move_cam()
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



a = Physics()
b = Figure(a)

Figure(a)
Animation(surface, a, figures)
