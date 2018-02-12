handType = {'high_card'       : 1,
            'one_pair'        : 2,
            'two_pairs'       : 3,
            'three_of_a_kind' : 4,
            'straight'        : 5,
            'flush'           : 6,
            'full_house'      : 7,
            'four_of_a_kind'  : 8,
            'straight_flush'  : 9,
            'royal_flush'     : 10}

cardType = {'1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'T' : 10,
            'J' : 11,
            'Q' : 12,
            'K' : 13,
            'A' : 14}

from collections import Counter

class hand():
    def __init__(self, cards):
        self.cards = cards
        self.determineScore()

    def determineScore(self):
        self.score = 0
        numElements = Counter(elem[0] for elem in self.cards).most_common(2)
        prevCard = self.cards[0][0]
        suit = self.cards[0][1]
        straight = True
        flush = True
        for card in self.cards[1:]:
            if cardType[card[0]] != cardType[prevCard[0]] + 1:
                straight = False
            if card[1] != suit:
                flush = False
            prevCard = card
        if flush and straight and self.cards[4][0] == 'A':
            self.score = handType['royal_flush']
        elif flush and straight:
            self.score = handType['straight_flush']
        elif flush:
            self.score = handType['flush']
        elif straight:
            self.score = handType['straight']
        elif numElements[0][1] == 4:
            self.score = handType['four_of_a_kind']
        elif numElements[0][1] == 3:
            if numElements[1][1] == 2:
                self.score = handType['full_house']
            else:
                self.score = handType['three_of_a_kind']
        elif numElements[0][1] == 2:
            if numElements[1][1] == 2:
                self.score = handType['two_pairs']
            else:
                self.score = handType['one_pair']
        else:
            self.score = handType['high_card']

    def hasHighCard(self, type, toCompare):
        for c in reversed(xrange(5)):
            if cardType[self.cards[c][0]] > cardType[toCompare.cards[c][0]]:
                return True
            elif cardType[self.cards[c][0]] < cardType[toCompare.cards[c][0]]:
                return False

    def compareTo(self, type, toCompare):
        numElements1 = Counter(elem[0] for elem in self.cards)
        numElements2 = Counter(elem[0] for elem in toCompare.cards)
        if type == handType['high_card'] or type == handType['straight'] or type == handType['flush'] or type == handType['straight_flush']:
            return self.hasHighCard(type, toCompare)
        elif type == handType['one_pair'] or type == handType['three_of_a_kind'] or type == handType['four_of_a_kind']:
            if cardType[numElements1.most_common(1)[0][0]] > cardType[numElements2.most_common(1)[0][0]]:
                return True
            elif cardType[numElements1.most_common(1)[0][0]] == cardType[numElements2.most_common(1)[0][0]]:
                return self.hasHighCard(type, toCompare)
            return False
        elif type == handType['two_pairs']:
            if cardType[numElements1.most_common(2)[0][0]] > cardType[numElements2.most_common(2)[0][0]]:
                return True
            elif cardType[numElements1.most_common(2)[0][0]] == cardType[numElements2.most_common(2)[0][0]]:
                if cardType[numElements1.most_common(2)[1][0]] > cardType[numElements2.most_common(2)[1][0]]:
                    return True
                elif cardType[numElements1.most_common(2)[1][0]] == cardType[numElements2.most_common(2)[1][0]]:
                    return self.hasHighCard(type, toCompare)
            return False
        elif type == handType['full_house']:
            if cardType[numElements1.most_common(2)[0][0]] > cardType[numElements2.most_common(2)[0][0]] or cardType[numElements1.most_common(2)[0][0]] > cardType[numElements2.most_common(2)[1][0]]:
                return True
            elif cardType[numElements1.most_common(2)[0][0]] == cardType[numElements2.most_common(2)[0][0]] or cardType[numElements1.most_common(2)[0][0]] == cardType[numElements2.most_common(2)[1][0]]:
                if cardType[numElements1.most_common(2)[1][0]] > cardType[numElements2.most_common(2)[1][0]] or cardType[numElements1.most_common(2)[1][0]] > cardType[numElements2.most_common(2)[0][0]]:
                    return True
                elif cardType[numElements1.most_common(2)[1][0]] == cardType[numElements2.most_common(2)[1][0]] or cardType[numElements1.most_common(2)[1][0]] == cardType[numElements2.most_common(2)[0][0]]:
                    return self.hasHighCard(type, toCompare)
            return False
        
f = file("poker.txt")

games = [[(card[0],card[1]) for card in game.split(" ")] for game in f.read().split("\n")]

p1Wins = 0

def getKey(item):
    return cardType[item[0]]

for game in games:
    hand1 = hand(sorted(game[:5], key=lambda tup: getKey(tup)))
    hand2 = hand(sorted(game[5:], key=lambda tup: getKey(tup)))
    if hand1.score == hand2.score:
        if hand1.compareTo(hand1.score, hand2):
            print "hand1: " + str(hand1.cards) + " - " + str(hand1.score) + " hand2: " + str(hand2.cards) + " - " + str(hand2.score)
            p1Wins = p1Wins + 1
    if hand1.score > hand2.score:
        print "hand1: " + str(hand1.cards) + " - " + str(hand1.score) + " hand2: " + str(hand2.cards) + " - " + str(hand2.score)
        p1Wins = p1Wins + 1

print p1Wins
