from termcolor import colored, cprint

RSL_NAME_AUTHOR = 'ROMANOV Sergey'
RSL_DEBUG = False


def main ( ) :
    """
        Функция
        @:params
        @:return result : int
    """
    result = int (0)

    if RSL_DEBUG :
        print (
                f'--->> Author module: '
                f'{RSL_NAME_AUTHOR}.'
                )
        result += result + 1
    else : return result
    return None


if __name__ == '__main__' :
    main ( )
