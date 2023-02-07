import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from windows import IMSWindow
from controllers import IMS


if __name__ == "__main__":
    ims_app = QApplication([])
    imsWindow = IMSWindow()
    imsWindow.show()
    IMS(model=None, view=imsWindow)
    sys.exit(ims_app.exec())
