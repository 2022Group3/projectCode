from PyQt5 import QtWidgets # import PyQt5 widgets
import sys
def func():
    # Create the application object
    app = QtWidgets.QApplication(sys.argv)

    # Create the form object
    first_window = QtWidgets.QWidget()

    # Set window size
    first_window.resize(800, 800)

    # Set the form title
    first_window.setWindowTitle("The first pyqt program")

    # Show form
    first_window.show()

    # Run the program
    sys.exit(app.exec())
if __name__ == '__main__':
    func()