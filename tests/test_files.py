# -*- coding: utf-8 -*-

from io import StringIO
import utools.files as ufiles


# --- utools.file.read_item ---

def test_read_item():
    string_io = StringIO("1\n2\n3\nab\n\nfoo")
    assert ufiles.read_item(string_io, bool) is True
    assert ufiles.read_item(string_io, str) == "2"
    assert ufiles.read_item(string_io, int) == 3
    assert ufiles.read_item(string_io, list) == ["a", "b"]
    assert ufiles.read_item(string_io, str) == ""
    assert ufiles.read_item(string_io, set) == {"f", "o"}


def test_read_multiple_items():
    string_io = StringIO("1\n2 3 4\n5,6,7,\n8-9")
    assert ufiles.read_mutiple_items(string_io, list, int) == [1]
    assert ufiles.read_mutiple_items(string_io, tuple, float) == (2., 3., 4.)
    assert ufiles.read_mutiple_items(string_io, set, bool, ",") == {True, False}
    assert ufiles.read_mutiple_items(string_io, list, str, " ") == ["8-9"]


def test_read_complex_file():
    # the original purpose of these methods was to easily parse Google Code Jam's input files
    # the following example corresponds to this problem:
    # https://code.google.com/codejam/contest/4304486/dashboard#s=p1
    string_io = StringIO("3\n3\n1 2 3\n2 3 5\n3 5 6\n2 3 4\n1 2 3\n"
                         "4\n7 9 12 13\n3 5 6 12\n2 4 5 10\n1 2 3 7\n1 2 3 8\n3 5 6 11\n8 10 11 13\n"
                         "2\n4 8\n2 6\n6 8")
    t = ufiles.read_item(string_io, int)
    assert t == 3
    for _i in range(t):
        n = ufiles.read_item(string_io, int)
        for _j in range(2 * n - 1):
            sublist = ufiles.read_mutiple_items(string_io, list, int, separator=" ")
            assert len(sublist) == n
