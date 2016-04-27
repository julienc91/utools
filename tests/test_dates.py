# -*- coding: utf-8 -*-

from utools import dates as udates


def test_timer():

    timer = udates.timer()

    # no with block, the timer should not have started
    assert timer.get() == 0
    assert not timer.ongoing()

    # a simple with block
    with timer:
        assert timer.ongoing()
        pass
    assert not timer.ongoing()
    assert timer.get() > 0

    # a simple with block with an exception
    try:
        with timer:
            raise SystemError
    except SystemError:
        pass
    assert timer.get() > 0
    assert timer.get() == timer.get()

    timer.reset()
    assert timer.get() == 0
    assert not timer.ongoing()

    timer.start()
    assert timer.ongoing()
    assert timer.get() != timer.get()

    timer.stop()
    assert not timer.ongoing()
    assert timer.get() > 0
    assert timer.get() == timer.get()
