from vehicle import Vehicle


class Truck(Vehicle):
    carry_limit = None
    current_carriage_weight = None

    def has_carriage(self):
        return self.current_carriage_weight is not None

    def attach_carriage(self, weight):
        if (weight <= self.carry_limit):
            self.current_carriage_weight = weight
            return True
        else:
            return False

    def detach_carriage(self):
        self.current_carriage_weight = None
