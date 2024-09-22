__author__ = 'ROMANOV Sergey'
__version__ = '2.8.0'
RSL_DEBUG = False


def main ( *args, **kwargs ) :
    """
        Функция
        @:return result : int
    """
    result = int ( 0 )

    if RSL_DEBUG :
        print ( f'--->> Author module:\t\t{__author__}.' )
    else :
        if args > 5 :
            return exit ( 1 )
        return result
    return None


if __name__ == '__main__' :
    main ( )
