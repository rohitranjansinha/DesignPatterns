from CakeImpl.CakeInterface import CakeInterface


class Message(CakeInterface):
    def __init__(self, cake: CakeInterface, message=""):
        super().__init__()
        self.cake = cake
        self.message = message

    def description(self) -> str:
        return self.cake.description() + " Message: " + self.message

    def getCost(self) -> float:
        return self.cake.getCost() + 50.0
