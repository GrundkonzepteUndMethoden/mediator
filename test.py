import main

def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(main)

    print("just test doctest")

if __name__ == "__main__":
    test()
