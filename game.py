import sys
sys.dont_write_bytecode = True

class Game:

	def retry(self):
		retry = ""
		while (retry != "yes" and retry != "no"):
			retry = input("Do you want to retry ? (yes or no)")
		if (retry == "no"):
			print("Bye bye")
		elif (retry == "yes"):
			self.run()

class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'