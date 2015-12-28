import pygame
import time

def update_screen(screen):
	'''
	This function will be the clock which updates the screen 
	while the game is running. 
	TODO: ensure this breaks on a "Quit", probably need a global?
	Maybe some IO threading. Either way, a lot of python purists 
	will be sad. Is there a better way to do it? 
	IO threading doesn't invoke GIL. 
	'''
	for x in range(255):
		screen.fill((x,x,x))
		print x
		pygame.display.update()
		time.sleep(.1)

def keyboard_control():
	'''
	This function will listen for keyboard events and pass them 
	to the controller, possibly the main fuction should handle the 
	whole looping? That has issues where a control event could be 
	delayed by a screen update. But do I actually care? This is a 
	very simple game. 
	'''
	pass


def enemy_control():
	'''
	This is where the logic for the enemy control will come in. 
	This is only for individual enemies, not their type or where in 
	the sequence they come in. That will be handled in stage and
	level control
	'''
	pass

def player_control():
	'''
	This is where I'll store player health and level.
	TODO: Do I want bonuses? Can players get items? If they can 
	we want to put the inventory here. 
	If lives = 0, then we need to reset level, stage, enemy and items.
	'''
	pass

def where_am_i():
	'''
	This is where the level, stage and enemy number is incremented. 
	Will need logic for if enemy = X then enemy = boss
	If boss = dead, level = increment. 
	If level = 3, stage = increment. 
	If stage = 6, game = win. 
	'''
	pass

def stage_control():
	'''
	This is where we'll update the assets for each stage. 
	we'll call this when we increment stages. Probably
	best to make the assets either global or set them in a config
	file and then read from it on stage change. Maybe a dictionary?
	'''
	pass


def main():
    pygame.init()
    #clock = pygame.time.clock()
    screen = pygame.display.set_mode((1024, 768))
    update_screen(screen)

main()