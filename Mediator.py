from abc import abstractmethod, ABC

class IMediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


#TestStub für die Unit Tests der Components
class MediatorStub(IMediator):
    def notify(self, sender, event):
        print("Notification erhalten, Event: " + event)

class Mediator(IMediator):
    # nicht in der init-Methode, da es sonst einen Zirkelbezug gibt
    # => Komponenten brauchen Mediator-Referenz, Mediator braucht 
    # Komponenten-Referenzen
    """
    Test instanciation of Mediator 
    >>> from Eingang import EingangStub
    >>> from Heizung import HeizungStub
    >>> from Fenster import FensterStub
    >>> from Lampe import LampeStub
    >>> eingangStub = EingangStub()
    >>> heizungStub = HeizungStub()
    >>> fensterStub = FensterStub()
    >>> lampeStub = LampeStub()

    >>> mediator = Mediator()
    >>> mediator.afterInit(heizungStub, fensterStub, eingangStub, lampeStub)

    >>> type(mediator)
    <class 'Mediator.Mediator'>

    Test notify(eingang, "ENTER") of Mediator
    >>> mediator.notify(eingangStub, "ENTER")
    Mediator handled Haus betreten
    Befehl erhalten: Lampe einschalten

    Test notify(eingang, "EXIT") of Mediator
    >>> mediator.notify(eingangStub, "EXIT")
    Mediator handled Haus verlassen
    Befehl erhalten: Lampe ausschalten
    Befehl erhalten: Fenster schließen
    Befehl erhalten: Heizung ausschalten
    

    Test notify(heizung, "ON") of Mediator
    >>> mediator.notify(heizungStub, "ON")
    Mediator handled Heizung einschalten
    Befehl erhalten: Fenster schließen
    

    Test notify(fenster, "OPEN") of Mediator
    >>> mediator.notify(fensterStub, "OPEN")
    Mediator handled Fenster öffnen
    Befehl erhalten: Heizung ausschalten
    Befehl erhalten: Lampe ausschalten

    Test notify(lampe, "ON") of Mediator
    >>> mediator.notify(lampeStub, "ON")
    Mediator handled Lampe einschalten
    Befehl erhalten: Fenster schließen
    """

    def afterInit(self, heizung, fenster, eingang, lampe):
        self.heizung = heizung
        self.fenster = fenster
        self.eingang = eingang
        self.lampe = lampe

    def notify(self, sender, event):
        # Abhängigkeiten sind in der Readme erklärt
        if sender == self.heizung:
            print("Mediator handled Heizung einschalten")
            self.fenster.zu()

        elif sender == self.fenster:
            print("Mediator handled Fenster öffnen")
            self.heizung.aus()
            self.lampe.aus()

        elif sender == self.lampe:
            print("Mediator handled Lampe einschalten")
            self.fenster.zu()

        elif sender == self.eingang:
            if event == "ENTER":
                print("Mediator handled Haus betreten")
                self.lampe.an()

            elif event == "EXIT": 
                print("Mediator handled Haus verlassen")
                self.lampe.aus()
                self.fenster.zu()
                self.heizung.aus()


        


        
