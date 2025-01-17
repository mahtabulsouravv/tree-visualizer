import sys
from PyQt5.QtWidgets import QApplication
from Backend.Action import TreeVisualization 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeVisualization()
    window.show()
    sys.exit(app.exec_())