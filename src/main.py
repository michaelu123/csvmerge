import sys
from gui import Gui
from task import CsvTask
from utils import log


def main():
    gui = Gui(CsvTask())
    gui.startGui()
    sys.exit(0)


if __name__ == '__main__':
    main()
