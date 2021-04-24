import math
import random

import pygame
from pygame import mixer

pygame.init()
mixer.music.load("Assets\\Music\\bgmusic.wav")
mixer.music.play(-1)

pygame.display.set_caption("Archery")
icon = pygame.image.load('Assets\\Sprites\\aim.png')
pygame.display.set_icon(icon)

class Viewee:
    def __init__(self):
        self.num_of_enemies = 6
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('Assets\\Sprites\\background.png')
        self.archerImg = pygame.image.load('Assets\\Sprites\\archer.png')
        self.targetImg = []

        for i in range(self.num_of_enemies):
            self.targetImg.append(pygame.image.load('Assets\\Sprites\\bullseye.png'))

        self.arrowImg = pygame.image.load('Assets\\Sprites\\arrow.png')

        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_score(self):
        score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))
        self.screen.blit(score, (self.textX, self.testY))

    def game_over_text(self):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(over_text, (200, 250))

    def archer(self):
        self.screen.blit(self.archerImg, (self.archerX, self.archerY))

    def target(self, i):
        self.screen.blit(self.targetImg[i], (self.targetX[i], self.targetY[i]))

    def fire_arrow(self):
        self.arrow_state = "fire"
        self.screen.blit(self.arrowImg, (self.arrowX + 16, self.arrowY + 10))

    def run(self):
        while True:

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))



game = Viewee()
if __name__ == "__main__":
    game.run()