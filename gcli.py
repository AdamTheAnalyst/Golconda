#!/usr/bin/python
import sys
from golconda import GolcondaApp


if __name__ == "__main__":
    app = GolcondaApp()
    sys.exit(app.run(sys.argv[1:]))