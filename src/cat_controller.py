
class CatController:
    def __init__(self):
        self.meat_dispenser = MeatDispenser()
        self.water_dispenser = WaterDispenser()
        self.cage = Cage()

    def hourly_run(self, hour):
        actions = []
        if hour == 7:
            actions.append(self.cage.open())
        elif hour == 20:
            actions.append(self.cage.close())
        elif hour in [8, 12, 17]:
            actions.append(self.meat_dispenser.feed())
        if hour in [8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]:
            actions.append(self.water_dispenser.give())
        return " ".join(actions)


class MeatDispenser:
    def feed(self):
        return "Feed the cat with 1 mouse, 1 hamster, and 1 chicken."

class WaterDispenser:
    def give(self):
        return "Give water."

class Cage:
    def open(self):
        return "Open cat cage."

    def close(self):
        return "Close cat cage."
