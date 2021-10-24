from abc import abstractmethod, ABC
from Mediator import MediatorStub


class IEingang(ABC):
    @abstractmethod
    def betreten(self):
        pass

    @abstractmethod
    def verlassen(self):
        pass


class Eingang(IEingang):
    """ 
    Test instanciation of Eingang
    >>> mediatorStub = MediatorStub()
    >>> eingang = Eingang(mediatorStub)
    >>> type(eingang)
    <class 'Eingang.Eingang'>

    Test betreten() of Eingang
    >>> eingang.betreten()
    Notification erhalten, Event: ENTER
    Das smartHome wurde betreten

    Test verlassen() of Eingang
    >>> eingang.verlassen()
    Notification erhalten, Event: EXIT
    Das smartHome wurde verlassen
    """

    def __init__(self, mediator):
        self.mediator = mediator
   
    def betreten(self):
        self.mediator.notify(self, "ENTER")
        print("Das smartHome wurde betreten")

    def verlassen(self):
        self.mediator.notify(self, "EXIT")
        print("Das smartHome wurde verlassen")

#TestStub für die Unit Tests des Mediators
class EingangStub(IEingang):
    def betreten(self):
        pass

    def verlassen(self):
        pass




