from Eingang import Eingang
import main
import Eingang

def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(main)
    doctest.testmod(Eingang)

    print("just test doctest")

if __name__ == "__main__":
    test()
