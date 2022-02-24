# -*- coding: utf-8 -*-
"""
From main library's example, Step01_BasicDots.py,
I will take out one of chart to make it for Lidar data display.

https://wise-self.tistory.com/74?category=1044077
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from collections import namedtuple
from itertools import chain

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(500,800)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('Lidar Test')

## create four areas to add plots
w1 = view.addPlot()
view.nextRow()
w4 = view.addPlot()
print("Generating data, this takes a few seconds...")

## There are a few different ways we can draw scatter plots; each is optimized for different types of data:

## 1) All spots identical and transform-invariant (top-left plot).
## In this case we can get a huge performance boost by pre-rendering the spot
## image and just drawing that image repeatedly.

n = 360
s1 = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
pos = np.random.normal(size=(2,n), scale=1e-5)
spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
s1.addPoints(spots)
w1.addItem(s1)

## Test performance of large scatterplots

s4 = pg.ScatterPlotItem(
    size=10,
    pen=pg.mkPen(None),
    brush=pg.mkBrush(255, 255, 255, 20),
    hoverable=True,
    hoverSymbol='s',
    hoverSize=15,
    hoverPen=pg.mkPen('r', width=2),
    hoverBrush=pg.mkBrush('g'),
)
n = 10000
pos = np.random.normal(size=(2, n), scale=1e-9)
s4.addPoints(
    x=pos[0],
    y=pos[1],
    #size=(np.random.random(n) * 20.).astype(int),
    #brush=[pg.mkBrush(x) for x in np.random.randint(0, 256, (n, 3))],
    data=np.arange(n)
)
w4.addItem(s4)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()