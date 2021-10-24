from abc import ABC, abstractmethod
from Mediator import MediatorStub

class IFenster(ABC):

    @abstractmethod
    def auf(self):
        pass

    @abstractmethod
    def zu(self):
        pass



class Fenster(IFenster):
    """ 
    Test instanciation of Fenster
    >>> mediatorStub = MediatorStub()
    >>> fenster = Fenster(mediatorStub)
    >>> type(fenster)
    <class 'Fenster.Fenster'>

    Test auf() of Fenster mit state=0
    >>> fenster.auf()
    Notification erhalten, Event: OPEN
    Fenster ist jetzt geöffnet

    Test auf() of Fenster mit state=1
    >>> fenster.auf()
    Fenster ist bereits geöffnet

    Test zu() of Fenster mit state=1
    >>> fenster.zu()
    Fenster ist jetzt geschlossen, keine Benachrichtung nötig

    Test zu() of Fenster mit state=0
    >>> fenster.zu()
    Fenster ist bereits geschlossen
    """

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

#TestStub für die Unit Tests des Mediators
class FensterStub(IFenster):
    def auf(self):
        print("Befehl erhalten: Fenster öffnen")

    def zu(self):
        print("Befehl erhalten: Fenster schließen")
