

class Heizung():
    def __init__(self, mediator):
        self.mediator = mediator
        self.state = 0


    def an(self):
        #Heizung nur einschalten, wenn sie aus ist
        if self.state == 0:
            self.mediator.notify(self, "ON")
            self.state = 1
            print("Heizung heizt jetzt")
        else:
            print("Heizung heizt bereits")


    def aus(self):
        #Heizung nur ausschalten, wenn sie an ist
        if self.state == 1:
            self.state = 0
            print("Heizung heizt jetzt nicht mehr, keine Benachrichtigung nötig")
        else: 
            print("Heizung ist schon aus")

