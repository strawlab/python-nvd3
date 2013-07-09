#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import lineChart
import math
from numpy import sin,pi,linspace

output_file = open('test_lineChartXY.html', 'w')

chart = lineChart(date=False,
                  x_axis_format=".1f",y_axis_format=".1f",
                  width=500, height=500,
                  show_legend=False)


#hacky? way to change the line color on mouse-over. should really be supported in nvd3
#natively
#https://github.com/novus/nvd3/issues/182
chart.chart_post_js.append(r"""
chart.lines.dispatch.on('elementMouseover.recolor', function(e){
    d3.select(chart.container).select('g.nv-group.nv-series-' + e.seriesIndex).select('path.nv-line').style('stroke','red')
  })

chart.lines.dispatch.on('elementMouseout.recolor', function(e){
    d3.select(chart.container).select('g.nv-group.nv-series-' + e.seriesIndex).select('path.nv-line').style('stroke','')
  })
""")

#lissajous parameters of a/b
a = [1,3,5,3]
b = [1,5,7,4]
delta = pi/2
t = linspace(-pi,pi,300)

for i in range(0,4):
    x = sin(a[i] * t + delta)
    y = sin(b[i] * t)
    
    chart.add_serie(y=y, x=x, name='lissajous-n%d' % i,  color='black')

chart.buildhtml()

output_file.write(chart.htmlcontent)

output_file.close()
