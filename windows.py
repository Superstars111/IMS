from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QStatusBar,
    QToolBar,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
)


class IMSWindow(QMainWindow):
    """IMS Main Window"""

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Inventory Management Software")  # TODO: Include JSON file for storing company name, etc.
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.setGeometry(10, 35, 1900, 1000)
        # self.resize(1900, 1000)
        self._createActions()
        self._createMenu()
        self._createToolbar()
        self._createStatusBar()

    def _createActions(self):
        self.newAction = QAction("&New", self)
        self.openAction = QAction("&Open", self)
        self.helpAction = QAction("&Help", self)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolbar(self):
        pass

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("All systems are nonexistent")
        self.setStatusBar(status)
