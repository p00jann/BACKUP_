
"""
PySide2
======

Set the QT_API environment variable to 'pyside2' before importing other
packages::

    >>> import os
    >>> os.environ['QT_API'] = 'pyside2'
    >>> from qtpy import QtGui, QtWidgets, QtCore
    >>> print(QtWidgets.QWidget)

"""

from distutils.version import LooseVersion
import os
import platform
import sys
import warnings

# Version of QtPy
from ._version import __version__


class PythonQtError(RuntimeError):
    """Error raise if no bindings could be selected."""
    pass


class PythonQtWarning(Warning):
    """Warning if some features are not implemented in a binding."""
    pass


# Qt API environment variable name
QT_API = 'QT_API'



# Names of the expected PySide2 api
PYSIDE2_API = ['pyside2']

# Detecting if a binding was specified by the user
binding_specified = QT_API in os.environ

# Setting a default value for QT_API
os.environ.setdefault(QT_API, 'pyside2')

API = os.environ[QT_API].lower()
initial_api = API
assert API in (PYSIDE2_API)


PYSIDE2 = True

if os.environ.get('FORCE_QT_API') is not None:

    if 'PySide2' in sys.modules:
        API = initial_api if initial_api in PYSIDE2_API else 'pyside2'



if API in PYSIDE2_API:
    try:
        from PySide2 import __version__ as PYSIDE_VERSION  # analysis:ignore
        from PySide2.QtCore import __version__ as QT_VERSION  # analysis:ignore

        PYQT_VERSION = None
        PYQT5 = False
        PYSIDE2 = True

        if sys.platform == 'darwin':
            macos_version = LooseVersion(platform.mac_ver()[0])
            if macos_version < LooseVersion('10.11'):
                if LooseVersion(QT_VERSION) >= LooseVersion('5.11'):
                    raise PythonQtError("Qt 5.11 or higher only works in "
                                        "macOS 10.11 or higher. Your "
                                        "program will fail in this "
                                        "system.")

            del macos_version
    except ImportError:
        API = os.environ['QT_API'] = 'pyside2'


if API != initial_api and binding_specified:
    warnings.warn('Selected binding "{}" could not be found, '
                  'using "{}"'.format(initial_api, API), RuntimeWarning)

API_NAME = {'pyside': 'PySide', 'pyside2':'PySide2'}[API]

