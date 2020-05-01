class Auto:
    def __init__(self, model):
        self.model = model

    def stay(self):
        return 'Stay'

    def move(self):
        return 'Move'


class Car(Auto):
    def __init__(self, model, passengers_max):
        super().__init__(model)
        self.passengers_max = passengers_max


class Truck(Auto):
    def __init__(self, model, carrying_capacity):
        super().__init__(model)
        self.carrying_capacity = carrying_capacity
        self.cargo_weight = 0

    def move(self):
        if self.cargo_weight <= self.carrying_capacity:
            return 'Move'
        else:
            return 'Overload'

    def increase_cargo_weight(self, weight):
        self.cargo_weight += weight

    def decrease_cargo_weight(self, weight):
        self.cargo_weight -= weight
