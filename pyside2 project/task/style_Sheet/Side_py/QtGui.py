# -*- coding: utf-8 -*-
#
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtGui classes and functions.
.. warning:: Only PyQt4/PySide QtGui classes compatible with PyQt5.QtGui are
    exposed here. Therefore, you need to treat/use this package as if it were
    the ``PyQt5.QtGui`` module.
"""
import warnings

from . import PYSIDE2, PythonQtError


if PYSIDE2:
    from PySide2.QtGui import *
else:
    raise PythonQtError('No Qt bindings could be found')
