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
    n = int(input("How many players: "))
    p = []
    for i in range(n):
        p.append(Player(input("{0}\tName: ".format(i))))
    seq = input("Enter a sequence:\n").split()
    seq.sort()
    print("Sorted sequence:", seq)
    random.shuffle(seq)
    print("Sequence shuffled.")
    while len(seq) >= n:
        for i in range(n):
            p[i].select_item(seq.pop(int(input("{0}, select an item in [0, {1}): ".format(p[i].getname(), len(seq))))))
            print("{0}: {1}".format(p[i].getname(), p[i].getitem()))
        max(p, key=lambda x: x.getitem()).addscore(2)
    print("Game over!")
    p.sort(reverse=True)
    print("No.", "Name", "Score", sep='\t')
    for num, plr in enumerate(p):
        print(num, plr.getname(), plr.getscore(), sep='\t')
