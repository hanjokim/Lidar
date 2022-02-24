# -*- coding: utf-8 -*-
"""
From main library's example, Step01_BasicDots.py,
I will take out one of chart to make it for Lidar data display.

https://wise-self.tistory.com/75?category=1044077
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from collections import namedtuple
from itertools import chain

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(530,500)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('Lidar Test')

## create four areas to add plots
w1 = view.addPlot()

# Add polar grid lines
w1.addLine(x=0, pen=0.3)
w1.addLine(y=0, pen=0.3)
for r in range(2, 2000, 200):   # Draw 10 circles
   # Adding circle (x, y, width, height)
   cwidth = r * 2
   cheight = r * 2
   circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, cwidth, cheight)
   circle.setPen(pg.mkPen(0.3))
   w1.addItem(circle)

###### 이제 여기 아래만 집중적으로 공략하면 라이다 데이타를 적을수 있게 될 듯 하다.  #######
n = 360
s1 = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
# Make 2 Dimension (X,Y) points array of 360 dots on scale of 500 for 500 mm.
pos = np.random.normal(size=(2,n), scale=500)
spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
s1.addPoints(spots)
w1.addItem(s1)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()