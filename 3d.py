import pygame, sys, math, itertools

pygame.init()
surface = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
counter = 0

cx, cy = [i//2 for i in pygame.display.get_surface().get_size()]

points = [
    (1, 1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (1, 1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (1, -1, -1)
]

connections = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7),
]

def gen():
    while True:
        for i in range(4):
            yield (i*2 + 1)/4

angles = gen()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(30)
    surface.fill((255, 255, 255))

    #
    #
    # new_x = math.cos(math.pi*(1/4 + counter/120))
    # new_z = math.sin(math.pi*(1/4 + counter/120))
    # x = int((new_x/(new_z+2)) * 60) + cx
    # y = int((-1/(new_z+2)) * 60) + cy
    pygame.draw.circle(surface, (0,200,0), (cx, cy), 2)
    # pygame.draw.circle(surface, (0,0,0), (x, y), 4)k


    line_points = []

    for x, y, z in points:

        angle = next(angles)
        # Cos*hip(2**(1/2)) == ca = x
        new_x = (2**(1/2))*math.cos((math.pi)* (angle+ (counter/120)))

        # Sin*hip(2**(1/2)) == co = z
        new_z = (2**(1/2))*math.sin((math.pi)* (angle +(counter/120)))

        new_x = int((new_x/(new_z+4))*80 + cx)
        new_y = int((y/(new_z+4))*80 + cy)
        line_points.append((new_x, new_y))


    for start, end in connections:
        pygame.draw.line(surface, (0,0,0), line_points[start], line_points[end], 1)

    counter += 1
    pygame.display.update()
