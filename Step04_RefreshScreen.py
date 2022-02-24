# -*- coding: utf-8 -*-
"""
From main library's example, ScatterPlot.py,
I will take out one of chart to make it for Lidar data display.

https://wise-self.tistory.com/77?category=1044077
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from collections import namedtuple
from itertools import chain
import sys

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(530, 500)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('Lidar Test, unit in mm')

## create areas to add plots
w1 = view.addPlot()


###### Refresh Screen
def RefreshScreen():
    # Add polar grid lines
    w1.clear()  # clear screen and start drawing basic lines
    w1.addLine(x=0, pen=0.3)  # draw vertical center line
    w1.addLine(y=0, pen=0.3)  # draw horizontal center line
    for radius in range(200, 2000, 200):  # Draw 9 circles 200 ~ 2000 step 200
        # Adding circle (x, y, width, height)
        circleWidth = radius * 2
        circleHeight = radius * 2
        circle = pg.QtGui.QGraphicsEllipseItem(-radius, -radius, circleWidth, circleHeight)
        circle.setPen(pg.mkPen(0.3))
        w1.addItem(circle)  # addItem means draw or plot.  Here, draw circle


######  I have to focus on putting data here.
def _update():
    RefreshScreen()  # Draw basic graph with no data dots

    n = 360

    s1 = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
    # Make 2 Dimension (X,Y) points array of 360 dots on scale of 500 for 500 mm.
    pos = np.random.normal(size=(2, n), scale=500)
    spots = [{'pos': pos[:, i], 'data': 1} for i in range(n)] + [{'pos': [0, 0], 'data': 1}]
    s1.addPoints(spots)
    # addItem means draw or plot.  Here, plot all points
    w1.addItem(s1, ignoreBounds=True)  # ignoreBounds will prevent annoying rescaling


timer = QtCore.QTimer(interval=1)
timer.timeout.connect(_update)
timer.start(500)  # duration number in millisecond

# RefreshScreen()  # Calling once, later it will be called from _update every 360 degree
_update()  # Calling only once, timer will keep calling them

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()