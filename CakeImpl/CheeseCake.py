from CakeImpl.CakeInterface import CakeInterface


class CheeseCake(CakeInterface):
    def __init__(self, weightInPounds):
        super().__init__(weightInPounds)

    def description(self):
        return "Baking a cheesecake"

    def getCost(self) -> float:
        return super().getCost() + (self.weightInPounds*350)