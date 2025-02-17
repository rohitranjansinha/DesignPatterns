from CakeImpl.CakeInterface import CakeInterface


class BreadCake(CakeInterface):
    def __init__(self, weightInPounds):
        super().__init__(weightInPounds)

    def description(self):
        return "Baking a bread cake"

    def getCost(self) -> float:
        return super().getCost() + (self.weightInPounds*250)
