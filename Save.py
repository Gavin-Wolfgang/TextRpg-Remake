import pickle, os

def findPath():
	fPath = os.path.join(os.path.abspath(''))
	splits = fPath.split("\\")
	newPath = splits[0] + "\\" + splits[1] + "\\"+splits[2] + "\\" + 'Desktop\\Game\\TextRpg Remake\\Character'
	return newPath

def char_import(name):
	file = open(findPath()+"\\"+str(name),"rb")
	charInfo = pickle.load(file)
	file.close()
	return charInfo

def save(slot, charInfo):
	file = open(findPath()+"\\"+str(slot), "wb")
	pickle.dump(charInfo,file,-1)
	file.close()

def char_list():
	final_names = []
	file = findPath()
	for x in os.listdir(file):
		if x.endswith(".txt"):
			pass
		else:
			final_names.append(x)
	return final_names

def char_exists(name):
	names = char_list()

	for x in names:
		if(x == str(name)):
			return True

	return False