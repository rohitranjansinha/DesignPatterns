from CakeImpl.CakeInterface import CakeInterface


class PlumCake(CakeInterface):
    def __init__(self, weightInPounds):
        super().__init__(weightInPounds)

    def description(self):
        return "Baking a plum cake"

    def getCost(self) -> float:
        return super().getCost() + (self.weightInPounds*200)