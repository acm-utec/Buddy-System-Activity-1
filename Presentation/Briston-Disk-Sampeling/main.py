import pygame
from simple_dskSmp import poisson_disc_samples

def draw_circle(screen, x, y, radious):
    pygame.draw.circle(screen, (0,0,0), (x, y), radious, 1) 


pygame.init()

height = 800
width = 600 

screen = pygame.display.set_mode([height,width])
BgrColor = [255, 255, 255]

# determines the concentration of points
# the lower the value the more points there are
# [radious, INF)
min_distance = 9
radious = 2

# width,height,radious
points = poisson_disc_samples(height,width , min_distance)

print(points)

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
    screen.fill(BgrColor)
    for point in points:
        pygame.draw.circle(screen, (0,0,0), (point[0]  , point[1] ) , radious) 
    pygame.display.update()