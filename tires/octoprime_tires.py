from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3.0