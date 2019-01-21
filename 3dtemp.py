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
