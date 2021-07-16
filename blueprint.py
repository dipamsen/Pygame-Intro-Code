from colors import *
import pygame
# unnecessary imports for vscode intellisense
import pygame.display
import pygame.time
import pygame.draw
import pygame.mouse
import pygame.event
import pygame.image
import pygame.transform

import math


pygame.init()


FPS = 60
WIDTH = 400
HEIGHT = 400

pygame.display.set_caption("PyGame: Sketch Title")
pygame.display.set_icon(pygame.image.load("logo.png"))

win = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()


def redraw_game_window():
  pygame.display.update()
  win.fill(DARK_GREY)


# mainloop
run = True
while run:

  redraw_game_window()

  MOUSE = pygame.mouse.get_pos()

  pygame.draw.circle(win, (150, 150, 150), MOUSE, 20)
  pygame.draw.circle(win, WHITE, MOUSE, 20, 2)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  clock.tick(FPS)


pygame.quit()
