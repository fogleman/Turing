import random
from ctypes import *

dll = CDLL('turing')

class Model(Structure):
    _fields_ = [
        ('width', c_int),
        ('height', c_int),
        ('states', c_int),
        ('symbols', c_int),
        ('position', c_int),
        ('state', c_int),
        ('table', POINTER(c_int)),
        ('tape', POINTER(c_int)),
    ]

def create_model(width, height, states, symbols):
    table_size = states * symbols * 3
    tape_size = width * height
    model = Model()
    model.width = width
    model.height = height
    model.states = states
    model.symbols = symbols
    model.position = (height / 2) * width + (width / 2)
    model.state = 0
    model.table = (c_int * table_size)()
    model.tape = (c_int * tape_size)()
    for i in xrange(0, table_size, 3):
        model.table[i + 0] = random.randint(0, symbols - 1)
        model.table[i + 1] = random.randint(0, states - 1)
        model.table[i + 2] = random.randint(1, 4)
    return model

def create_palette(colors):
    result = (c_uint * len(colors))()
    for i, (r, g, b) in enumerate(colors):
        result[i] = 255 << 24 | b << 16 | g << 8 | r
    return result

def update(model):
    dll.update(byref(model))

def updates(model, count):
    dll.updates(byref(model), count)

def create_image(model, palette):
    size = model.width * model.height
    result = (c_uint * size)()
    dll.create_image(byref(model), byref(palette), byref(result))
    return result
