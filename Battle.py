import random, pygame, time, math
from Visuals import*

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
		loop = True
		if(location == "cave"):
			self.enemy = self.cave_battle()
		elif(location == "forrest"):
			self.enemy = self.forrest_battle()
		elif(location == "river"):
			self.enemy = self.river_battle()
		elif(location == "harlech_house"):
			self.enemy = self.harlech_house_battle()

		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			gameDisplay.fill(black)

			self.char_text(gameDisplay)
			self.enemy_text(gameDisplay)

			print_text(gameDisplay,self.text[0],"arial",20,red,(75,400))
			print_text(gameDisplay,self.text[1],"arial",20,red,(450,400))

			self.enemy_turn()
			if(self.charInfo["hp"][0] <= 0 or self.enemy["hp"][0] <= 0):
				button_image(gameDisplay,"End Battle",400-73,475,145,36,buttonNeutral,buttonActive,self.end_it)
				if(self.end):
					break

			else:
				button_image(gameDisplay,"Weak Attack",150,475,145,36,buttonNeutral,buttonActive,self.weak_attack)
				button_image(gameDisplay,"Strong Attack",450,475,145,36,buttonNeutral,buttonActive,self.strong_attack)


			pygame.display.update()
			clock.tick(60)
		self.give_exp()
		self.give_gold()
		self.level_up(gameDisplay)

	#--------------------------------------------------------------------------

	def char_text(self,gameDisplay):
		pygame.draw.rect(gameDisplay,red,(70,74,150,35))
		size = int(142*(self.charInfo["hp"][0]/self.charInfo["hp"][1]))
		if(size < 0):
			size = 0
		if self.charInfo["hp"][0]/self.charInfo["hp"][1] > 0.80:
			pygame.draw.rect(gameDisplay,bright_green,(73,78,size,27))
		elif self.charInfo["hp"][0]/self.charInfo["hp"][1] > 0.30:
			pygame.draw.rect(gameDisplay,yellow,(73,78,size,27))
		else:
			pygame.draw.rect(gameDisplay,bright_red,(73,78,size,27))

		pygame.draw.rect(gameDisplay,blue,(70,114,150,35))
		size = int(142*(self.charInfo["mp"][0]/self.charInfo["mp"][1]))
		pygame.draw.rect(gameDisplay,bright_blue,(73,118,size,27))

		text = "HP: "+str(self.charInfo["hp"][0])+" / "+str(self.charInfo["hp"][1])
		print_text(gameDisplay,text,"arial",25,black,(75,75))

		text = "MP: "+str(self.charInfo["mp"][0])+" / "+str(self.charInfo["mp"][1])
		print_text(gameDisplay,text,"arial",25,black,(73,115))

	#--------------------------------------------------------------------------

	def enemy_text(self,gameDisplay):
		pygame.draw.rect(gameDisplay,red,(545,114,150,35))
		size = int(142*(self.enemy["hp"][0]/self.enemy["hp"][1]))
		if(size < 0):
			size = 0
		pygame.draw.rect(gameDisplay,bright_red,(548,118,size,27))

		print_text(gameDisplay,self.enemy["name"],"arial",25,bright_red,(550,75))
		text = "HP: "+str(self.enemy["hp"][0])+" / "+str(self.enemy["hp"][1])
		print_text(gameDisplay,text,"arial",25,black,(550,115))

	#--------------------------------------------------------------------------


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
		randNum = random.randint(1,5)
		if(randNum == 1):
			enemy = {"name": "Giant Squid", "hp": [60,60], "str":6, "exp": 100, "lvl":12, "gold": [15,35]}
		elif(randNum == 2):
			enemy = {"name": "Squid", "hp": [40,40], "str":4, "exp": 100, "lvl":12, "gold": [12,28]}
		elif(randNum == 3):
			enemy = {"name": "Water Nymph", "hp": [66,66], "str":6, "exp": 100, "lvl":12, "gold": [26,48]}
		elif(randNum == 4):
			enemy = {"name": "Crab", "hp": [48,48], "str":5, "exp": 100, "lvl":12, "gold": [22,32]}
		elif(randNum == 5):
			enemy = {"name": "Giant Crab", "hp": [64,64], "str":6, "exp": 100, "lvl":12, "gold": [25, 50]}
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

	def enemy_turn(self):
		if(self.turn == False):
			minimum = 2
			maximum = 2+self.enemy["str"]
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
		gold = random.randint(self.enemy["gold"][0], self.enemy["gold"][1])
		self.charInfo["gold"] += gold
		print(self.charInfo["gold"])

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