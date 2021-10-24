from Eingang import Eingang
import main
import Eingang
import Mediator

def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(main)
    doctest.testmod(Eingang)
    doctest.testmod(Mediator)

    print("just test doctest")

if __name__ == "__main__":
    test()
