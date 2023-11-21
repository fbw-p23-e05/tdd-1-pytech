class CatController:
    def __init__(self) -> None:
        self.additional_water_hours = [9, 10, 11, 13, 14, 15, 16, 18, 19]

    def hourly_run(self, hour):
        actions = set()

        if hour in [8, 17]:
            actions.update(['Give water.', "Feed", "1 mouse", "1 chicken"])
        elif hour == 12:
            actions.update(["Feed", "1 hamster"])
        elif hour == 7:
            actions.add("Open cat cage.")
        elif hour == 20:
            actions.add("Close cat cage.")
        elif hour in self.additional_water_hours:
            actions.add('Give water.')
        else:
            actions.add('Nothing')

        return actions