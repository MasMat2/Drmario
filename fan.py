import pygame, sys, math

display = pygame.display.set_mode((255, 255), 0, 32)
count = 0
initial = (255//2, 255//2)
frame = 64

def blur(side, count):
    co = int(math.sin((count)*2*math.pi/(frame*0.5))*side*50)
    ca = int(math.cos((count)*2*math.pi/(frame*0.5))*side*50)
    final = (255//2 + ca, 255//2 + co)
    return final

while True:
    count += 0.8
    count = count % frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill((0,0,0))
    for i in range(2):
        pygame.draw.line(display, (250, 250, 250), initial, blur(1, (frame/8)*i+count))
        pygame.draw.line(display, (250, 250, 250), initial, blur(-1, (frame/8)*i+count))
    if count%8 > 7.9 or count%8 < 0.4:
        final = tuple(i for i in blur(-0.5, 0))
        pygame.Surface.set_at(display, final, (250,0, 0))
    pygame.display.update()
