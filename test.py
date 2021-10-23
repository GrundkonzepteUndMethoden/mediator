import Lampe 

def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(Lampe)

    print("just test doctest")

if __name__ == "__main__":
    test()
