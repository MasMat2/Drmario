import pygame, random, sys, copy, time
from pygame.locals import   *

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)
COLORS = [BLUE,GREEN,YELLOW,PURPLE]



class Observer:

    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, player_status):
        for observer in self.observers:
            observer.on_notify(player_status)
    def on_notify():
        pass

class Block(Observer):
    def __init__(self, surface):
        super().__init__()
        
        self.surface = surface
        self.blocks_dict = {}
        self.floating_blocks = None

    def tetris(self, player_status):
        # For the tail and head of the player object check if a line was created
        def find_streak(dire):
            # Check if a row with same block colors was created after placing the player
            # This will got to the last block with the same color in a line (dire=1)
            # and reverse (dire=-1) to take into account the blocks on both sides
            new_block_color = init_color
            streak = 0
            while True:
                new_block[0] += (direction[0] * 24)*dire
                new_block[1] += (direction[1] * 24)*dire
                try:
                    new_block_color = self.surface.get_at(new_block)
                except IndexError:
                    new_block_color = None
                if init_color != new_block_color:
                    break
                streak += 1

            return streak

        def delete_blocks():
            if streak > 3:
                for loop in range(streak):
                    new_block[0] += direction[0] * 24
                    new_block[1] += direction[1] * 24
                    if new_block not in ghost_block: ghost_block.append(new_block[:])
                    self.blocks_dict.pop(tuple(new_block), None)

        def is_floating(block):
            comp_points = [(0,-1),(1,0),(0,1),(-1,0)]
            for point in comp_points:
                lonely_block = block[:]
                lonely_block[0] += 24*point[0]
                lonely_block[1] += 24*point[1]
                if tuple(lonely_block) in self.blocks_dict:
                    if block == cur_gblock:
                        return is_floating(lonely_block)
                    else:
                        return None
            if block == cur_gblock:
                return None
            else:
                return block

        up_right = ([0,-1], [1,0])
        ghost_block = []
        for slice in player_status:
            init_color = self.surface.get_at(slice[0])

            for direction in up_right:
                new_block = list(slice[0])
                find_streak(1)
                streak = find_streak(-1)

                # Delete the lines formed and return list of deleted blocks
                delete_blocks()
                floating_blocks = []
                for cur_gblock in ghost_block:
                    float_block = is_floating(cur_gblock)
                    if float_block:
                        floating_blocks.append(float_block)
        return floating_blocks


    def on_notify(self, player_status):
        # Add player to the block dictionary and check if it has created a row or line with the same color
        first, last = [(player_status[i][0], player_status[i][1]) for i in range(2)]
        for pos_color in first, last:
            self.blocks_dict[pos_color[0]] = pos_color[1]
        self.floating_blocks = self.tetris(player_status)


    def draw(self):
        for block in self.blocks_dict:
            color = self.blocks_dict[block]
            pygame.draw.rect(self.surface, COLORS[color], (block[0], block[1], 24, 24), 0)

class Player(Observer):

    def __init__(self, surface):

        super().__init__()

        self.speed = 24

        self.width, self.height = 24, 24

        self.surface = surface

        self.clock = pygame.time.get_ticks()

        self.on_init()

    def on_init(self):
        self.rect_left, self.rect_top = 0, 0
        self.color = (int(random.random()*4), int(random.random()*4))

        self.config = self.change_config()
        self.rect_config = next(self.config)

        self.events = set()
        self.player_position = self.correct_pos()


    def input_events(self):
        for event in self.events:
            if event == pygame.K_UP:
                self.rect_top -= self.speed

            if event in (pygame.K_DOWN, pygame.K_s, pygame.K_x, pygame.K_k):
                self.rect_top += self.speed
                self.clock = pygame.time.get_ticks()

            if event in (pygame.K_RIGHT, pygame.K_d, pygame.K_l):
                self.rect_left += self.speed

            if event in (pygame.K_LEFT, pygame.K_a, pygame.K_j):
                self.rect_left -= self.speed

            if event in (pygame.K_SPACE, 0):
                self.rect_config = next(self.config)
        if pygame.time.get_ticks()-self.clock > 1000:
            self.rect_top += self.speed
            self.clock = pygame.time.get_ticks()

    def change_config(self):
        while True:
                yield [(0,0),(1,0)]
                yield [(0,0),(0,-1)]
                yield [(1,0),(0,0)]
                yield [(0,-1),(0,0)]

    def get_pos(self):
        self.first_left = self.rect_left + self.rect_config[0][0] * self.width
        self.first_top = self.rect_top + self.rect_config[0][1] * self.height
        self.last_left = self.rect_left + self.rect_config[1][0] * self.width
        self.last_top = self.rect_top + self.rect_config[1][1] * self.height

    def correct_pos(self):
            self.get_pos()

            width_limit = self.surface.get_width() - self.width
            height_limit = self.surface.get_height() - self.height

            if self.first_left < 0 or self.last_left < 0:
                self.rect_left += self.width
            elif self.first_left > width_limit or self.last_left > width_limit:
                self.rect_left -= self.width

            if self.first_top < 0 or self.last_top < 0:
                self.rect_top += self.height
            elif self.first_top > height_limit or self.last_top > height_limit:
                self.rect_top -= self.height

            self.get_pos()
            self.events = set()

            return ((self.first_left, self.first_top), (self.last_left, self.last_top))

    def touch_block(self, player_position):
        first, last = [(i[0], i[1] + self.height) for i in player_position]
        pos_to_check = [i for i in (first, last) if i not in player_position]

        color_to_check = []
        for i in pos_to_check:
            try:
                color_to_check.append(self.surface.get_at(i))
            except IndexError:
                return True
        for pos_color in color_to_check:
            if BLACK != pos_color:
                return True
        return None

    def update(self):
        if self.touch_block(self.player_position):
            player_status = [(self.player_position[i], self.color[i]) for i in range(2)]
            self.notify_observers(player_status)
            self.on_init()

        self.input_events()
        self.player_position = self.correct_pos()


    def draw(self):
        pygame.draw.rect(self.surface, COLORS[self.color[0]], (self.first_left, self.first_top, self.width, self.height), 0)
        pygame.draw.rect(self.surface, COLORS[self.color[1]], (self.last_left, self.last_top, self.width, self.height), 0)

class Game:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 480, 480

    def on_init(self):
        # Pygame parameters
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

        # Player objects
        self.blocks = Block(self._display_surf)
        self.player = Player(self._display_surf)
        self.blocks.register_observer(self.player)
        self.player.register_observer(self.blocks)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # Gameplay input
        if event.type == pygame.KEYDOWN:
            self.player.events.add(event.key)

    def on_loop(self):
        self.player.update()

    def on_render(self):
        self._display_surf.fill(BLACK)
        self.player.draw()
        self.blocks.draw()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == '__main__' :
    theGame = Game()
    theGame.on_execute()
