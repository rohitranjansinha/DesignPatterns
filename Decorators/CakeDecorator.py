from CakeImpl.CakeInterface import CakeInterface


class CakeDecorator(CakeInterface):
    def __init__(self, cake=None):
        super().__init__()
        self.cake = cake
