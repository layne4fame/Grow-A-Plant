class plant:

    def __init__(self, name, baseHappy, range):
        self.name = name
        self.baseHappy = baseHappy
        self.range = range
        self.lightlevel = 0
        self.total = 0

    def calculateHappy(self, temp):
        if self.range[0] <= temp <= self.range[1] and self.lightlevel > .5:
            if self.baseHappy == 100:
                return
            self.baseHappy = self.baseHappy + 1
            return
        if self.baseHappy == 0:
            return
        self.baseHappy = self.baseHappy - 1

    def calculateLightLevel(self, light, count):
        if light:
            self.total = self.total + 1
        self.lightlevel = self.total/count


