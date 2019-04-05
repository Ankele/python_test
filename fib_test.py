#! -*- coding: utf-8 -*-
import sys

class Fib(object):
    def __init__(self, i_max=10):
        self.a, self.b = 0, 1
        self.max = i_max
    def __iter__(self):
        return self
    # PY2中使用next，PY3中使用__next__
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > self.max:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance(n, int):
            self._getitem(n)
        elif isinstance(n, slice):
            self._getitem_slice(n)
        else:
            raise Exception('no... fuck... you...')
    def _getitem(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a
    def _getitem_slice(self, n):
        L = []
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a + b
        print L

def main(argv):
    i_max = 1000
    if len(argv) > 1 and argv[1].isdigit():
        i_max = int(argv[1])
    #for n in Fib(i_max):
    #    print n
    Fib(10000)[:10]

if __name__ == '__main__':
    main(sys.argv)
