# -*- coding: utf-8 -*-

""" Useful functions to manipulate files.
"""


def __read(f, decode):
    line = next(f).rstrip("\r\n")
    return decode(line)


def read_item(f, item_type):

    """ Extract a single item from the current line of a file-like object.

    Args:
        f (file): the file-like object to read from
        item_type (type): type of the element to extract

    Returns:
        The extracted element

    Example:
        The file "a.input" contains three lines and three with a single digit on each::

            >>> with open("a.input") as f:
            ...     print(utools.files.read_item(f, int))
            ...     print(utools.files.read_item(f, str))
            ...     print(utools.files.read_item(f, float))
            ...
            1
            "2"
            3.0
    """

    return __read(f, lambda line: item_type(line))


def read_mutiple_items(f, container_type, item_type, separator=" "):

    """ Extract an iterable from the current line of a file-like object.

    Args:
        f (file): the file-like object to read from
        container_type (type): type of the iterable that will be returned
        item_type (type): type of the values that will be elements of the returned iterable
        separator (str): the separator between two consecutive items

    Returns:
        The extracted iterable

    Example:
        The file "a.input" contains three lines and three comma-separated digits on each::

            >>> with open("a.input") as f:
            ...     print(utools.files.read_multiple_items(f, list, int, separator=","))
            ...     print(utools.files.read_multiple_items(f, set, str, separator=","))
            ...     print(utools.files.read_multiple_items(f, tuple, float, separator=","))
            ...
            [1, 2, 3]
            {"4", "5", "6"}
            (7.0, 8.0, 9.0)
    """

    return __read(f, lambda line: container_type(item_type(item) for item in line.split(separator)))
