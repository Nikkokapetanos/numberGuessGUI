"""
Program: numberGuessGUI.py
Author: Nikko Kapetanos 7/13/2023

GUI-based version of the number guessing game

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
import random 

# Other imports go here

# Class header (application name will change project to project)
class GuessingGame(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		# Call to the Easy Frame construction method
		EasyFrame.__init__(self, title = "Guessing Game", width = 260, height = 180)

		# Initialize the instance variables for the class
		self.magicNumber = random.randint(1, 10)
		self.count = 0

		# Create and add widgets to the window 
		self.hintLabel = self.addLabel(text = "Guess a Number Between 1 and 10", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addLabel(text ="Your guess:", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)

	# Definition of the nextGuess() function
	def nextGuess(self):
		self.count += 1
		guess = self.guessField.getNumber()
		# Logic that determins the games outcome
		if guess == self.magicNumber:
			self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempts!"
			self.nextButton["state"] = "disabled"
		elif guess < self.magicNumber:
			self.hintLabel["text"] = "Sorry, your guess was too small!"
		else:
			self.hintLabel["text"] = "Sorry, your guess was too large!"
	# Definition of the newGame() function
	def newGame(self):
		"""Resets the data and GUI to their original states."""
		self.magicNumber = random.randint(1, 10)
		self.count = 0
		self.hintLabel["text"] = "Guess a Number Between 1 and 100"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"



# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	GuessingGame().mainloop()

# Global call to the main() for program entry
if __name__ == '__main__':
	main()