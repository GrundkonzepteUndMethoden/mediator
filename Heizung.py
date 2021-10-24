from abc import ABC, abstractmethod
from Mediator import MediatorStub

class IHeizung(ABC):

    @abstractmethod
    def an(self):
        pass

    @abstractmethod
    def aus(self):
        pass



class Heizung(IHeizung):
    """
    >>> mediatorStub = MediatorStub()
    >>> heizung = Heizung(mediatorStub)
    >>> type(heizung)
    <class 'Heizung.Heizung'>

    Test an() of Heizung mit state=0
    >>> heizung.an()
    Notification erhalten, Event: ON
    Heizung heizt jetzt

    Test an() of Heizung mit state=1
    >>> heizung.an()
    Heizung heizt bereits

    Test aus() of Heizung mit state=1
    >>> heizung.aus()
    Heizung heizt jetzt nicht mehr, keine Benachrichtigung nötig

    Test aus() of Heizung mit state=0
    >>> heizung.aus()
    Heizung ist schon aus
    """

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

#TestStub für die Unit Tests des Mediators
class HeizungStub(IHeizung):
    def an(self):
        print("Befehl erhalten: Heizung einschalten")

    def aus(self):
        print("Befehl erhalten: Heizung ausschalten")