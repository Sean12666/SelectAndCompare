import random


class Player:
    """A class for Players."""

    counter = 0

    def __init__(self, name):
        self.counter += 1
        self.num = self.counter
        self.name = name
        self.score = 0
        self.item = ""

    def getnum(self):
        return self.num

    def getname(self):
        return self.name

    def getscore(self):
        return self.score

    def addscore(self, val):
        self.score += val

    def getitem(self):
        return self.item

    def select_item(self, item):
        self.item = item

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score


if __name__ == "__main__":
    p1 = Player(input("Player1's name: "))
    p2 = Player(input("Player2's name: "))
    seq = input("Enter a sequence:\n").split()
    random.shuffle(seq)
    while len(seq) >= 2:
        p1.item = seq.pop(int(input("{0}, select an item: ".format(p1.getname()))))
        p2.item = seq.pop(int(input("{0}, select an item: ".format(p2.getname()))))
        print("{0}: {1}".format(p1.getname(), p1.getitem()))
        print("{0}: {1}".format(p2.getname(), p2.getitem()))
