# import time
import datetime # imported for due_date and date_created fields
# import calendar # imported for date functions
# describes the task class

class Task:
    name = ''
    description = '' 
    due_date
    is_done = False
    priority = 3 # priority of 1 to 3, 1 being high, 2 being medium, 3 being low
    date_created = date.today() + ',' + date.time()
   
    def __init__(self, name):
        self.name = name

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

