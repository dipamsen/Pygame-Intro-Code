from colors import *
import pygame
import pygame.display
import pygame.time
import pygame.draw
import pygame.mouse
import pygame.event
import pygame.transform
import math

pygame.init()


FPS = 60
WIDTH = 400
HEIGHT = 400


win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Steering Behaviours: Arrive")

clock = pygame.time.Clock()


def redraw_game_window():
  win.fill(DARK_GREY)


def vector_from_polar(polar):
  vec = pygame.Vector2()
  vec.from_polar(polar)
  return vec


class Vehicle:
  def __init__(self, x, y):
    self.pos = pygame.Vector2(x, y)
    self.vel = pygame.Vector2(0, 0)
    self.acc = pygame.Vector2(0, 0)
    self.max_speed = 4
    self.max_force = 0.1

  def display(self):
    heading = self.vel.angle_to(pygame.Vector2(1, 0))

    vertices = [pygame.Vector2(i) for i in [(20, -6), (20, 6), (0, 0)]]
    vertices_rotated = map(lambda x: x.rotate(180 - heading), vertices)

    vertices_translated = list(map(lambda x: self.pos + x, vertices_rotated))
    pygame.draw.polygon(win, (150, 150, 150), vertices_translated)
    pygame.draw.polygon(win, WHITE, vertices_translated, width=2)

  def move(self):
    self.pos += self.vel
    self.vel += self.acc

    self.acc *= 0

  def steer(self, x, y):
    target = pygame.Vector2(x, y)
    desired_vector = target - self.pos
    dist = desired_vector.magnitude()
    try:
      if dist < 100:
        desired_vector.scale_to_length(dist / 100 * self.max_speed)
      else:
        desired_vector.scale_to_length(self.max_speed)
    except ValueError:
      pass
    steer = desired_vector - self.vel
    if steer.magnitude() > self.max_force:
      steer.scale_to_length(self.max_force)
    self.acc += steer


# mainloop
run = True
vh = Vehicle(WIDTH / 2, HEIGHT / 2)
while run:

  redraw_game_window()

  MOUSE = pygame.mouse.get_pos()

  pygame.draw.circle(win, (150, 150, 150), MOUSE, 20)
  pygame.draw.circle(win, WHITE, MOUSE, 20, 2)

  vh.display()
  vh.move()
  vh.steer(*MOUSE)

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  clock.tick(FPS)


pygame.quit()
