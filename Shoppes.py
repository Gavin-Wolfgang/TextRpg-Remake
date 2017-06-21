
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