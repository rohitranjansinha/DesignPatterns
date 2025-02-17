from CakeImpl.CakeInterface import CakeInterface


class PlumCake(CakeInterface):
    def __init__(self, weightInPounds):
        super().__init__(weightInPounds)

    def bake(self):
        print("Baking a plum cake\n")