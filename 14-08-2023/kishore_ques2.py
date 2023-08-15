class Print:
    def __init__(self):
        self.printingTasks = []
        self.max_queue_length = 5  # Maximum length of the printing tasks queue

    def addPrintTaskToSchedule(self, printTask):
        if len(self.printingTasks) < self.max_queue_length:
            self.printingTasks.append(printTask)
            print(f"Added task: {printTask}")
        else:
            print("Queue is full. Cannot add more tasks.")

    def printingTheTask(self):
        if len(self.printingTasks) == 0:
            print("No Tasks")
            return
        else:
            while self.printingTasks:
                printTask = self.printingTasks.pop(0)
                print(f"Printing: {printTask}")

# Test the Print class
printScheduler = Print()

printScheduler.addPrintTaskToSchedule("Sravya's resume")
printScheduler.addPrintTaskToSchedule("Krishna's wiki page for Telangana tourism")
printScheduler.addPrintTaskToSchedule("Bindu's Mahesh Babu poster")
printScheduler.addPrintTaskToSchedule("Sandeep's research paper")
printScheduler.addPrintTaskToSchedule("Neha's birthday invitation")
printScheduler.addPrintTaskToSchedule("Rahul's project proposal")

printScheduler.printingTheTask()
