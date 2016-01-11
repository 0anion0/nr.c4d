# -*- coding: utf8; -*-
''' Fake of the C4D package. '''

FILESELECTTYPE_ANYTHING = 0
FILESELECT_LOAD = 0

class Matrix(object):
  def __init__(self):
    pass
  def __repr__(self):
    return '<c4d.Matrix (unit)>'
  pass

from . import utils, gui
