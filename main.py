


text_filename = "blackadder.txt"
json_filename = "blackadder.json"

class BlackAdderQuote(object):
	def __init__(self, line):
		parts = line.strip().split(":")
		self.key = parts[0].strip()
		self.quote = parts[1].strip()

	def Key(self):
		return self.key

	def Quote(self):
		return self.quote

	def __str__(self):
		return self.Key()

def main():
	with open(text_filename) as f:
		content = f.read()

	quoteObjects = []
	for line in content.split("\n"):
		line_text = line.strip()
		if len(line_text) and line_text[0] != "#":
			quoteObject = BlackAdderQuote(line_text)
			quoteObjects.append(quoteObject)
			pass
		pass

	for quoteObject in quoteObjects:
		#print(quoteObject)
		pass

	jsonObject = {}
	jsonObject["quotes"] = {}
	for quoteObject in quoteObjects:
		jsonObject["quotes"][quoteObject.Key()] = quoteObject.Quote()
		pass

	with open(json_filename, "w") as f:
		f.write(str(jsonObject))
		pass
	pass

if __name__ == '__main__':
	main()
