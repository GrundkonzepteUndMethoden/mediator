from Heizung import Heizung
from Fenster import Fenster
from Eingang import Eingang
from Mediator import Mediator

class Lampe():
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