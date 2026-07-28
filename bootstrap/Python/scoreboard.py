class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print("Cricket Player:", self.__player, "|Score:", self.__score)
    def play(self):
        print(self.__player, "is playing Cricket")
    def set_score(self, score):
        if score >= 0:
            self.__score = score
        else:
            print("Invalid Score")
class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print("Football Player:", self.__player, "|Score:", self.__score)
    def play(self):
        print(self.__player, "is playing Football")
    def set_score(self, score):
        if score >= 0:
            self.__score = score
        else:
            print("Invalid Score")
cricket = Cricket("Virat", 95)
football = Football("Messi", 3)
sports[cricket, football]
for sport in sports:
    sport.info()
    sport.play()
    print()
cricket.__score = -20
print("After direct change attempt:")
cricket.info()
print()
cricket.set_score(120)
print("After setter update:")
cricket.info()