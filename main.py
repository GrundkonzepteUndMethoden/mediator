from Heizung import Heizung
from Fenster import Fenster
from Eingang import Eingang
from Lampe import Lampe
from Mediator import Mediator
class main:
    """Tests of all methods.
    >>> smartHomeMediator = Mediator()
    >>> heizung = Heizung(smartHomeMediator)
    >>> fenster = Fenster(smartHomeMediator)
    >>> eingang = Eingang(smartHomeMediator)
    >>> lampe = Lampe(smartHomeMediator)
    >>> smartHomeMediator.afterInit(heizung, fenster, eingang, lampe)

    Test instantiation of Heizung
    >>> type(heizung)
    <class 'Heizung.Heizung'>

    Test instantiation of Fenster
    >>> type(fenster)
    <class 'Fenster.Fenster'>

    Test instantiation of Eingang
    >>> type(eingang)
    <class 'Eingang.Eingang'>

    Test instantiation of Lampe
    >>> type(lampe)
    <class 'Lampe.Lampe'>

    Test an() of Heizung.
    >>> heizung.an()
    Mediator handled Heizung einschalten
    Fenster ist bereits geschlossen
    Heizung heizt jetzt

    Test aus() of Heizung.
    >>> heizung.aus()
    Heizung heizt jetzt nicht mehr, keine Benachrichtigung nötig

    Test auf() of Fenster.
    >>> fenster.auf()
    Mediator handled Fenster öffnen
    Heizung ist schon aus
    Lampe ist schon ausgeschaltet
    Fenster ist jetzt geöffnet

    Test zu() of Fenster.
    >>> fenster.zu()
    Fenster ist jetzt geschlossen, keine Benachrichtung nötig

    Test betreten() of Eingang.
    >>> eingang.betreten()
    Mediator handled Haus betreten
    Mediator handled Lampe einschalten
    Fenster ist bereits geschlossen
    Lampe leuchtet jetzt
    Das smartHome wurde betreten

    Test verlassen() of Eingang.
    >>> eingang.verlassen()
    Mediator handled Haus verlassen
    Lampe leuchtet jetzt nicht mehr, keine Benachrichtigung nötig
    Fenster ist bereits geschlossen
    Heizung ist schon aus
    Das smartHome wurde verlassen

    Test an() of Lampe.
    >>> lampe.an()
    Mediator handled Lampe einschalten
    Fenster ist bereits geschlossen
    Lampe leuchtet jetzt

    Test aus() of Lampe.
    >>> lampe.aus()
    Lampe leuchtet jetzt nicht mehr, keine Benachrichtigung nötig
    """
    pass

if __name__ == "__main__":

    
    
    #2 Etagen => 2 Mediatoren
    
    smartHomeMediator = Mediator()
    heizung = Heizung(smartHomeMediator)
    fenster = Fenster(smartHomeMediator)
    eingang = Eingang(smartHomeMediator)
    lampe = Lampe(smartHomeMediator)
    smartHomeMediator.afterInit(heizung, fenster, eingang, lampe)

    print("SmartHome bereit")

    heizung.an()
    print()
    fenster.auf()
    print()
    eingang.verlassen()
    print()
    eingang.betreten()
    print()
    lampe.an()
    print()
    fenster.auf()
    print()
    
