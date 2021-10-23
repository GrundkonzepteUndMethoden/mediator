from Fenster import Fenster
from Eingang import Eingang
from Mediator import Mediator
from Lampe import Lampe

class Heizung():
    """Test instanciation of Lampe.
    >>> smartHomeMediator = Mediator()
    >>> heizung = Heizung(smartHomeMediator)
    >>> fenster = Fenster(smartHomeMediator)
    >>> eingang = Eingang(smartHomeMediator)
    >>> lampe = Lampe(smartHomeMediator)
    >>> smartHomeMediator.afterInit(heizung, fenster, eingang, lampe)

    >>> type(lampe)
    <class 'Lampe.Lampe'>

    Test an() of Lampe.
    >>> lampe.an()
    Mediator handled Lampe einschalten
    Fenster ist bereits geschlossen
    Lampe leuchtet jetzt

    Test aus() of Lampe.
    >>> lampe.aus()
    Lampe leuchtet jetzt nicht mehr, keine Benachrichtigung nötig
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

