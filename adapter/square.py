class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


def draw_point(p):
    print('.', end='')


# ^^ you are given this

# vv you are working with this
class Line:
    def __init__(self, start, end):
        self.end = end
        self.start = start


class Rectangle(list):
    """ Represented as a list of lines. """

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:
    count = 0
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()
        self.count += 1
        print(f'{self.count}: Generating points for line ' +
              f'[{line.start.x},{line.start.y}]→[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])

######

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side