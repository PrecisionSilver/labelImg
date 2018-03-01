#!/usr/bin/python
# -*- coding: utf-8 -*-

from libs.shape import *

class Tile(Shape):
	P_SQUARE, P_ROUND = range(2)

	MOVE_VERTEX, NEAR_VERTEX = range(2)

	# The following class variables influence the drawing
	# of _all_ shape objects.
	line_color = DEFAULT_LINE_COLOR
	fill_color = DEFAULT_FILL_COLOR
	select_line_color = DEFAULT_SELECT_LINE_COLOR
	select_fill_color = DEFAULT_SELECT_FILL_COLOR
	vertex_fill_color = DEFAULT_VERTEX_FILL_COLOR
	hvertex_fill_color = DEFAULT_HVERTEX_FILL_COLOR
	point_type = P_ROUND
	point_size = 8
	scale = 1.0

	def __init__(self):
		super(Tile, self).__init__(label='Tile')
		super(Tile, self).addPoint(QPointF(0.0, 0.0))
		super(Tile, self).addPoint(QPointF(290.0, 0.0))
		super(Tile, self).addPoint(QPointF(290.0, 290.0))
		super(Tile, self).addPoint(QPointF(0.0, 290.0))
		super(Tile, self).close()

		#print(self.points)

#tile = Tile()
