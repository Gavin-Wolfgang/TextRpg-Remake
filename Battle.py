import random, pygame, time, math
from Visuals import*
from Text import*

black =			(  0,  0,  0)
white = 		(255,255,255)
red = 			(120,  0,  0)
blue = 			(  0,  0,150)
bright_blue = 	(  0,  0,250)
green =			(  0,200,  0)
bright_red = 	(200,  0,  0)
bright_green = 	(  0,255,  0)
yellow =        (255, 255, 0)
something = 	(100,100,100)

class battle():
	def __init__(self,charInfo,location, gameDisplay):
		buttonNeutral = pygame.image.load('GRAPHICS\\button_neutral.bmp')
		buttonActive = pygame.image.load('GRAPHICS\\button_hover.bmp')
		clock = pygame.time.Clock()
		self.turn = True
		self.charInfo = charInfo
		self.text = ["",""]
		self.end = False
		self.give_gold_loc = 0
		self.gold = 0
		self.location = 0
		loop = True
		if(location == "cave"):
			self.enemy = self.cave_battle()
		elif(location == "forrest"):
			self.enemy = self.forrest_battle()
		elif(location == "river"):
			self.enemy = self.river_battle()
		elif(location == "harlech_house"):
			self.enemy = self.harlech_house_battle()

		battleText = battle_text(gameDisplay,charInfo,self.enemy, self.text )

		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			battleText.char_text()
			battleText.enemy_text()
			battleText.attacks()

			self.enemy_turn()
			if(self.charInfo["hp"][0] <= 0 or self.enemy["hp"][0] <= 0):
				button_image(gameDisplay,"End Battle",400-73,475,145,36,buttonNeutral,buttonActive,self.end_it)
				if(self.enemy["hp"][0] <= 0 and self.charInfo["hp"][0] > 0):
					gold = self.give_gold
					battleText.end_game(self.gold)
				if(self.end):
					break

			elif(self.location == 1):
				button_image(gameDisplay,"Weak Potion",150,450,145,36,buttonNeutral,buttonActive,self.heal, "weak")
				button_image(gameDisplay,"Normal Potion",350,450,145,36,buttonNeutral,buttonActive,self.heal,"normal")
				button_image(gameDisplay,"Strong Potion",550,450,145,36,buttonNeutral,buttonActive,self.heal, "strong")
				button_image(gameDisplay,"Max Potion",150,500,145,36,buttonNeutral,buttonActive,self.heal,"max")
				button_image(gameDisplay,"Attacks",550,500,145,36,buttonNeutral,buttonActive,self.change_loc,0)

			else:
				button_image(gameDisplay,"Weak Attack",100,475,145,36,buttonNeutral,buttonActive,self.weak_attack)
				button_image(gameDisplay,"Strong Attack",500,475,145,36,buttonNeutral,buttonActive,self.strong_attack)
				button_image(gameDisplay,"Health Potion",300,475,145,36,buttonNeutral,buttonActive,self.change_loc,1)


			battleText.update(charInfo,self.enemy, self.text)
			pygame.display.update()
			clock.tick(15)

		self.give_exp()
		self.level_up(gameDisplay)

	#--------------------------------------------------------------------------
	def change_loc(self, loc):
		self.location = loc

	def forrest_battle(self):
		randNum = random.randint(1,5)
		if(randNum == 1):
			enemy = {"name": "Spider", "hp": [9,9], "str":2, "exp": 100, "lvl":1, "gold": [0,9]}
		elif(randNum == 2):
			enemy = {"name": "Bunny", "hp": [5,5], "str":1, "exp": 100, "lvl":1, "gold": [0,6]}
		elif(randNum == 3):
			enemy = {"name": "Bear", "hp": [17,17], "str":2, "exp": 100, "lvl":1, "gold": [6,17]}
		elif(randNum == 4):
			enemy = {"name": "Wolf", "hp": [12,12], "str":4, "exp": 100, "lvl":1, "gold": [3,20]}
		elif(randNum == 5):
			enemy = {"name": "Boar", "hp": [23,23], "str":1, "exp": 100, "lvl":1, "gold": [10,16]}
		elif(randNum == 6):
			enemy = {"name": "Big Bat", "hp": [35,35], "str":1, "exp": 100, "lvl":1, "gold": [10,16]}
		return enemy 

	#--------------------------------------------------------------------------

	def cave_battle(self):
		randNum = random.randint(1,5)
		if(randNum == 1):
			enemy = {"name": "Cave Spider", "hp": [27,27], "str":1, "exp": 100, "lvl":4, "gold": [0,17]}
		elif(randNum == 2):
			enemy = {"name": "Troll", "hp": [40,40], "str":2, "exp": 100, "lvl":4, "gold": [4,27]}
		elif(randNum == 3):
			enemy = {"name": "Witch", "hp": [22,22], "str":4, "exp": 100, "lvl":4, "gold": [22,32]}
		elif(randNum == 4):
			enemy = {"name": "Scorpian", "hp": [16,16], "str":6, "exp": 100, "lvl":4, "gold": [12,32]}
		elif(randNum == 5):
			enemy = {"name": "Bat", "hp": [18,18], "str":3, "exp": 100, "lvl":4, "gold": [6, 21]}
		return enemy 

	#--------------------------------------------------------------------------

	def river_battle(self):
		randNum = random.randint(1,5)
		if(randNum == 1):
			enemy = {"name": "Giant Squid", "hp": [60,60], "str":6, "exp": 100, "lvl":8, "gold": [15,35]}
		elif(randNum == 2):
			enemy = {"name": "Squid", "hp": [40,40], "str":4, "exp": 100, "lvl":8, "gold": [12,28]}
		elif(randNum == 3):
			enemy = {"name": "Water Nymph", "hp": [66,66], "str":6, "exp": 100, "lvl":8, "gold": [26,48]}
		elif(randNum == 4):
			enemy = {"name": "Crab", "hp": [48,48], "str":5, "exp": 100, "lvl":8, "gold": [22,32]}
		elif(randNum == 5):
			enemy = {"name": "Giant Crab", "hp": [64,64], "str":6, "exp": 100, "lvl":8, "gold": [25, 50]}
		return enemy 

	#--------------------------------------------------------------------------

	def harlech_house_battle(self):
		#pygame.draw.rect(gameDisplay,yellow,(73,300,150,15))
		randNum = random.randint(1,2)
		if(randNum == 1):
			enemy = {"name": "Lesser Demon", "hp": [75,75], "str":8, "exp": 200, "lvl":12, "gold": [50,100]}
			#text = "Screaming can be heard from deeper within the house, this is not the end..."
			#print_text(gameDisplay,text,"arial",15,white,(73,300))
		elif(randNum == 2):
			enemy = {"name": "Harlech Demon", "hp": [90,90], "str":10, "exp": 300, "lvl":12, "gold": [75,250]}
			#text = "Your spine shivers, this must be the demon of the Harlech House!"
			#print_text(gameDisplay,text,"arial",15,white,(73,300))

		return enemy 

	#--------------------------------------------------------------------------

	def weak_attack(self):
		if(self.turn == True):
			minimum = self.charInfo["weapon"][1]+self.charInfo["str"]
			maximum = self.charInfo["weapon"][2]+self.charInfo["str"]
			damage = random.randint(minimum,maximum)
			self.enemy["hp"][0] -= damage
			self.text[0] = "You dealt "+str(damage)+" with a weak attack."
			self.turn = False
		else:
			pass

	#--------------------------------------------------------------------------

	def strong_attack(self):
		if(self.turn == True and self.charInfo["mp"][0] > 0):
			minimum = self.charInfo["weapon"][1]+self.charInfo["str"]+2
			maximum = self.charInfo["weapon"][2]+self.charInfo["str"]+2
			damage = random.randint(minimum,maximum)
			self.enemy["hp"][0] -= damage
			self.charInfo["mp"][0] -=1
			self.text[0] = "You dealt "+str(damage)+" with a strong attack."
			self.turn = False
		else:
			pass

	#--------------------------------------------------------------------------

	def heal(self, potion):
		print("using potion")
		if(self.turn == True and self.charInfo["potions"][0] >= 1 and potion == "weak"):
			maximum = math.ceil(self.charInfo["hp"][1]*.4)
			minimum = math.floor(self.charInfo["hp"][1]*.2)
			regeneration = random.randint(minimum,maximum)
			self.charInfo["hp"][0] += regeneration
			if self.charInfo["hp"][0] > self.charInfo["hp"][1]:
				self.charInfo["hp"][0] = self.charInfo["hp"][1]
			self.charInfo["potions"][0] -=1
			self.text[0] = "You healed "+str(regeneration)+" with a weak health potion."
			self.turn = False
		elif(self.turn == True and self.charInfo["potions"][1] >= 1 and potion == "normal"):
			maximum = math.ceil(self.charInfo["hp"][1]*.6)
			minimum = math.floor(self.charInfo["hp"][1]*.4)
			regeneration = random.randint(minimum,maximum)
			self.charInfo["hp"][0] += regeneration
			if self.charInfo["hp"][0] > self.charInfo["hp"][1]:
				self.charInfo["hp"][0] = self.charInfo["hp"][1]
			self.charInfo["potions"][1] -=1
			self.text[0] = "You healed "+str(regeneration)+" with a weak health potion."
			self.turn = False
		elif(self.turn == True and self.charInfo["potions"][2] >= 1 and potion == "strong"):
			maximum = math.ceil(self.charInfo["hp"][1]*.8)
			minimum = math.floor(self.charInfo["hp"][1]*.6)
			regeneration = random.randint(minimum,maximum)
			self.charInfo["hp"][0] += regeneration
			if self.charInfo["hp"][0] > self.charInfo["hp"][1]:
				self.charInfo["hp"][0] = self.charInfo["hp"][1]
			self.charInfo["potions"][2] -=1
			self.text[0] = "You healed "+str(regeneration)+" with a weak health potion."
			self.turn = False
		elif(self.turn == True and self.charInfo["potions"][3] >= 1 and potion == "max"):
			regeneration = self.charInfo["hp"][1] - self.charInfo["hp"][0]
			self.charInfo["hp"][0] = self.charInfo["hp"][1]
			self.charInfo["potions"][2] -= 1
			self.text[0] = "You healed "+str(regeneration)+" with a weak health potion."
			self.turn = False
		else:
			pass

		#--------------------------------------------------------------------------

	def enemy_turn(self):
		if(self.turn == False):
			minimum = 2 - self.charInfo["def"]
			maximum = 2+self.enemy["str"]-self.charInfo["def"]
			damage = random.randint(minimum,maximum) * self.charInfo["difficulty"]
			self.charInfo["hp"][0] -= damage
			self.text[1] = "The enemy dealt "+str(damage)+" damage"
			self.turn = True

	#--------------------------------------------------------------------------

	def get_charInfo(self):
		return self.charInfo

	def end_it(self):
		self.end = True

	#--------------------------------------------------------------------------

	def give_exp(self):
		exp = (self.enemy["exp"] * (math.pow(self.charInfo["lvl"]/self.enemy["lvl"],-1)))
		exp = math.ceil(exp)
		self.charInfo["exp"] += exp
		print(self.charInfo["exp"])

	def give_gold(self):
		if(self.give_gold_loc == 0):
			self.gold = random.randint(self.enemy["gold"][0], self.enemy["gold"][1])
			self.charInfo["gold"] += gold
			print(self.charInfo["gold"])
		self.give_gold_loc = 1

	#--------------------------------------------------------------------------

	def level_up(self, gameDisplay):
		print("leveling up")
		print("exp: ",self.charInfo["exp"])
		print("lvl: ",self.charInfo["lvl"])
		if(self.charInfo["hp"][0] > 0):
			while(True):
				expNeeded = 100 * math.pow(self.charInfo["lvl"],1.6)
				expNeeded = math.ceil(expNeeded)
				print("Need exp: ",expNeeded)
				if(self.charInfo["exp"] >= expNeeded):
					self.charInfo["lvl"] += 1
					self.charInfo["exp"] -= expNeeded
					up = level_ups(self.charInfo, gameDisplay)
					self.charInfo = up.get_charInfo()
				else:
					break
		print("lvl: ",self.charInfo["lvl"])

	#--------------------------------------------------------------------------

