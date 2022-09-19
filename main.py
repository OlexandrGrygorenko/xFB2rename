# -*- coding: utf-8 -*-
#from PyQt5 import QtWidgets # import PyQt5 widgets
from PyQt5 import QtCore, QtGui, QtWidgets

import sys


'''
import re
import os
import shutil
from xml.dom import minidom

KEY_PATH_SOURCE = '/storage/local/book/done_book'
KEY_PATH_DESTINATION = ''

# формат
fmt = '{0} {1} - {2}.fb2'

# аргументы
args = [
    ['title-info', 'author', 'first-name'],
    ['title-info', 'author', 'last-name'],
    ['title-info', 'book-title'],
]

def getFirst(node, key):
    lst = node.getElementsByTagName(key)
    return lst[0] if lst else None

def solveArg(node, args):
    path = []
    for arg in args:
        path.append(arg)
        node = getFirst(node, arg)
        assert node, "Can't find node '{0}'".format('/'.join(path))
    return node.firstChild.data


def parse(fname, fmt, args):
    root = minidom.parse(fname)
    assert root, "Can't open file '{0}'".format(fname)
    args = [solveArg(root, a) for a in args]
    fname = fmt.format(*args)
    print(fname)

    return fname


for dname, dnames, fnames in os.walk(KEY_PATH_SOURCE):
    for fname in fnames:
        if fname[-4:].lower() == '.fb2':
            try:
                fname_src = os.path.join(dname, fname)
                fname_dst = parse(fname_src, fmt, args)
                #dst = dname_dst + dname[len(dname_src):]
                #dst = os.path.join(dst, fname_dst)
                #modifyFile(fname_src, dst)
            except Exception as e:
                print('{0}: {1}'.format(fname_src, e))


#####################################################################################3
<description>
 <title-info>
  <genre>history_russia</genre>
  <author>
   <first-name>Лев</first-name>
   <middle-name>Николаевич</middle-name>
   <last-name>Толстой</last-name>
  </author>
  <book-title>Война и мир</book-title>
  <lang>ru</lang>
 </title-info>
 <document-info>
  <author>
   <nickname>GribUser</nickname>
  </author>
 <date value="2002-10-15">15 ноября 2002г., 19:53</date>
 <id>GribUser_WarAndWorld_D49FHSH8l0HS5</id>
 <version>2.0</version>
 </document-info>
</description>
'''

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("main_.ui", self)
        self.pshBttnQuit.clicked.connect(QtWidgets.qApp.quit)
        #self.pshBttnReadPath.clicked.connect()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())