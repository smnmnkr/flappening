from entities.particle import Particle

from config.bird import bird
from config.util import colors


class Bird(Particle):
    def __init__(self,
                 screen,
                 velocity: float = bird['startVelocity'],
                 maxVelocity: float = bird['maxVelocity'],
                 lift: int = bird['lift']):

        super().__init__(
            screen,
            size=bird['size'],
            position=bird['startPosition'],
            color=colors['red'],
        )

        self.alive: bool = True
        self.score: int = 0

        self.velocity: float = velocity
        self.maxVelocity: float = maxVelocity
        self.lift: float = lift

    def draw(self):
        super().draw()

    def move(self, flapped: bool = False):

        if flapped:
            self.position[1] -= self.lift
            self.velocity *= 0.9

        else:
            self.position[1] += self.velocity

            if (self.velocity < self.maxVelocity):
                self.velocity *= 1.1
