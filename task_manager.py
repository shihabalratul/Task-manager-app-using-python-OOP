from datetime import datetime
import uuid

class Task_Manager:
    __tasks = []
    def __init__(self):
        pass

    def add_task(self, task):
        Task_Manager.__tasks.append(task)
        print("\nTask Created Successfully\n")
    
    def show_tasks(self, numbering = False):
        if not len(self.__tasks):
            print("\nNo Task Created Yet\n")
        else:
            for index, task in enumerate(self.__tasks):
                print("\n")
                if numbering == True:
                    print(f"Task No - {index+1}")
                print(task)

    def show_incompleted(self, numbering = False):
        is_empty = True
        incompleted = []
        count = 0
        for index, task in enumerate(self.__tasks):
            if task.task_done == False:
                print("\n")
                if numbering == True:
                    count+=1
                    print(f"Task No - {count}")
                    incompleted.append(task)
                print(task)
                is_empty = False


        if is_empty == True:
            print("\nNo Incomplete Task\n")

        if numbering == True:
            return incompleted
    
    def show_completed(self):
        is_empty = True
        for task in self.__tasks:
            if task.task_done == True:
                print("\n")
                print(task)
                is_empty = False

        if is_empty == True:
            print("\nNo Complete Task\n")

    def update(self):
        print("\nSelect which task to update\n")

        self.show_tasks(True)

        choice = int(input("Enter Task No: "))
        name = input("Enter New Task: ")
        task = self.__tasks[choice-1]

        task.update_task(name)

    def mark_completed(self):
        print("\nSelect Which Task to Complete\n")
        incompleted = self.show_incompleted(True)

        choice = int(input("Enter Task Number: "))

        incompleted[choice-1].complete_task()



class Task(Task_Manager):
    
    def __init__(self, task) -> None:
        self.task = task
        self.created_time = datetime.now()
        self.updated_task = None
        self.completed_time = None
        self.task_done = False
        self.__id = uuid.uuid4()
        super().add_task(self)
    
    def __repr__(self) -> str:
        return f"ID - {self.__id}\nTask - {self.task}\nCreated time - {self.created_time}\nUpdated time - {self.updated_task if self.updated_task else 'NA'}\nCompleted - {self.task_done}\nCompleted time - {self.completed_time if self.completed_time else 'NA'}\n"


    def update_task(self, task_name):
        self.task = task_name
        self.updated_task = datetime.now()

    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.now()




task_manager = Task_Manager()

while True:
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Task")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")
    choice = int(input("Enter Option: "))

    if choice == 1:
        name = input("Enter New Task: ")
        self = Task(name)
    elif choice == 2:
        task_manager.show_tasks()
    elif choice == 3:
        task_manager.show_incompleted()
    elif choice == 4:
        task_manager.show_completed()
    elif choice == 5:
        task_manager.update()
    elif choice == 6:
        task_manager.mark_completed()





