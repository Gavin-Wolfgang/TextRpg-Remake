import pygame, time, random, os, math
from Visuals import*
from Battle import*
from Save import*
from Shoppes import*
from Text import*

pygame.init()
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Battle")
clock = pygame.time.Clock()

KEY_REPEAT_SETTING = (200,70)
pygame.key.set_repeat(*KEY_REPEAT_SETTING)

global inputText, charInfo, buttonNeutral, buttonActive, background
charInfo = {"hp": [15,15], "mp": [5,5], "lvl": 1, "str": 2, "int": 2, "weapon": ["wooden dagger",1,3], "def": 0, "armor": "None", 
			"rune": "None", "gold": 50000, "potions": [0,0,0,0], "stats":{"kills": 0, "champ kills": 0, "chests": 0}, "spells": [0,0,0,0],
			"shield": "None", "amulet": "None", "exp": 0, "class": ""}
#w=145 h=36
buttonNeutral = pygame.image.load('GRAPHICS\\button_neutral.bmp')
buttonActive = pygame.image.load('GRAPHICS\\button_hover.bmp')


black =			(  0,  0,  0)
white = 		(255,255,255)
red = 			(200,  0,  0)
blue = 			(  0,  0,200)
green =			(  0,200,  0)
bright_red = 	(255,  0,  0)
bright_green = 	(  0,255,  0)
yellow =        (255, 255, 0)
something = 	(100,100,100)

class game_intro():
	def __init__(self):
		global charInfo, inputText,buttonNeutral, buttonActive
		intro = True
		self.location = 0

		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			if(self.location == 0):
				button_image(gameDisplay,"New Game", 400-73,215,145,36,buttonNeutral,buttonActive,self.create_char_screen)
				button_image(gameDisplay,"Load Game", 400-73,315,145,36,buttonNeutral,buttonActive,self.load_char_screen)

			elif(self.location == 1):
				button_image(gameDisplay,"Load Slot 1",400-73,85,145,36,buttonNeutral,buttonActive,self.load_char,1)
				button_image(gameDisplay,"Load Slot 2",400-73,185,145,36,buttonNeutral,buttonActive,self.load_char,2)
				button_image(gameDisplay,"Load Slot 3",400-73,285,145,36,buttonNeutral,buttonActive,self.load_char,3)
				button_image(gameDisplay,"Load Slot 4",400-73,385,145,36,buttonNeutral,buttonActive,self.load_char,4)
				button_image(gameDisplay,"Back to Main",400-73,485,145,36,buttonNeutral,buttonActive,self.back_main)

			elif(self.location == 2):
				#print_text(gameDisplay,msg,font,point,color,location)
				#def print_text_center(gameDisplay,msg,font,point,color,xr,xl,yb,yt):
				print_text_center(gameDisplay,"Choose Difficulty","arial",25,white,DISPLAY_WIDTH,0,50,0)
				button_image(gameDisplay,"Easy",400-73,85,145,36,buttonNeutral,buttonActive,self.set_difficulty,.5)
				button_image(gameDisplay,"Normal",400-73,185,145,36,buttonNeutral,buttonActive,self.set_difficulty,1)
				button_image(gameDisplay,"Hard",400-73,285,145,36,buttonNeutral,buttonActive,self.set_difficulty,1.5)
				button_image(gameDisplay,"Very Hard",400-73,385,145,36,buttonNeutral,buttonActive,self.set_difficulty,2)
				button_image(gameDisplay,"Back to Main",400-73,485,145,36,buttonNeutral,buttonActive,self.back_main)

			elif(self.location == 3):
				print_text_center(gameDisplay,"Choose Your Class","arial",25,white,DISPLAY_WIDTH,0,50,0)
				button_image(gameDisplay,"Warrior",250-73,85,145,36,buttonNeutral,buttonActive,self.set_class,"warrior")
				button_image(gameDisplay,"Mage",550-73,85,145,36,buttonNeutral,buttonActive,self.set_class,"mage")
				self.warrior_text()
				self.mage_text()
				button_image(gameDisplay,"Back to Main",400-73,485,145,36,buttonNeutral,buttonActive,self.back_main)

			elif(self.location == 4):
				intro = False

			pygame.display.update()
			clock.tick(15)

		main_menu()
	def load_char_screen(self):
		self.location = 1

	def create_char_screen(self):
		self.location = 2

	def back_main(self):
		self.location = 0

	def set_difficulty(self,difficulty):
		global charInfo
		charInfo.update({"difficulty": difficulty})
		self.location = 3

	def warrior_text(self):
		print_text(gameDisplay,"+ 5 HP","arial",15,white,(250-73,125))
		print_text(gameDisplay,"+ Leather Armor","arial",15,white,(250-73,145))
		print_text(gameDisplay,"+ 1 Strength","arial",15,white,(250-73,165))
		print_text(gameDisplay,"Base Level: +3HP/+1MP","arial",15,white,(250-73,185))

	def mage_text(self):
		print_text(gameDisplay,"+ 3 MP","arial",15,white,(550-73,125))
		print_text(gameDisplay,"+ Cure Spell","arial",15,white,(550-73,145))
		print_text(gameDisplay,"+ Weak Fireball Spell","arial",15,white,(550-73,165))
		print_text(gameDisplay,"Base Level: +1HP/+2MP","arial",15,white,(550-73,185))

	def set_class(self, char_class):
		global charInfo
		charInfo.update({"class": char_class})
		if(char_class == "warrior"):
			charInfo["hp"][0] += 5
			charInfo["hp"][1] += 5
			charInfo["str"] += 1
			charInfo["armor"] = ["leather armor", 1]
			charInfo["class"] = char_class
		elif(char_class == "mage"):
			charInfo["mp"][0] += 3
			charInfo["mp"][1] += 3
			charInfo["int"] += 1
			charInfo["spells"][0] = True
			charInfo["spells"][1] = True
			charInfo["class"] = char_class
		else:
			exit()
		self.location = 4
		print(charInfo)


	def load_char(self,slot):
		global charInfo
		print("trying to load")
		print(slot)
		print(char_exists(slot))
		if(char_exists(slot)):
			print("loading char")
			charInfo = char_import(slot)
			print(charInfo)
			self.location = 4


