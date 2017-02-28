#!/usr/bin/python3

"""
Module to replace default print function
# TODO config pour le client http
# TODO booster le client http et le scinder
"""


import sys
import io
import threading
import time


class Printer:
    """
    class to provide timed print function
    """
    def __init__(self, file=sys.stdout, date="%Y%m%d %H%M%S - "):
        """
        @param file default output file
        @param date date format according to module time documentation
        """
        self.semaphore = threading.Semaphore(1)
        self.initial = __builtins__.print
        self.file = file
        self.date = date
        __builtins__.print = self

    def __call__(
            self, value, *args, sep=' ',
            end='\n', file=None, flush=False):
        """
        @param value first argument to be written
        @param *args other arguments to be writen
        @param sep arguments string separator
        @param end string to be writen to the end
        @param file output file
        @param flush indicator to flush
        """
        if file is None:
            file = self.file
        self.semaphore.acquire()
        try:
            if self.date is not None:
                file.write(time.strftime(self.date, time.gmtime(time.time())))
            file.write(str(value))
            for arg in args:
                file.write(sep)
                file.write(str(arg))
            file.write(end)
            if flush:
                file.flush()
        finally:
            self.semaphore.release()

    def close(self, close_all=True):
        """
        @param close_all indicator to close embedded output
        """
        __builtins__.print = self.initial
        if close_all:
            self.file.close()

    def flush(self):
        """
        flush default output
        """
        self.file.flush()


class StringBuffer:
    """
    String file to be used as sys.stdout or sys.stderr
    """
    def __init__(self):
        """
        Constructor
        """
        self.obj = io.StringIO()

    def write(self, st):
        """
        @param st string to be writen
        """
        self.obj.write(st)

    def get(self):
        """
        @return read text value
        """
        return self.obj.getvalue()

    def reset(self):
        """
        Discard the read string
        @return previous read value
        """
        ret = self.obj.getvalue()
        self.obj = io.StringIO()
        return ret


if __name__ == "__main__":
    buffer = StringBuffer()
    Printer()

    print(
        "mon texte", "en", 2, "parties", None, ":",
        True, [3, (4, 5)], file=buffer)

    print.initial(buffer.reset())

    print("nouvelle chaine", file=buffer)
    print.initial("+++", buffer.get())