class level_ups():
	def __init__(self,charInfo,gameDisplay):
		loop = True
		buttonNeutral = pygame.image.load('GRAPHICS\\button_neutral.bmp')
		buttonActive = pygame.image.load('GRAPHICS\\button_hover.bmp')
		clock = pygame.time.Clock()
		self.charInfo = charInfo
		self.loop = True
		while self.loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			print_text(gameDisplay,"+5 hp","arial",20,white,(150,300))
			print_text(gameDisplay,"+2 hp if warrior","arial",20,white,(150,340))
			print_text(gameDisplay,"+1 strength","arial",20,white,(150,380))

			print_text(gameDisplay,"+3 mp","arial",20,white,(400,300))
			print_text(gameDisplay,"+1 mp if warrior","arial",20,white,(400,340))
			print_text(gameDisplay,"+1 Intelligence","arial",20,white,(400,380))

			print_text(gameDisplay,"You get +1 mp and hp no matter which you choose!","arial",20,white,(200,250))

			button_image(gameDisplay,"Strength",150,475,145,36,buttonNeutral,buttonActive,self.str_up)
			button_image(gameDisplay,"Intelligence",450,475,145,36,buttonNeutral,buttonActive,self.int_up)

			pygame.display.update()
			clock.tick(15)

	#--------------------------------------------------------------------------

	def str_up(self):
		if(self.charInfo["class"] == "warrior"):
			self.charInfo["hp"][1] += 8
		else:
			self.charInfo["hp"][1] += 6

		self.charInfo["mp"][1] += 1
		self.charInfo["str"] += 1
		self.loop = False

	#--------------------------------------------------------------------------
	
	def int_up(self):
		if(self.charInfo["class"] == "mage"):
			self.charInfo["mp"][1] += 5
		else:
			self.charInfo["mp"][1] += 4
		self.charInfo["hp"][1] += 1
		self.charInfo["mp"][1] += 1
		self.loop = False

	#--------------------------------------------------------------------------

	def get_charInfo(self):
		return self.charInfo