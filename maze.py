import pygame, sys


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       image = pygame.image.load("maze.png")
       self.image.blit(image, (0,0))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()


class Text:
    def __init__(self):
        pygame.font.init() # you have to call this at the start,
                        # if you want to use this module.
        self.myfont = pygame.font.SysFont('Arial', 8)


    def render(self, msg):
        textsurface = self.myfont.render(msg, False, (0, 255, 0))
        return textsurface

text = Text()

def cordinates(surface):
    num = -1
    x = int(surface.get_width())
    for i in range(0,x,11):
        pygame.draw.line(surface, (255,255,0), (i,0), (i,x))
        pygame.draw.line(surface, (255,255,0), (0,i), (x,i))
        if i % 33 == 0:
            num += 1
            surface.blit(text.render(str(num)), (i,0))
            surface.blit(text.render(str(num)), (0,i))



class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True

        self.block = Block((0,255,0), 512, 512)
        self.group = pygame.sprite.Group(self.block)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.group.draw(self._display_surf)
        cordinates(self._display_surf)
        pygame.display.update()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.on_render()

        while True:
            for event in pygame.event.get():
                self.on_event(event)

if __name__ == "__main__":
    theApp = main()
    theApp.on_execute()
