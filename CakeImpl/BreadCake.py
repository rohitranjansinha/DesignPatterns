from CakeImpl.CakeInterface import CakeInterface


class BreadCake(CakeInterface):
    def __init__(self, weightInPounds):
        super().__init__(weightInPounds)

    def bake(self):
        print("Baking a bread cake\n")

