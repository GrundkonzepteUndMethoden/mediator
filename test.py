import Eingang
import Heizung
import Fenster
import Lampe
import Mediator


def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(Eingang)
    doctest.testmod(Heizung)
    doctest.testmod(Fenster)
    doctest.testmod(Lampe)
    doctest.testmod(Mediator)

    print("just test doctest")

if __name__ == "__main__":
    test()
