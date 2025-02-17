from CakeImpl.BreadCake import BreadCake
from Decorators.Flavor import Flavor
from Decorators.Message import Message

cake1 = BreadCake(1)
cake1 = Flavor(cake1, "vanilla")
cake1 = Message(cake1, "happy birthday")

if __name__ == "__main__":
    print(cake1.description())
    print("Cost = "+str(cake1.getCost()))