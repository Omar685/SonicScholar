from src.MainWindow import SonicScholar
from PyQt5.QtWidgets import QApplication
import sys

def run():
  app = QApplication(sys.argv)
  window = SonicScholar()
  window.show()
  sys.exit(app.exec_())