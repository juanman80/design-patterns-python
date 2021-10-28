# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
from abc import ABC

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

class VectorRenderer(Renderer):
    def __init__(self):
        super().__init__()

    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    def __init__(self):
        super().__init__()

    @property
    def what_to_render_as(self):
        return 'pixels'


class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer

    def __str__(self):
        return 'Drawing %s as %s'%(self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'