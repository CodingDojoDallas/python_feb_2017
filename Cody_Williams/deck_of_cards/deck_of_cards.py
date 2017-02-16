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
				suit = 'Clubs'
			elif i == 2:
				suit = 'Spades'
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

	def deal(self, players):
		for i in range(2):
			for player in players:
				output = self.deck[0]
				del self.deck[0]
				player.hand.append(output)
		return self

class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

a = Deck()
bob = Player('Bob')
cody = Player('Cody')
steve = Player('Steve')

a.deal([bob, cody, steve])

a.shuffle()
dealt_card = a.deal(bob)
print "dealing {} of {} to {}".format(dealt_card.value, dealt_card.suit, bob.name)
dealt_card = a.deal(bob)
print "dealing {} of {} to {}".format(dealt_card.value, dealt_card.suit, bob.name)
dealt_card = a.deal(bob)
print "dealing {} of {} to {}".format(dealt_card.value, dealt_card.suit, bob.name)
dealt_card = a.deal(bob)
print "dealing {} of {} to {}".format(dealt_card.value, dealt_card.suit, bob.name)


print "Bob is holding..."
for card in bob.hand:
	print "{} of {}".format(card.value, card.suit)




