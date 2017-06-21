import pygame, time, random, os, math
from Visuals import*

pygame.init()
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Battle")
clock = pygame.time.Clock()

KEY_REPEAT_SETTING = (200,70)
pygame.key.set_repeat(*KEY_REPEAT_SETTING)

global inputText, charInfo, buttonNeutral, buttonActive, background
																						#1 = heal 2 = fire 3 = ice 4 = inferno
charInfo = {"hp": 15, "mp": 5, "lvl": 1, "str": 1, "int": 1, "weapon": None, "armor": None, "spells": [False,False,False,False]}
#w=145 h=36
buttonNeutral = pygame.image.load('GRAPHICS\\button_neutral.png')
buttonActive = pygame.image.load('GRAPHICS\\button_hover.png')


black =			(  0,  0,  0)
white = 		(255,255,255)
red = 			(200,  0,  0)
green =			(  0,200,  0)
bright_red = 	(255,  0,  0)
bright_green = 	(  0,255,  0)
something = 	(100,100,100)

class game_intro():
	def __init__(self):
		global charInfo, inputText,buttonNeutral, buttonActive
		intro = True
		self.location = 0

		self.main_menu()

	def main_menu(self):
		intro = True
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			button_image(gameDisplay,"Next Menu", 400-73,215,145,36,buttonNeutral,buttonActive,self.next_menu)
			button_image(gameDisplay,"Nexter Menu", 400-73,315,145,36,buttonNeutral,buttonActive,self.nexter_menu)

			clock.tick(15)
			pygame.display.update()

	def next_menu(self):
		intro = True
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			button_image(gameDisplay,"Main Menu", 400-73,215,145,36,buttonNeutral,buttonActive,self.main_menu)
			button_image(gameDisplay,"Nexter Menu", 400-73,315,145,36,buttonNeutral,buttonActive,self.nexter_menu)

			clock.tick(15)
			pygame.display.update()

	def nexter_menu(self):
		intro = True
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			button_image(gameDisplay,"Main Menu", 400-73,215,145,36,buttonNeutral,buttonActive,self.main_menu)
			button_image(gameDisplay,"Next Menu", 400-73,315,145,36,buttonNeutral,buttonActive,self.next_menu)

			clock.tick(15)
			pygame.display.update()
text = "AIron Dagger"			
print(text)
print(text[:1])
print(text[1:])