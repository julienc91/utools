# -*- coding: utf-8 -*-

import pytest
from utools import dicts as udicts


# --- utools.dicts.deep_get ---
def test_deep_get():

    d = {"user": {"id": 1, "login": "foo"}, "date": "2016-04-27"}
    assert udicts.deep_get(d) == d
    assert udicts.deep_get(d, default=3) == d
    assert udicts.deep_get(d, "user", "login") == "foo"
    assert udicts.deep_get(d, "user") == {"id": 1, "login": "foo"}
    assert udicts.deep_get(d, "user", "name") is None
    assert udicts.deep_get(d, "user", "name", default="bar") == "bar"
    assert udicts.deep_get(d, "user", "login", default="bar") == "foo"

    # deep_get should also work with lists
    d = [[[3], 4]]
    assert udicts.deep_get(d, 0, 0, 0) == 3
    assert udicts.deep_get(d, 0, 0) == [3]
    assert udicts.deep_get(d, 0, 1) == 4
    assert udicts.deep_get(d, 0, 0, 0, 0) is None
    assert udicts.deep_get(d, 0, 3, 5, default=17) == 17


# deep_get should be safe and should never raise
@pytest.mark.parametrize("d", [
    1,
    "foo",
    {1, 2, 3},
    object(),
    int,
    None
])
def test_deep_get_with_safety(d):
    assert udicts.deep_get(d, "foo", 1, 4) is None
