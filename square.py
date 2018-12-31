import pygame, sys
from pygame.locals import *

display = pygame.display.set_mode((255, 255), 0, 32)

display.fill((0,0,0))
loops = [0+ 10, 234//2 +10, 234 +10]
new = []

for i in loops:
    for j in loops:
        new.append((i,j))
        for point in new:
            pygame.draw.line(display, (0, 250, 0), point, (i,j))

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
