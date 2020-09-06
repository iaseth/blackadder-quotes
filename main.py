


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
	with open("blackadder.txt") as f:
		content = f.read()

	quoteObjects = []
	for line in content.split("\n"):
		line_text = line.strip()
		if len(line_text):
			quoteObject = BlackAdderQuote(line_text)
			quoteObjects.append(quoteObject)
			pass
		pass

	for quoteObject in quoteObjects:
		print(quoteObject)
		pass
	pass

if __name__ == '__main__':
	main()
