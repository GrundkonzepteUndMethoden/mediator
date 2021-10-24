from abc import ABC, abstractmethod


class IFenster(ABC):

    @abstractmethod
    def auf(self):
        pass

    @abstractmethod
    def zu(self):
        pass



class Fenster(IFenster):
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

class FensterStub(IFenster):
    def an(self):
        print("Befehl erhalten: Fenster öffnen")

    def aus(self):
        print("Befehl erhalten: Fenster schließen")
