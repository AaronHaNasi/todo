import task
# this class allows for the creation of multiple todo lists 
# this would allow someone to have multiple categories of todos
class Task_List:
    name = ''
    description = ''
    list_of_tasks = []

    def __init__(self, name):
        self.name = name

