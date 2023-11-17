class CatController:
    # TODO: You need to write the code for this class based on what the tests
    # expect.

    def __init__(self) -> None:
        self.additional_water_hours = [9, 10, 11, 13, 14, 15, 16, 18, 19]


    def hourly_run(self, hour):
        if hour in [8, 17]:
            return {'Give water.', "Feed", "1 mouse", "1 chicken"}
        elif hour == 12:
            return {"Feed", "1 hamster"}
        elif hour == 7:
            return {"Open cat cage."}
        elif hour == 20:
            return {"Close cat cage."}
        elif hour in self.additional_water_hours:
            return {'Give water.'}
        else:
            return {'Nothing'}

# cat = CatController()
# print('Give water.' in cat.hourly_run(8))

