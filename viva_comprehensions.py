from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param parity: Based on which parity is passed, the method will be applied to each item in the list
    :return: Returns a list in specified range parity
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
    :param start: Key value start (inclusive).
    :param stop: Key value end (exclusive).
    :param strategy: takes in a lambda function to carryout on each item in the list
    :return: Returns a dict with keys in range, and a value with a strategy applied for each key value
    """
    dicts = {}
    keys = range(start, stop)
    for i in keys:
        dicts[i] = strategy(i)
    return dicts


def gen_set(val_in: str) -> set:
    """
    :param val_in: Takes in a string
    :return: Returns a set of only lower case distanct characters from the string, and returns them capitalized in the set.
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
