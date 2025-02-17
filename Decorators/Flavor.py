from CakeImpl.CakeInterface import CakeInterface
from Decorators.CakeDecorator import CakeDecorator


class Flavor(CakeDecorator):
    def __init__(self, cake: CakeInterface, flavorType: str):
        super().__init__(cake)
        self.flavorType = flavorType

    def description(self) -> str:
        return self.cake.description() + " Flavor: " + self.flavorType

    def getCost(self) -> float:
        match self.flavorType.lower():
            case "vanilla":
                return self.cake.getCost() + 102.0
            case "chocolate":
                return self.cake.getCost() + 177.0
            case "blueberry":
                return self.cake.getCost() + 204.0
        return self.cake.getCost()