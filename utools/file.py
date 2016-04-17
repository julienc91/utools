# -*- coding: utf-8 -*-


def __read(f, decode):
    line = next(f).rstrip("\r\n")
    return decode(line)


def read_item(f, item_type):
    return __read(f, lambda line: item_type(line))


def read_mutiple_items(f, container_type, value_type, separator=" "):
    return __read(f, lambda line: container_type(value_type(item) for item in line.split(separator)))
