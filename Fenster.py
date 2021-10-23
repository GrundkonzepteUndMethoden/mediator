from Heizung import Heizung
from Eingang import Eingang
from Mediator import Mediator
from Lampe import Lampe

class Fenster():
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


