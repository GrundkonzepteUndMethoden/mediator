class Eingang():
    
    def __init__(self, mediator):
        self.mediator = mediator

    def betreten(self):
        self.mediator.notify(self, "ENTER")
        print("Das smartHome wurde betreten")

    def verlassen(self):
        self.mediator.notify(self, "EXIT")
        print("Das smartHome wurde verlassen")


