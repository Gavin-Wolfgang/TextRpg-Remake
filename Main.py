import pygame, time, random, os, math
from Visuals import*
from Battle import*
from Save import*
from Shoppes import*

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
charInfo = {"hp": [15,15], "mp": [5,5], "lvl": 1, "str": 2, "int": 2, "weapon": ["wooden dagger",1,3], "armor": "None", 
			#1 = heal 2 = fire 3 = ice 4 = inferno
			"spells": [False,False,False,False], "gold": 50, "stats":{"kills": 0, "champ kills": 0, "chests": 0},
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
		loop = True
		self.location = location

		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			if(self.location == 0):
				self.intro_text()
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
				self.display_stats()
				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Shops
			elif(self.location == 3):
				button_image(gameDisplay,"Armor Smith",100,100,145,36,buttonNeutral,buttonActive,self.change_loc,3.1)
				button_image(gameDisplay,"Weapon Smith",300,100,145,36,buttonNeutral,buttonActive,self.change_loc,3.2)
				button_image(gameDisplay,"Mage's Tower",500,100,145,36,buttonNeutral,buttonActive,self.change_loc,3.3)
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
				button_image(gameDisplay,"Back",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 3)

			#Inn
			elif(self.location == 4):
				text = "The Inn costs " + str(5+charInfo["lvl"]) + " gold"
				print_text_center(gameDisplay,text,"arial",20,white,DISPLAY_WIDTH,0,DISPLAY_HEIGHT-100,0)
				button_image(gameDisplay,"Sleep at Inn",400-73,300,145,36,buttonNeutral,buttonActive,self.reset_hp)
				button_image(gameDisplay,"Main Menu",400-73,500,145,36,buttonNeutral,buttonActive,self.change_loc, 1)

			#Explore
			elif(self.location == 5):
				button_image(gameDisplay,"Cave (Level 4)",100,100,145,36,buttonNeutral,buttonActive,self.battle_start, "cave")
				button_image(gameDisplay,"Forrest (Level 1)",300,100,145,36,buttonNeutral,buttonActive,self.battle_start, "forrest")
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

	def intro_text(self):
		text = "You walk into a small town. It has basic amenities from an inn to an armory."
		print_text(gameDisplay,text,"arial",15,white,(100,80))
		text = "You see a man standing in the town square preaching of demonic visions he had."
		print_text(gameDisplay,text,"arial",15,white,(100,100))
		text = "Most of the villagers didn't seem to be paying attention but there was clear fear in his eyes."
		print_text(gameDisplay,text,"arial",15,white,(100,120))
		text = "You decide to listen to what he has to say."
		print_text(gameDisplay,text,"arial",15,white,(100,140))
		text = "Man: They are coming! Someone please listen! we msut fortify the town, we must tell all who will hear!"
		print_text(gameDisplay,text,"arial",15,white,(100,160))
		text = "Man: I fear I am too old to do anything of value for the town other than share my experiences..."
		print_text(gameDisplay,text,"arial",15,white,(100,180))
		text = "Man: So if anyone could help please visit me in my house at the edge of town, I have several ideas."
		print_text(gameDisplay,text,"arial",15,white,(100,200))
		text = "After his speech you see an ominous look in his eyes, when you see this he catches your eye"
		print_text(gameDisplay,text,"arial",15,white,(100,220))
		text = "You hold his gaze for a moment then he turns and walks off."
	
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

	def display_stats(self):
		global charInfo
		text = "Your Level: "+str(charInfo["lvl"])
		print_text(gameDisplay,text,"arial",20,white,(73,50))

		text = "HP: "+str(charInfo["hp"][0])+" / "+str(charInfo["hp"][1])
		print_text(gameDisplay,text,"arial",20,red,(75,75))

		text = "MP: "+str(charInfo["mp"][0])+" / "+str(charInfo["mp"][1])
		print_text(gameDisplay,text,"arial",20,blue,(73,100))

		text = "Intelligence "+str(charInfo["int"])
		print_text(gameDisplay,text,"arial",20,white,(73,125))

		text = "Strength: "+str(charInfo["str"])
		print_text(gameDisplay,text,"arial",20,white,(73,150))

		text = "Weapon: " + charInfo["weapon"][0]
		print_text(gameDisplay,text,"arial",20,white,(240,75))
		if(charInfo["armor"] == None):
			text = "Armor: " + charInfo["armor"]
		else:
			text = "Armor: " +charInfo["armor"][0]
		print_text(gameDisplay,text,"arial",20,white,(240,100))

		text = "Shield: " + charInfo["shield"]
		print_text(gameDisplay,text,"arial",20,white,(240,125))

		text = "Amulet: " + charInfo["amulet"]
		print_text(gameDisplay,text,"arial",20,white,(240,150))

		text = "Experience: " + str(charInfo["exp"])
		print_text(gameDisplay,text,"arial",20,white,(74,175))

		text = "To next: " + str(int((100*math.pow(charInfo["lvl"],1.6)) - charInfo["exp"]))
		print_text(gameDisplay,text,"arial",20,white,(74,200))

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

	def buy_item(self,item):
		start = item[:1]
		item = item[1:]
		if(start == "W"):
			charInfo["weapon"],charInfo["gold"] = buy_weapon(charInfo["weapon"],charInfo["gold"], item) 
		elif(start == "A"):
			charInfo["armor"],charInfo["gold"] = buy_armor(charInfo["armor"],charInfo["gold"], item) 

game_intro()
