import random

"""Rock paper scissors player"""
class RPSPlayer:
	strategy = RPSOppositeStrategy()
	def play(self):
		decideStrategy()
		strategy.makeMove()
		
	def setStrategy(self,strat):
		self.strategy = strat
	
	def decideStrategy(self):
		"""Randomly sets a strategy"""
		strategies[] = [RPSOppositeStrategy,RPSLeastUsedStrategy,RPSMostUsedStrategy]
		setStrategy(random.choice(strategies)) 
		
		
"""
#Chose what beats the last played move by the opponent. 
#Weak in that it's an easy-to-spot pattern.
"""
class RPSOppositeStrategy:
	def makeMove(self):
		if opponentLastMove = "rock":
			return "paper"
		elif opponentLastMove = "paper":
			return "scissors"
		elif opponentLastMove = "scissors":
			return "rock"

"""
# Determine the least picked by the opponent and play the choice that would beat the least picked by opponent.
# The logic being that the opponent will not expect you to expect the least picked hand.
# Weak against players who repeatedly choose the same thing.			
"""
class RPSLeastUsedStrategy:
	def makeMove(self):
		if opponentLeastUsed = "rock":
			return "paper"
		elif opponentLeastUsed = "paper":
			return "scissors"
		elif opponentLeastUsed = "scissors":
			return "rock"
	
	def calculateLeastUsed(self):
		return leastUsed

"""
Determine most picked by the opponent and play the choice that would beat the most picked.
Strong against players who tend to play the same hand
"""
class RPSMostUsedStrategy:
	def makeMove(self):
		if opponentMostUsed = "rock":
			return "paper"
		elif opponentMostUsed = "paper":
			return "scissors"
		elif opponentMostUsed = "scissors":
			return "rock"
	
	def calculateMostUsed(self):
		return mostUsed