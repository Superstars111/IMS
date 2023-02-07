from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QStatusBar,
    QToolBar,
    QGridLayout,
    QVBoxLayout,
    QPushButton
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
        self.setGeometry(100, 100, 500, 500)
        self.resize(100, 100)
        self._createMenu()
        self._createToolbar()
        self._createStatusBar()
        self._createDisplay()
        self._createButtons()

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolbar(self):
        pass

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("All systems are nonexistent")
        self.setStatusBar(status)

    def _createDisplay(self):
        pass

    def _createButtons(self):
        pass
