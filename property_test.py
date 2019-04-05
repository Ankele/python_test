class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        # some check
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        # some check
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print 'resolutioin = ', s.resolution
    if s.resolution == 786432:
        print 'Ok...'
    else:
        print 'Fai_x'