class main_menu():
	def __init__(self, location=0):
		global charInfo, inputText,buttonNeutral, buttonActive
		mainText = main_text(gameDisplay,charInfo)
		loop = True
		self.location = location

		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			if(self.location == 0):
				mainText.intro_text()
				button_image(gameDisplay,"Continue",400-73,385,145,36,buttonNeutral,buttonActive,self.change_loc, 1)
			
			elif(self.location == 1):
				button_image(gameDisplay,"Stats/Inventory",250-73,200,145,36,buttonNeutral,buttonActive,self.change_loc, 2)
				button_image(gameDisplay,"Enter Shops",550-73,200,145,36,buttonNeutral,buttonActive,self.change_loc, 3)
				button_image(gameDisplay,"Sleep at Inn",250-73,300,145,36,buttonNeutral,buttonActive,self.change_loc, 4)
				button_image(gameDisplay,"Go Exploring",550-73,300,145,36,buttonNeutral,buttonActive,self.change_loc, 5)
				button_image(gameDisplay,"Visit Questgiver",250-73,400,145,36,buttonNeutral,buttonActive,self.change_loc, 6)
				button_image(gameDisplay,"Visit Dungeon",550-73,400,145,36,buttonNeutral,buttonActive,self.change_loc, 7)
				button_image(gameDisplay,"Save",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 10)
			
			#Stats
			elif(self.location == 2):
				#print_text(gameDisplay,msg,font,point,color,location)
				mainText.stats()
				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Shops
			elif(self.location == 3):
				button_image(gameDisplay,"Armor Smith",100,100,145,36,buttonNeutral,buttonActive,self.change_loc,3.1)
				button_image(gameDisplay,"Weapon Smith",300,100,145,36,buttonNeutral,buttonActive,self.change_loc,3.2)
				button_image(gameDisplay,"Mage's Tower",500,100,145,36,buttonNeutral,buttonActive,self.change_loc,3.3)
				button_image(gameDisplay,"Apothecary",100,150,145,36,buttonNeutral,buttonActive,self.change_loc,3.4)
				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Armor Smith
			elif(self.location == 3.1):
				self.display_armor()
				button_image(gameDisplay,"Back",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 3)

			#Weapon Smith
			elif(self.location == 3.2):
				self.display_weapon()
				button_image(gameDisplay,"Back",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc,3)

			#Mage Tower
			elif(self.location == 3.3):
				self.display_rune()
				button_image(gameDisplay,"Back",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 3)

			#Apothecary
			elif(self.location == 3.4):
				self.display_potion()
				mainText.potions()
				button_image(gameDisplay,"Back",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 3)



			#Inn
			elif(self.location == 4):
				text = "The Inn costs " + str(5+charInfo["lvl"]) + " gold"
				print_text_center(gameDisplay,text,"arial",20,white,DISPLAY_WIDTH,0,DISPLAY_HEIGHT-100,0)
				button_image(gameDisplay,"Sleep at Inn",400-73,300,145,36,buttonNeutral,buttonActive,self.reset_hp)
				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Explore
			elif(self.location == 5):
				button_image(gameDisplay,"Forrest (Level 1)",100,100,145,36,buttonNeutral,buttonActive,self.battle_start, "forrest")
				button_image(gameDisplay,"Cave (Level 4)",300,100,145,36,buttonNeutral,buttonActive,self.battle_start, "cave")
				button_image(gameDisplay,"River (Level 8)",100,200,145,36,buttonNeutral,buttonActive,self.battle_start, "river")
				button_image(gameDisplay,"Harlech House (Level 12)",300,200,145,36,buttonNeutral,buttonActive,self.battle_start, "harlech_house")
				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Quest
			elif(self.location == 6):

				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Dungeon
			elif(self.location == 7):

				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			elif(self.location == 8):
				if(charInfo["hp"][0] > 0):
					text = "You won!"
					button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc,1)
				else:
					text = "You died!"
					button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc,9)
				print_text_center(gameDisplay,text,"arial",60,white,DISPLAY_WIDTH,0,DISPLAY_HEIGHT,0)
			elif(self.location == 9):
				break

			#save
			elif(self.location == 10):
				button_image(gameDisplay,"Save Slot 1",400-73,85,145,36,buttonNeutral,buttonActive,self.save_char,1)
				button_image(gameDisplay,"Save Slot 2",400-73,185,145,36,buttonNeutral,buttonActive,self.save_char,2)
				button_image(gameDisplay,"Save Slot 3",400-73,285,145,36,buttonNeutral,buttonActive,self.save_char,3)
				button_image(gameDisplay,"Save Slot 4",400-73,385,145,36,buttonNeutral,buttonActive,self.save_char,4)
				button_image(gameDisplay,"Back to Main",400-73,485,145,36,buttonNeutral,buttonActive,self.change_loc,1)

			pygame.display.update()
			clock.tick(15)

		if(self.location == 9):
			game_intro()
	
	#--------------------------------------------------------------------------

	def change_loc(self, loc):
		self.location = loc

	def reset_hp(self):
		global charInfo
		charInfo["hp"][0] = charInfo["hp"][1]
		charInfo["mp"][0] = charInfo["mp"][1]

	#--------------------------------------------------------------------------

	def battle_start(self, location):
		global charInfo
		start = battle(charInfo,location,gameDisplay)
		charInfo = start.get_charInfo()
		self.location = 8 

	#--------------------------------------------------------------------------

	def save_char(self,slot):
		global charInfo
		save(slot,charInfo)
		print("saved to slot "+str(slot))

	#--------------------------------------------------------------------------

	def display_armor(self):
		button_image(gameDisplay,"Ringmail Armor: 100",100,100,145,36,buttonNeutral,buttonActive,self.buy_item,"ARingmail Armor")
		button_image(gameDisplay,"Chainmail Armor: 200",300,100,145,36,buttonNeutral,buttonActive,self.buy_item,"AChainmail Armor")
		button_image(gameDisplay,"Iron Armor: 350",500,100,145,36,buttonNeutral,buttonActive,self.buy_item,"AIron Armor")
		button_image(gameDisplay,"Steel Armor: 500",100,150,145,36,buttonNeutral,buttonActive,self.buy_item,"ASteel Armor")

	def display_weapon(self):
		button_image(gameDisplay,"Iron Dagger: 100",100,100,145,36,buttonNeutral,buttonActive,self.buy_item,"WIron Dagger")
		button_image(gameDisplay,"Iron Sword: 200",300,100,145,36,buttonNeutral,buttonActive,self.buy_item,"WIron Sword")
		button_image(gameDisplay,"Silver Sword: 400",500,100,145,36,buttonNeutral,buttonActive,self.buy_item,"WSilver Sword")
		button_image(gameDisplay,"Granite Hammer: 700",100,150,145,36,buttonNeutral,buttonActive,self.buy_item,"WGranite Hammer")

	def display_rune(self):
		button_image(gameDisplay,"Health Rune: 500",100,100,145,36,buttonNeutral,buttonActive,self.buy_item,"RHealth Rune")
		button_image(gameDisplay,"Strength Rune: 500",300,100,145,36,buttonNeutral,buttonActive,self.buy_item,"RStrenth Rune")
		button_image(gameDisplay,"Intelligence Rune: 500",300,150,145,36,buttonNeutral,buttonActive,self.buy_item,"RStrenth Rune")
		button_image(gameDisplay,"Defense Rune: 500",500,100,145,36,buttonNeutral,buttonActive,self.buy_item,"RDefense Rune")
		button_image(gameDisplay,"Mana Rune: 500",100,150,145,36,buttonNeutral,buttonActive,self.buy_item,"RMana Rune")

	def display_potion(self):
		button_image(gameDisplay,"Weak Health Potion: 100",100,100,245,36,buttonNeutral,buttonActive,self.buy_item,"PWeak Health Potion")
		button_image(gameDisplay,"Intermediate Health Potion: 200",100,150,245,36,buttonNeutral,buttonActive,self.buy_item,"PHealth Potion")
		button_image(gameDisplay,"Strong Health Potion: 400",100,200,245,36,buttonNeutral,buttonActive,self.buy_item,"PStrong Health Potion")
		button_image(gameDisplay,"Max Health Potion: 700",100,250,245,36,buttonNeutral,buttonActive,self.buy_item,"PMax Health Potion")

	#--------------------------------------------------------------------------

	def buy_item(self,item):
		start = item[:1]
		item = item[1:]
		if(start == "W"):
			print("buying: " + item)
			charInfo["weapon"],charInfo["gold"] = buy_weapon(charInfo["weapon"],charInfo["gold"], item) 
		elif(start == "A"):
			print("buying: " + item)
			charInfo["armor"],charInfo["gold"] = buy_armor(charInfo["armor"],charInfo["gold"], item) 
		elif(start == "R"):
			print("buying: " + item)
			charInfo["rune"],charInfo["gold"] = buy_rune(charInfo["rune"],charInfo["gold"], item) 
		elif(start == "P"):
			print("buying: " + item)
			charInfo["potions"],charInfo["gold"] = buy_health_potion(charInfo["potions"],charInfo["gold"], item) 

	#--------------------------------------------------------------------------

game_intro()
