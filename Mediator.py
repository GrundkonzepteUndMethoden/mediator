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


        


        
