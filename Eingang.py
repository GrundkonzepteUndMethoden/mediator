from Heizung import Heizung
from Fenster import Fenster
from Mediator import Mediator
from Lampe import Lampe

class Eingang():
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

    def betreten(self):
        self.mediator.notify(self, "ENTER")
        print("Das smartHome wurde betreten")

    def verlassen(self):
        self.mediator.notify(self, "EXIT")
        print("Das smartHome wurde verlassen")


