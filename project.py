import pygame
import math

def drawgrid(w, rows, surface):
    sizebtwen = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizebtwen
        y = y + sizebtwen

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))


def createwindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawgrid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows

    width = 600
    rows = 12
    surface = pygame.display.set_mode((width, rows))
    check = True
    clock = pygame.time.Clock()
    while check:
        pygame.time.delay(50)
        clock.tick(10)
        createwindow(surface)

    pass

main()
