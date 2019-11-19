#! Python3
# crev - add concrete report review to the clipboard

import sys
import pyperclip


cyls = sys.argv[1]
export = 'Concrete report review: ' + cyls
pyperclip.copy(export)