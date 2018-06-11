# Importing necessary libraries
import pygame
from pygame.locals import *

# Initializing Pygame library
pygame.init()

# Opening the display window
display = pygame.display.set_mode((640, 480), RESIZABLE)

# Loading and pasting the background image
background = pygame.image.load('background.jpg').convert()
display.blit(background, (0,0))

# Loading and pasting of the character
character = pygame.image.load('perso.png').convert_alpha() # = see through transparence
char_position = character.get_rect()
display.blit(character, char_position)

# For Mouse Buttons & Movements:
character_x = 0
character_y = 0
display.blit(character, (character_x, character_y))

# Refreshing Display Window
pygame.display.flip()

# Continuous pressing keys accordding to delay in milliseconds of how mong key is pressed before char movement,
# and time in milliseconds between each movement of char. 
pygame.key.set_repeat(400, 30)

# Endless Loop
carry_on = 1 # Variable to keep the loop going if = 1, stop if = 0
while carry_on:
	for event in pygame.event.get(): # We browse the list of all happening events.
		if event.type == QUIT: # If one of the events is from type QUIT,
# Question for Olivier: why is my .type not in blue like the other imports from pygame?
			carry_on = 0 # Then we stop the loop.
		if event.type == KEYDOWN:
			if event.key == K_DOWN: # if use 'down arrow',
				char_position = char_position.move(0,3) # Then character moves down 3 pixels.
			if event.key == K_UP:
				char_position = char_position.move(0,-3)
			if event.key == K_RIGHT:
				char_position = char_position.move(3,0)
			if event.key == K_LEFT:
				char_position = char_position.move(-3,0)
# Making character move with the mouse clicks:
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1: # if left click,
				# Then we change character coordonnates
				character_x = event.pos[0]
				character_y = event.pos[1]
# Making the character move with the mouse motions:
		if event.type == MOUSEMOTION:
			character_x = event.pos[0]
			character_y = event.pos[1]

	# Reloading and pasting
	display.blit(background, (0,0))
	display.blit(character, char_position)
	display.blit(character, (character_x,character_y))

	# Refresh Display Window
	pygame.display.flip()