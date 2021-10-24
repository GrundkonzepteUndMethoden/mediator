from Heizung import Heizung
from Fenster import Fenster
from Eingang import Eingang
from Lampe import Lampe
from Mediator import Mediator

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
    
