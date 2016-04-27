# -*- coding: utf-8 -*-

""" Useful functions to work with dictionaries.
"""


def deep_get(d, *keys, default=None):
    """ Recursive safe search in a dictionary of dictionaries.

    Args:
        d: the dictionary to work with
        *keys: the list of keys to work with
        default: the default value to return if the recursive search did not succeed

    Returns:
        The value wich was found recursively in d, or default if the search did not succeed

    Example:

        >>> d = {"user": {"id": 1, "login": "foo"}, "date": "2016-04-27"}
        >>> deep_get(d, "user", "login")
        "foo"
        >>> deep_get(d, "user")
        {"id": 1, "login": "foo"}
        >>> deep_get(d, "user", "name")
        None
        >>> deep_get(d, "user", "name", default="bar")
        "bar"
    """

    for key in keys:
        try:
            d = d[key]
        except (KeyError, IndexError, TypeError):
            return default
    return d
