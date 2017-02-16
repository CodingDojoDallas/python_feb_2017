import random

class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class Deck(object):
	def __init__(self):
		self.deck = []
		for i in range(4):
			if i == 0:
				suit = 'Diamonds'
			elif i == 1:
				suit = 'Spades'
			elif i == 2:
				suit = 'Clubs'
			else:
				suit = 'Hearts'
			for value in range(2, 15):
				if value == 14:
					value = 'Ace'
				elif value == 13:
					value = 'King'
				elif value == 12:
					value = 'Queen'
				elif value == 11:
					value = 'Jack'
				self.deck.append(Card(suit, value))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self, num, players):
		for i in range(num):
			for player in players:
				print "dealiing {} of {} to {}".format(self.deck[0].value, self.deck[0].suit, player.name)
				player.hand.append(self.deck[0])
				del self.deck[0]

class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

a = Deck()
bob = Player('Bob')
kevin = Player('Kevin')
sarah = Player('Sarah')

a.deal(2, [bob, kevin, sarah])

for card in bob.hand:
	print "{} of {}".format(card.suit, card.value)

for card in kevin.hand:
	print "{} of {}".format(card.suit, card.value)

for card in sarah.hand:
	print "{} of {}".format(card.suit, card.value)




