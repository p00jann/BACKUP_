# -*- coding: utf-8 -*-
#
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtCore classes and functions.
"""

from . import PYSIDE2, PythonQtError

if PYSIDE2:
    from PySide2.QtCore import *
    try:  # may be limited to PySide-5.11a1 only 
        from PySide2.QtGui import QStringListModel
    except:
        pass

    import PySide2.QtCore
    __version__ = PySide2.QtCore.__version__
else:
    raise PythonQtError('No Qt bindings could be found')
