class Lampe():

    def __init__(self, mediator):
        self.mediator = mediator
        self.state = 0

    def an(self):
        #Lampe nur einschalten, wenn sie nicht bereits leuchtet
        if self.state == 0:
            self.mediator.notify(self, "ON")
            self.state = 1
            print("Lampe leuchtet jetzt")
        else: 
            print("Lampe leuchtet bereits")
        

    def aus(self):
        #Lampe nur ausschalten, wenn sie leuchtet
        if self.state == 1:
            self.state = 0
            print("Lampe leuchtet jetzt nicht mehr, keine Benachrichtigung nötig")
        else:
            print("Lampe ist schon ausgeschaltet")