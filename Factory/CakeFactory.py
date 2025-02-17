from CakeImpl import CakeInterface
from CakeImpl.BreadCake import BreadCake
from CakeImpl.CheeseCake import CheeseCake
from CakeImpl.PlumCake import PlumCake


class CakeFactory:
    def __init__(self, typeOfCake, weightInPounds):
        self.typeOfCake = typeOfCake
        self.weightInPounds = weightInPounds

    def makeCake(self):
        match self.typeOfCake.lower():
            case "bread cake":
                return BreadCake(self.weightInPounds)
            case "plum cake":
                return PlumCake(self.weightInPounds)
            case "cheese cake":
                return CheeseCake(self.weightInPounds)

