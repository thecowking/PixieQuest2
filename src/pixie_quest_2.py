import pygame
import time

def update_screen(screen):
	for x in range(255):
		screen.fill((x,x,x))
		print x
		pygame.display.update()
		time.sleep(.1)


def main():
    pygame.init()
    #clock = pygame.time.clock()
    screen = pygame.display.set_mode((1024, 768))
    update_screen(screen)

main()