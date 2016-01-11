# -*- coding: utf8; -*-
''' Fake of the C4D package. '''

class _unconst(object):
  def __init__(self):
    raise RuntimeError('objects of fake "c4d" must not be constructed')

FILESELECTTYPE_ANYTHING = 0
FILESELECT_LOAD = 0

class Matrix(_unconst):
  pass

class Vector(_unconst):
  pass

from . import gui
