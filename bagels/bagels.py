from random import randrange
class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

class Game:

	def __init__(self, max_guess):
		self.round = 1
		self.max_guess = max_guess
		self.number_to_guess = self.generate_number()
		self.welcome_message = """
		
		Bagels, a deductive logic game.
		By Al Sweigart al@inventwithpython.com
		
		I am thinking of a 3-digit number. Try to guess what it is.
		
		Here are some clues:
		When I say:    That means:
		Pico         One digit is correct but in the wrong position.
		Fermi        One digit is correct and in the right position.
		Bagels       No digit is correct.
		"""
		self.start_message = """\t\tI have thought up a number.\n\t\tYou have """+ str(max_guess) + """ guesses to get it.\n"""
		print(colors.RED + self.welcome_message + colors.ENDC)

	def run(self):
		print(colors.GREEN + self.start_message + colors.ENDC)
		self.round = 1
		while (True):
			guess = input("Guess #"+str(self.round)+":\n")
			answer = ""
			if (len(guess) == 3):
				for i in range(3):
					if (guess[i] == self.number_to_guess[i]):
						answer += "Fermi "
					elif (guess[i] in self.number_to_guess):
						answer += "Pico "
					else:
						answer += "- "
				if (answer == "- - - "):
					answer = "Bagels"

				if (self.number_to_guess == guess):
					self.win()
					break
				else:
					print(answer)
				self.round += 1
			else:
				print("You must provide a number of lengths 3")
			if (self.round > self.max_guess):
				self.lost()
				break
		self.retry()

	def retry(self):
		retry = ""
		while (retry != "yes" and retry != "no"):
			retry = input("Do you want to retry ? (yes or no)")
		if (retry == "no"):
			print("Bye bye")
		elif (retry == "yes"):
			self.run()

	def generate_number(self):
		random_number = str(randrange(10)) + str(randrange(10)) + str(randrange(10))
		return random_number

	def lost(self):
		# print(colors.RED + "You lost!" + colors.ENDC)
		print(colors.RED + "Aya t'est nul!" + colors.ENDC)
	
	def win(self):
		print(colors.GREEN + "BINGO !!!" + colors.ENDC)


game = Game(10)
game.run()