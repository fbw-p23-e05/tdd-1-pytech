

class CatController:
    # TODO: You need to write the code for this class based on what the tests
    # expect.
    def hourly_run(self, hour):  
        
        water = "Give water."
        cage_open = "Open cat cage."
        cage_close = "Close cat cage."
        feed = "Feed"
        food = ["1 mouse", "1 hamster", "1 chicken"]
        result=[]
        
        if hour in [8, 12, 17]:
            result += [feed]
            if hour == 8:
                result += [food[0]]
            elif hour == 12:
                result += [food[1]]
            elif hour == 17:
                result += [food[2]]
        if hour in [8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]:
            result += [water]
        elif hour == 7:
            result += [cage_open]
        elif hour == 20:
            result += [cage_close]
        else:
            if hour == 12:
                result
            else:
                result = []
            
        return result
        



# if hour corresponds to any of 8,9,10,11,13,14,15,16,17,18 ans 19
#    and  'Give water' is not accociated with those numbers
#       denn it is false
# but 'Give water' is accociated with a number other than 8,9,10,11,13,14,15,16,17,18 ans 19
#       denn it is also false

# test_failed = False
# cat_controller = CatController()

# for hour in range(0, 23): 
#     if hour in WATER_HOURS: 
#         if not "Give water." in cat_controller.hourly_run(hour):
#             test_failed = True
#     elif "Give water." in cat_controller.hourly_run(hour):
#         test_failed = True
    
#     print(hour, test_failed, cat_controller.hourly_run(hour))



# not_yet_fed = ["1 mouse", "1 hamster", "1 chicken"]
# not_yet_fed.remove("1 chicken")
# print(not_yet_fed)


