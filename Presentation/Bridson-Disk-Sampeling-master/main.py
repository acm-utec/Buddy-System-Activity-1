import pygame
import timeit
from simple_dskSmp import poisson_disc_samples


def draw_circle(screen, x, y, radious):
    pygame.draw.circle(screen, (0,0,0), (x, y), radious, 1) 


pygame.init()

width = 1200
height = 700 

screen = pygame.display.set_mode([width,height])
BgrColor = [255, 255, 255]

# determines the concentration of points
# the lower the value the more points there are
# [radious, INF)
min_distance = 9
radious = 2

start = timeit.timeit()
# width,height,radious
points = poisson_disc_samples(width,height , min_distance)
end = timeit.timeit()
print(end - start)

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
    screen.fill(BgrColor)
    for point in points:
        pygame.draw.circle(screen, (0,0,0), (point[0]  , point[1] ) , radious) 
    pygame.display.update()