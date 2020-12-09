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

    def __eq__(self, other):
        return self.getscore() == other.getscore()

    def __gt__(self, other):
        return self.getscore() > other.getscore()

    def __lt__(self, other):
        return self.getscore() < other.getscore()

    def __ne__(self, other):
        return self.getscore() != other.getscore()


if __name__ == "__main__":
    p1 = Player(input("Player1's name: "))
    p2 = Player(input("Player2's name: "))
    seq = input("Enter a sequence:\n").split()
    seq.sort()
    print("Sorted sequence:", seq)
    random.shuffle(seq)
    print("Sequence shuffled.")
    while len(seq) >= 2:
        p1.select_item(seq.pop(int(input("{0}, select an item in [0, {1}): ".format(p1.getname(), len(seq))))))
        p2.select_item(seq.pop(int(input("{0}, select an item in [0, {1}): ".format(p2.getname(), len(seq))))))
        print("{0}: {1}".format(p1.getname(), p1.getitem()))
        print("{0}: {1}".format(p2.getname(), p2.getitem()))
        if p1.getitem() > p2.getitem():
            print("{0}'s item is greater!".format(p1.getname()))
            p1.addscore(2)
        elif p2.getitem() > p1.getitem():
            print("{0}'s item is greater!".format(p2.getname()))
            p2.addscore(2)
        else:
            print("{0}'s item is as great as {1}'s item.".format(p1.getname(), p2.getname()))
            p1.addscore(1)
            p2.addscore(1)
        print("Score:", p1.getscore(), ":", p2.getscore())
    print("Game over!")
    if p1 != p2:
        print(p1.getname() if p1 > p2 else p2.getname(), "wins!")
    else:
        print("The game is tied.")
