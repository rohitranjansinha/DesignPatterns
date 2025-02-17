from CakeImpl.BreadCake import BreadCake
from CakeImpl.PlumCake import PlumCake
from Decorators.Flavor import Flavor
from Decorators.Message import Message

cake1 = BreadCake(1)
cake1 = Flavor(cake1, "vanilla")
cake1 = Message(cake1, "happy birthday")

cake2 = PlumCake(0.5)
cake2 = Flavor(cake2, "blueberry")

if __name__ == "__main__":
    print(cake1.description())
    print("Cost1 = "+str(cake1.getCost()))
    print(cake2.description())
    print("Cost2 = " + str(cake2.getCost()))