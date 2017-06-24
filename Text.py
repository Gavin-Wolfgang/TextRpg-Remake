import pygame, math 
from Visuals import*

global gameDisplay, charInfo, enemy

black =			(  0,  0,  0)
white = 		(255,255,255)
red = 			(200,  0,  0)
blue = 			(  0,  0,200)
green =			(  0,200,  0)
bright_red = 	(255,  0,  0)
bright_green = 	(  0,255,  0)
yellow =        (255, 255, 0)
something = 	(100,100,100)
bright_blue = 	(  0,  0,250)


class main_text():
	def __init__(self,Display, Info):
		global gameDisplay, charInfo
		gameDisplay = Display
		charInfo = Info

	def intro_text(self):
		text = "You walk into a small town. It has basic amenities from an inn to an armory."
		print_text(gameDisplay,text,"arial",15,white,(100,80))
		text = "You see a man standing in the town square preaching of demonic visions he had."
		print_text(gameDisplay,text,"arial",15,white,(100,100))
		text = "Most of the villagers didn't seem to be paying attention but there was clear fear in his eyes."
		print_text(gameDisplay,text,"arial",15,white,(100,120))
		text = "You decide to listen to what he has to say."
		print_text(gameDisplay,text,"arial",15,white,(100,140))
		text = "Man: They are coming! Someone please listen! we must fortify the town, we must tell all who will hear!"
		print_text(gameDisplay,text,"arial",15,white,(100,160))
		text = "Man: I fear I am too old to do anything of value for the town other than share my experiences..."
		print_text(gameDisplay,text,"arial",15,white,(100,180))
		text = "Man: So if anyone could help please visit me in my house at the edge of town, I have several ideas."
		print_text(gameDisplay,text,"arial",15,white,(100,200))
		text = "After his speech you see an ominous look in his eyes, when you see this he catches your eye"
		print_text(gameDisplay,text,"arial",15,white,(100,220))
		text = "You hold his gaze for a moment then he turns and walks off."
		print_text(gameDisplay,text,"arial",15,white,(100,240))

	def stats(self):
		#first column
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

		text = "Experience: " + str(charInfo["exp"])
		print_text(gameDisplay,text,"arial",20,white,(74,175))

		text = "To next: " + str(int((100*math.pow(charInfo["lvl"],1.6)) - charInfo["exp"]))
		print_text(gameDisplay,text,"arial",20,white,(74,200))

		#second column
		text = "Gold: "+str(charInfo["gold"])
		print_text(gameDisplay,text,"arial",20,white,(240,50))

		text = "Weapon: " + charInfo["weapon"][0]
		print_text(gameDisplay,text,"arial",20,white,(240,75))

		if(charInfo["armor"] == None):
			text = "Armor: " + charInfo["armor"]
		else:
			text = "Armor: " +charInfo["armor"][0]
		print_text(gameDisplay,text,"arial",20,white,(240,100))

		if(charInfo["rune"] == None):
			text = "Rune: " + charInfo["rune"]
		else:
			text = "Rune: " +charInfo["rune"][0]
		print_text(gameDisplay,text,"arial",20,white,(240,175))

		text = "Shield: " + charInfo["shield"]
		print_text(gameDisplay,text,"arial",20,white,(240,125))

		text = "Amulet: " + charInfo["amulet"]
		print_text(gameDisplay,text,"arial",20,white,(240,150))

		print_text(gameDisplay,"Potions","arial",20,white,(450,50))		

		text = "Weak Potion: " + str(charInfo["potions"][0])
		print_text(gameDisplay,text,"arial",20,white,(450,75))

		text = "Potion: " + str(charInfo["potions"][1])
		print_text(gameDisplay,text,"arial",20,white,(450,100))

		text = "Strong Potion: " + str(charInfo["potions"][2])
		print_text(gameDisplay,text,"arial",20,white,(450,125))

		text = "Max Potion: " + str(charInfo["potions"][3])
		print_text(gameDisplay,text,"arial",20,white,(450,150))

	def potions(self):
		text = "Weak Potion: " + str(charInfo["potions"][0])
		print_text(gameDisplay,text,"arial",20,white,(450,75))

		text = "Potion: " + str(charInfo["potions"][1])
		print_text(gameDisplay,text,"arial",20,white,(450,100))

		text = "Strong Potion: " + str(charInfo["potions"][2])
		print_text(gameDisplay,text,"arial",20,white,(450,125))

		text = "Max Potion: " + str(charInfo["potions"][3])
		print_text(gameDisplay,text,"arial",20,white,(450,150))


		
class battle_text():
	def __init__(self,Display,Info,enemyInfo, text):
		self.gameDisplay = Display
		self.charInfo = Info
		self.enemy = enemyInfo
		self.text = text

	def update(self, info, enemyInfo, text):
		self.charInfo = info
		self.enemy = enemyInfo
		self.text = text

	def char_text(self):
		pygame.draw.rect(self.gameDisplay,red,(70,74,150,35))
		size = int(142*(self.charInfo["hp"][0]/self.charInfo["hp"][1]))
		if(size < 0):
			size = 0
		if self.charInfo["hp"][0]/self.charInfo["hp"][1] > 0.80:
			pygame.draw.rect(self.gameDisplay,bright_green,(73,78,size,27))
		elif self.charInfo["hp"][0]/self.charInfo["hp"][1] > 0.30:
			pygame.draw.rect(self.gameDisplay,yellow,(73,78,size,27))
		else:
			pygame.draw.rect(self.gameDisplay,bright_red,(73,78,size,27))

		pygame.draw.rect(self.gameDisplay,blue,(70,114,150,35))
		size = int(142*(self.charInfo["mp"][0]/self.charInfo["mp"][1]))
		pygame.draw.rect(self.gameDisplay,bright_blue,(73,118,size,27))

		text = "HP: "+str(self.charInfo["hp"][0])+" / "+str(self.charInfo["hp"][1])
		print_text(self.gameDisplay,text,"arial",25,black,(75,75))

		text = "MP: "+str(self.charInfo["mp"][0])+" / "+str(self.charInfo["mp"][1])
		print_text(self.gameDisplay,text,"arial",25,black,(73,115))

	def enemy_text(self):
		pygame.draw.rect(self.gameDisplay,red,(545,114,150,35))
		size = int(142*(self.enemy["hp"][0]/self.enemy["hp"][1]))
		if(size < 0):
			size = 0
		pygame.draw.rect(self.gameDisplay,bright_red,(548,118,size,27))

		print_text(self.gameDisplay,self.enemy["name"],"arial",25,bright_red,(550,75))
		text = "HP: "+str(self.enemy["hp"][0])+" / "+str(self.enemy["hp"][1])
		print_text(self.gameDisplay,text,"arial",25,black,(550,115))

	def attacks(self):
		print_text(self.gameDisplay,self.text[0],"arial",20,red,(75,400))
		print_text(self.gameDisplay,self.text[1],"arial",20,red,(450,400))

	def end_game(self, gold):
		text = "You got "+str(self.enemy["exp"])+" experience."
		print_text(self.gameDisplay,text,"arial",20,white,(75,250))
		text = "You got "+str(gold)+" gold."
		print_text(self.gameDisplay,text,"arial",20,white,(450,250))