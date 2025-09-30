from abc import ABC, abstractmethod

#Factory Method
class Task(ABC):
    def __init__(self, name):
        self.name = name
        self.status = "Not Started"
        self.observers = []
 
    #Attach an observer(users)
    def attach(self, observer):
        self.observers.append(observer)

    def notify(self): #notify all observers about status change
        for obs in self.observers:
            obs.update(self)


    def change_status(self, status):
        self.status = status
        self.notify()

#Task Types
class DesignTask(Task): pass
class ReviewTask(Task): pass
class DeploymentTask(Task): pass

class TaskFactory:
    @staticmethod
    def create_task(task_type, name):
        if task_type == "Design": 
            return DesignTask(name)
        elif task_type == "Review": 
            return ReviewTask(name)
        elif task_type == "Deployment": 
            return DeploymentTask(name)
        else:
            raise ValueError("Invalid task type")


#Observer Pattern
class User:
    def __init__(self, name):
        self.name = name
    
    def update(self, task):
        print(f"**{self.name} has been notified: Task '{task.name}' status changed to {task.status}")

#Singleton Pattern
class TaskManager:
    _instance = None #Holds single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task, user): #Add task and assign it to user
        task.attach(user)
        self.tasks.append(task)

if  __name__ == "__main__":
    manager = TaskManager()

    # users
    jordan = User("Jordan")
    alex = User("Alex")

    #Using Fctory to create tasks
    t1 = TaskFactory.create_task("Design", "Design")
    t2 = TaskFactory.create_task("Review", "Review")
    t3 = TaskFactory.create_task("Deployment", "Deploy")

    #Assigning tasks to different users
    manager.add_task(t1, jordan)
    manager.add_task(t2, alex)
    manager.add_task(t3, jordan)

    t1.change_status("In Progress")
    t2.change_status("Completed")
    t3.change_status("In Progress")
    
    t1.change_status("In Progress")
    t2.change_status("Completed")
    t3.change_status("In Progress")
    
    
    
    
    
    
    
    
    
    
    
    