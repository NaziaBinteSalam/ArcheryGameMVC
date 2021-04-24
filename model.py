import math
import random
import pygame
from eventmanager import *

class Archery:
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


    def isHit(self, idx):
        distance = math.sqrt(
            math.pow(self.targetX[idx] - self.arrowX, 2) + (math.pow(self.targetY[idx] - self.arrowY, 2)))
        if distance < 27:
            return True
        else:
            return False

    def run(self):
        while True:

            self.archerX += self.archerX_change
            if self.archerX <= 0:
                self.archerX = 0
            elif self.archerX >= 736:
                self.archerX = 736

            for i in range(self.num_of_enemies):

                if self.targetY[i] > 440:
                    for j in range(self.num_of_enemies):
                        self.targetY[j] = 2000
                    self.game_over_text()
                    break

                self.targetX[i] += self.targetX_change[i]
                if self.targetX[i] <= 0:
                    self.targetX_change[i] = 4
                    self.targetY[i] += self.targetY_change[i]
                elif self.targetX[i] >= 736:
                    self.targetX_change[i] = -4
                    self.targetY[i] += self.targetY_change[i]

                hit = self.isHit(i)
                if hit:
                    hitSound = mixer.Sound("Assets\\Music\\wood.wav")
                    hitSound.play()
                    self.arrowY = 480
                    self.arrow_state = "ready"
                    self.score_value += 10
                    self.targetX[i] = random.randint(0, 736)
                    self.targetY[i] = random.randint(50, 150)

                self.target(i)

            if self.arrowY <= 0:
                self.arrowY = 480
                self.arrow_state = "ready"

            if self.arrow_state is "fire":
                self.fire_arrow()
                self.arrowY -= self.arrowY_change

            self.archer()
            self.show_score()
            pygame.display.update()


game = Archery()

if __name__ == "__main__":
    game.run()
