import pygame

from config import game
from config import colors


# default particle class (rectangular box):
class Particle:
    def __init__(self,
                 screen,
                 size: list = [0, 0],
                 position: list = [0, 0],
                 color: set = colors['black'],
                 debug: bool = False):
        super().__init__()

        # enables additional printing
        self.debug: bool = debug

        # saves corresponding screen object
        self.screen = screen

        self.size: int = size
        self.position: list = position
        self.color: set = color

    def draw(self):
        # draw.rect(surface[display.obj], color[tuple], rect[left[px], top[px], width[px], height[px]])
        # src: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))

    def getSize(self):

        # debug printing
        if (self.debug):
            print(self.size)

        return self.size

    def getPosition(self):

        # debug printing
        if (self.debug):
            print(self.position)

        return self.position

    # TODO: solve this elegant:
    def getBoxModel(self):

        # p(x,y)px
        p1 = tuple(self.position)  # top left
        p3 = (self.position[0], self.position[1] + self.size[1])  # top right
        p2 = (self.position[0] + self.size[0], self.position[1])  # bottom left
        p4 = (self.position[0] + self.size[0], self.position[1] + self.size[1]
              )  # bottom right

        # debug printing
        if (self.debug):
            print([p1, p2, p3, p4])

        return [p1, p2, p3, p4]

    def inBound(self):

        # check border collision for each point in box model
        for point in self.getBoxModel():

            # check if x is out of bound
            if (point[0] < 0 or point[0] > game['size'][0]):
                return False

            # check if y out of bound
            if (point[1] < 0 or point[1] > game['size'][1]):
                return False

        return True

    def collision(self, particle) -> bool:

        # Rectangle/Rectangle collision
        # src: http://www.jeffreythompson.org/collision-detection/rect-rect.php
        if (self.position[0] + self.size[0] >= particle.position[0]
                and self.position[0] <= particle.position[0] + particle.size[0]
                and self.position[1] + self.size[1] >= particle.position[1] and
                self.position[1] <= particle.position[1] + particle.size[1]):
            return True

        return False
