from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar,
    QGridLayout,
    QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Inventory Management Software")
        self.setCentralWidget(QLabel("Welcome, Tester"))
        self.setGeometry(100, 100, 500, 500)
        self._createMenu()
        self._createToolbar()
        self._createStatusBar()

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolbar(self):
        pass

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("All systems are nonexistant")
        self.setStatusBar(status)
