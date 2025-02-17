from CakeImpl.CakeInterface import CakeInterface


class CheeseCake(CakeInterface):
    def __init__(self, weightInPounds):
        super().__init__(weightInPounds)

    def bake(self):
        print("Baking a cheesecake\n")