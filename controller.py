import math
import random
import pygame
import model
from eventmanager import *

class Controllee:
    def __init__(self):

        self.archerX = 370
        self.archerY = 480
        self.archerX_change = 0

        self.targetX = []
        self.targetY = []
        self.targetX_change = []
        self.targetY_change = []
        self.num_of_enemies = 6

        for i in range(self.num_of_enemies):
            self.targetX.append(random.randint(0, 736))
            self.targetY.append(random.randint(50, 150))
            self.targetX_change.append(4)
            self.targetY_change.append(40)

        self.arrowX = 0
        self.arrowY = 480
        self.arrowX_change = 0
        self.arrowY_change = 10
        self.arrow_state = "ready"

        self.textX = 10
        self.testY = 10

        self.arrow_state = "ready"

    def run(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.archerX_change = -5
                    if event.key == pygame.K_RIGHT:
                        self.archerX_change = 5
                    if event.key == pygame.K_SPACE:

                        if self.arrow_state is "ready":
                            arrowSound = mixer.Sound("Assets\\Music\\swoosh.wav")
                            arrowSound.play()
                            # Get the current x cordinate of the archer
                            self.arrowX = self.archerX
                            self.fire_arrow()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.archerX_change = 0


game = Controllee()
if __name__ == "__main__":
    game.run()