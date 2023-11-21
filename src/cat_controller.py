# src/cat_controller.py

class CatController:
    def __init__(self):
        self.cage_locked = False
        self.meat_dispenser_status = "Idle"
        self.water_dispenser_status = "Idle"

    def lock_cage(self):
        self.cage_locked = True
        return "Cage locked."

    def unlock_cage(self):
        self.cage_locked = False
        return "Cage unlocked."

    def dispense_meat(self):
        self.meat_dispenser_status = "Dispensing meat."
        return "Meat dispensed."

    def dispense_water(self):
        self.water_dispenser_status = "Dispensing water."
        return "Water dispensed."
