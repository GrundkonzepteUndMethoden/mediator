
class Fenster():
    def __init__(self, mediator):
        self.mediator = mediator
        self.state = 0

    def auf(self):
        #Fenster nur öffnen, wenn es geschlossen ist
        if self.state == 0:
            self.mediator.notify(self, "OPEN")
            self.state = 1
            print("Fenster ist jetzt geöffnet")
        else:
            print("Fenster ist bereits geöffnet")


    def zu(self):
        #Fenster nur schließen, wenn es geöffnet ist
        if self.state == 1:
            self.state = 0
            print("Fenster ist jetzt geschlossen, keine Benachrichtung nötig")
        else: 
            print("Fenster ist bereits geschlossen")


