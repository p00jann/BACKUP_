import logging
import os
import platform
import traceback
import warnings

from style_Sheet.Sty_Sheet.palette import DarkPalette


__version__ = "2.8.1"


_logger = logging.getLogger(__name__)

REPO_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__))).split('style_Sheet')[0]
print(REPO_PATH)
EXAMPLE_PATH = os.path.join(REPO_PATH, "style_Sheet","Sty_Sheet",'example')
IMAGES_PATH = os.path.join(REPO_PATH, "style_Sheet","Sty_Sheet",'images')
PACKAGE_PATH = os.path.join(REPO_PATH, "style_Sheet","Sty_Sheet")

print(PACKAGE_PATH)

QSS_PATH = os.path.join(PACKAGE_PATH, 'qss')
RC_PATH = os.path.join(PACKAGE_PATH, 'rc')
print("sajkdhgajkshd",RC_PATH)
SVG_PATH = os.path.join(PACKAGE_PATH, 'svg')
print(QSS_PATH)


QSS_FILE = 'style.qss'
QRC_FILE = QSS_FILE.replace('.qss', '.qrc')
print("kjdfhoisjdgoidsfghjosdfijhgoisdchgjosdjf",QRC_FILE)

MAIN_SCSS_FILE = 'main.scss'
STYLES_SCSS_FILE = '_styles.scss'
VARIABLES_SCSS_FILE = '_variables.scss'

QSS_FILEPATH = os.path.join(PACKAGE_PATH, QSS_FILE)
print(QSS_FILEPATH)
QRC_FILEPATH = os.path.join(PACKAGE_PATH, QRC_FILE)

MAIN_SCSS_FILEPATH = os.path.join(QSS_PATH, MAIN_SCSS_FILE)
STYLES_SCSS_FILEPATH = os.path.join(QSS_PATH, STYLES_SCSS_FILE)
VARIABLES_SCSS_FILEPATH = os.path.join(QSS_PATH, VARIABLES_SCSS_FILE)

DEPRECATION_MSG = '''This function will be deprecated in v3.0.
Please, set the wanted binding by using QtPy environment variable QT_API,
then use load_stylesheet() or use load_stylesheet()
passing the argument qt_api='wanted_binding'.'''

def _apply_os_patches():
    """
    Apply OS-only specific stylesheet pacthes.

    Returns:
        str: stylesheet string (css).
    """
    os_fix = ""

    if platform.system().lower() == 'darwin':
        # See issue #12
        os_fix = '''
        QDockWidget::title
        {{
            background-color: {color};
            text-align: center;
            height: 12px;
        }}
        '''.format(color=DarkPalette.COLOR_BACKGROUND_NORMAL)

    # Only open the QSS file if any patch is needed
    if os_fix:
        _logger.info("Found OS patches to be applied.")

    return os_fix

def _apply_binding_patches():
    """
    Apply binding-only specific stylesheet patches for the same OS.

    Returns:
        str: stylesheet string (css).
    """
    binding_fix = ""

    if binding_fix:
        _logger.info("Found binding patches to be applied.")

    return binding_fix

def _apply_version_patches():
    """
    Apply version-only specific stylesheet patches for the same binding.

    Returns:
        str: stylesheet string (css).
    """
    version_fix = ""

    if version_fix:
        _logger.info("Found version patches to be applied.")

    return version_fix

def _apply_application_patches(QCoreApplication, QPalette, QColor):
    """
    Apply application level fixes on the QPalette.

    The import names args must be passed here because the import is done
    inside the load_stylesheet() function, as QtPy is only imported in
    that moment for setting reasons.
    """
    # See issue #139
    color = DarkPalette.COLOR_SELECTION_LIGHT
    qcolor = QColor(color)

    # Todo: check if it is qcoreapplication indeed
    app = QCoreApplication.instance()

    _logger.info("Found application patches to be applied.")

    if app:
        palette = app.palette()
        palette.setColor(QPalette.Normal, QPalette.Link, qcolor)
        app.setPalette(palette)
    else:
        _logger.warn("No QCoreApplication instance found. "
                     "Application patches not applied. "
                     "You have to call load_stylesheet function after "
                     "instantiation of QApplication to take effect. ")

def _load_stylesheet(qt_api=''):

    if qt_api:
        os.environ['QT_API'] = qt_api

    from style_Sheet.Side_py.QtCore import QCoreApplication, QFile, QTextStream
    from style_Sheet.Side_py.QtGui import QColor, QPalette
    from style_Sheet.Sty_Sheet import style_rc

    # Then we import resources - binary qrc content
    # from style_Sheet import style_rc
    print('dfhhfkjh',PACKAGE_PATH)
    # Thus, by importing the binary we can access the resources
    # package_dir = os.path.basename(PACKAGE_PATH)
    # print("saiudghaisugdiuashdiuasdh",package_dir)
    #
    # print("fnkghmikh",package_dir)

    qss_rc_path = ":" + os.path.join('style_Sheet\Sty_Sheet', QSS_FILE)
    print("qss_rc_path",qss_rc_path)

    _logger.debug("Reading QSS file in: %s" % qss_rc_path)

    # It gets the qss file from compiled style_rc that was import
    # not from the file QSS as we are using resources
    qss_file = QFile(qss_rc_path)
    print("dsfondnko",qss_file)

    if qss_file.exists():
        qss_file.open(QFile.ReadOnly | QFile.Text)
        text_stream = QTextStream(qss_file)
        stylesheet = text_stream.readAll()
        _logger.info("QSS file sucessfuly loaded.")
    else:
        stylesheet = ""
        # Todo: check this raise type and add to docs
        raise FileNotFoundError("Unable to find QSS file '{}' "
                                "in resources.".format(qss_rc_path))

    _logger.debug("Checking patches for being applied.")

    # Todo: check execution order for these functions
    # 1. Apply OS specific patches
    stylesheet += _apply_os_patches()

    # 2. Apply binding specific patches
    stylesheet += _apply_binding_patches()

    # 3. Apply binding version specific patches
    stylesheet += _apply_version_patches()

    # 4. Apply palette fix. See issue #139
    _apply_application_patches(QCoreApplication, QPalette, QColor)

    return stylesheet

def load_stylesheet_pyside2():
    try:
        return _load_stylesheet(qt_api='pyside2')
    except:
        print(traceback.print_exc())


load_stylesheet_pyside2()


