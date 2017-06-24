
def buy_weapon(weapon, gold, toBuy):
	if(toBuy == "Iron Dagger"):
		if(gold > 100):
			gold -= 100
			weapon = ["Iron Dagger", 1,6]
			return weapon, gold

	elif(toBuy == "Iron Sword"):
		if(gold > 200):
			gold -= 200
			weapon = ["Iron Sword", 2,8]
			return weapon, gold

	elif(toBuy == "Silver Sword"):
		if(gold > 400):
			gold -= 400
			weapon = ["Silver Sword", 3,10]
			return weapon, gold

	elif(toBuy == "Granite Hammer"):
		if(gold > 700):
			gold -= 700
			weapon = ["Granite Hammer", 1,17]
			return weapon, gold
	return weapon, gold

def buy_armor(armor, gold, toBuy):
	if(toBuy == "Ringmail Armor"):
		if(gold > 100):
			gold -= 100
			armor = ["Ringmail Armor", 2]
			return armor, gold

	elif(toBuy == "Iron Armor"):
		if(gold > 200):
			gold -= 200
			armor = ["Iron Armor", 3]
			return armor, gold

	elif(toBuy == "Chainmail Armor"):
		if(gold > 350):
			gold -= 350
			armor = ["Chainmail Armor", 5]
			return armor, gold

	elif(toBuy == "Steel Armor"):
		if(gold > 500):
			gold -= 500
			armor = ["Steel Armor", 7]
			return armor, gold
	return armor, gold

def buy_rune(rune, gold, toBuy):
		if(toBuy == "Health Rune"):
			if(gold > 500):
				gold -= 500
				rune = ["Health Rune","hp", 1.05]
				return rune, gold

		elif(toBuy == "Strength Rune"):
			if(gold > 500):
				gold -= 500
				rune = ["Strenth Rune","str", 1.1]
				return rune, gold

		elif(toBuy == "Intelligence Rune"):
			if(gold > 500):
				gold -= 500
				rune = ["Strenth Rune","int", 1.1]
				return rune, gold

		elif(toBuy == "Defense Rune"):
			if(gold > 500):
				gold -= 500
				rune = ["Defense Rune","def", 1.25]
				return rune, gold

		elif(toBuy == "Mana Rune"):
			if(gold > 500):
				gold -= 500
				rune = ["Mana Rune","mp", 1.1]
				return rune, gold
		return rune, gold

def buy_health_potion(health_potion, gold, toBuy):
	if(toBuy == "Weak Health Potion"):
		if(gold > 100):
			gold -= 100
			health_potion[0] += 1
			return health_potion, gold

	elif(toBuy == "Health Potion"):
		if(gold > 300):
			gold -= 300
			health_potion[1] += 1
			return health_potion, gold

	elif(toBuy == "Strong Health Potion"):
		if(gold > 500):
			gold -= 500
			health_potion[2] += 1
			return health_potion, gold

	elif(toBuy == "Max Health Potion"):
		if(gold > 1000):
			gold -= 1000
			health_potion[3] += 1
			return health_potion, gold

	return health_potion,gold

