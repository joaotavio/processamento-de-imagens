import numpy as np
import cv2
from random import randint

def getColorGrid(color, n_lines, n_columns, proportion):
	grid = np.empty((n_lines, n_columns, 3), np.float64)
	grid[:, :, 0] = proportion * color[2] # blue
	grid[:, :, 1] = proportion * color[1] # green
	grid[:, :, 2] = proportion * color[0] # red
	return grid

# c1 = top left color. Format (R, G, B)
# c2 = top right color. Format (R, G, B)
# c3 = bottom left color. Format (R, G, B)
# c4 = bottom right color. Format (R, G, B)
def makeColorGrid(c1, c2, c3, c4, n_lines, n_columns, window_width=500, window_height=650):
	TILE_WIDTH = window_width / n_columns
	TILE_HEIGHT = window_height / n_lines

	x = np.linspace(255, 0, n_lines)
	y = np.linspace(255, 0, n_columns)
	xv, yv = np.meshgrid(x, y)
	proportionGrid = (xv * yv) / (255*255)

	topleft = getColorGrid(c1, n_lines, n_columns, proportionGrid)

	proportionGrid = np.rot90(proportionGrid);

	bottomleft = getColorGrid(c3, n_lines, n_columns, proportionGrid)

	proportionGrid = np.rot90(proportionGrid);

	bottomright = getColorGrid(c4, n_lines, n_columns, proportionGrid)

	proportionGrid = np.rot90(proportionGrid);

	topright = getColorGrid(c2, n_lines, n_columns, proportionGrid)

	colors = topleft + topright + bottomleft + bottomright

	# OpenCV uses the 0 to 1 range for RGB color
	colors = colors / 255.0

	# Creates the image with the colors
	image = colors.repeat(TILE_HEIGHT, axis=0).repeat(TILE_WIDTH, axis=1)
	
	cv2.imshow('Color grid', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	

def randomColor():
	return (randint(0, 255), randint(0, 255), randint(0, 255))

# MAIN
if __name__ == '__main__':
	#makeColorGrid((0,0,0), (255,255,255),(0,255,0),(0,0,255), 70, 70)
	makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 5, 5)
	#makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 100, 100)
	#makeColorGrid(randomColor(), randomColor(), randomColor(), randomColor(), 10, 10);


