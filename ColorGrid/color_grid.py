import numpy as np
import cv2

# c1 = top left color. Format (R, G, B)
# c2 = top right color. Format (R, G, B)
# c3 = bottom left color. Format (R, G, B)
# c4 = bottom right color. Format (R, G, B)
def makeColorGrid(c1, c2, c3, c4, n_lines, n_columns, window_width=500, window_height=650):
	TILE_WIDTH = window_width / n_columns
	TILE_HEIGHT = window_height / n_lines

	colors = np.zeros((n_lines, n_columns, 3))
	
	# LEFT
	colors[:, 0, 2] = np.linspace(c1[0], c3[0], n_lines) # RED
	colors[:, 0, 1] = np.linspace(c1[1], c3[1], n_lines) # GREEN
	colors[:, 0, 0] = np.linspace(c1[2], c3[2], n_lines) # BLUE

	# RIGHT
	colors[:, -1, 2] = np.linspace(c2[0], c4[0], n_lines) # RED
	colors[:, -1, 1] = np.linspace(c2[1], c4[1], n_lines) # GREEN
	colors[:, -1, 0] = np.linspace(c2[2], c4[2], n_lines) # BLUE

	for i in range(n_lines):
		color1 = colors[i, 0]
		color2 = colors[i, -1]
		
		colors[i, :, 2] = np.linspace(color1[2], color2[2], n_columns) # RED
		colors[i, :, 1] = np.linspace(color1[1], color2[1], n_columns) # GREEN
		colors[i, :, 0] = np.linspace(color1[0], color2[0], n_columns) # BLUE


	# OpenCV uses the 0 to 1 range for RGB color
	colors = colors / 255.0

	# Creates the image with the colors
	image = colors.repeat(TILE_HEIGHT, axis=0).repeat(TILE_WIDTH, axis=1)

	cv2.imshow('Color grid', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# MAIN
if __name__ == '__main__':
	#makeColorGrid((0,0,0), (255,255,255),(0,255,0),(0,0,255), 70)
	makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 5, 5)
	makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 100, 100)

