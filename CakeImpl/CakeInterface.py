class CakeInterface:
    def __init__(self, weightInPounds=0, cost=0):
        self.cost = 0.0
        self.weightInPounds = weightInPounds

    def description(self) -> str:
        return ""

    def getCost(self) -> float:
        return self.cost
