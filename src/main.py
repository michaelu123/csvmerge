import argparse
import sys
from gui import Gui
from task import CsvTask
from utils import log


def main():
    if len(sys.argv) == 1:
        gui = Gui(CsvTask())
        gui.startGui()
        sys.exit(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--execute", action="store_true",
                        dest="doIt", default=False)
    args = parser.parse_args()
    print("parser.doIt", args.doIt)

    logName = "csvmerge"
    aksync = None
    msgs = "???"
    if args.doIt:
        log(logName, msgs)
    print(msgs)


if __name__ == '__main__':
    main()
