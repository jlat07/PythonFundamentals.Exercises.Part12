from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param parity: Adds
    :return:
    """
    if parity == Parity.ODD:
        list1 = list(range(start, stop, 1))
        new_list = list(filter((lambda x: x % 2 == 1), list1))
        return new_list
    elif parity == Parity.EVEN:
        list1 = list(range(start, stop, 1))
        new_list = list(filter((lambda x: x % 2 == 0), list1))
        return new_list
    


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    dicts = {}
    keys = range(start, stop)
    for i in keys:
        dicts[i] = strategy(i)
    return dicts


def gen_set(val_in: str) -> set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    so takes string. turns it into a set. which elminates duplicates(need to capitlize them some how)
    
    then takes string and turns into another set, where it takes the difference of capitale letters from the two sets
    
    """
    
    lst =list(val_in)
    lower_case = []
    upper_case = []
    for i in lst:
        if (i.islower()):
            lower_case.append(i)
    for i in lower_case:
        upper_case.append(i.upper())
    gen_set = set(upper_case)
    return gen_set
