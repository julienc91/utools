# -*- coding: utf-8 -*-

""" Useful functions to work with dates and durations
"""

from datetime import datetime


class timer:
    """ Get the execution time of a block of code.

    Example:
        The easiest way to use the timer is inside a 'with' statement::

            >>> import time
            >>> t = timer()
            >>> with t:
            ...     time.sleep(1)
            >>> t.get()
            1.001263

        The timer class also provides methods to start and stop the timer when you want::

            >>> t = timer()
            >>> t.get()
            0.
            >>> t.start()
            >>> t.get()
            1.425219
            >>> t.stop()
            >>> t.get()
            2.636786
    """

    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, traceback):
        del exc_type, exc_value, traceback
        self.stop()

    def start(self):
        """ Start or restart the timer.
        """
        self.reset()
        self._start_time = datetime.now()

    def stop(self):
        """ Stop the timer.
        """
        if self.ongoing():
            self._stop_time = datetime.now()

    def reset(self):
        """ Reset the timer.
        """
        self._start_time = None
        self._stop_time = None

    def ongoing(self):
        """ Check if the timer is running.

        Returns: True if the timer is currently running, False otherwise
        """
        return self._start_time is not None and self._stop_time is None

    def get(self):
        """ Get the current timer value in seconds.

        Returns: the elapsed time in seconds since the timer started or until the timer was stopped
        """
        now = datetime.now()
        if self._start_time:
            if self._stop_time:
                return (self._stop_time - self._start_time).total_seconds()
            return (now - self._start_time).total_seconds()
        return 0.
