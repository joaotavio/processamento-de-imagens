import numpy as np
import cv2

#c1 = color top left
#c2 = color top right
#c3 = color bottom left
#c4 = color bottom right 
def makeColorGrid(c1, c2, c3, c4, gridSize, window_width=500, window_height=650):
	TILE_WIDTH = window_width / gridSize
	TILE_HEIGHT = window_height / gridSize

	colors = np.zeros((gridSize, gridSize, 3))
	
	# TOP
	colors[0, 0:gridSize, 2] = np.linspace(c1[0], c2[0], gridSize) # RED
	colors[0, 0:gridSize, 1] = np.linspace(c1[1], c2[1], gridSize) # GREEN
	colors[0, 0:gridSize, 0] = np.linspace(c1[2], c2[2], gridSize) # BLUE

	# LEFT
	colors[0:gridSize, 0, 2] = np.linspace(c1[0], c3[0], gridSize) # RED
	colors[0:gridSize, 0, 1] = np.linspace(c1[1], c3[1], gridSize) # GREEN
	colors[0:gridSize, 0, 0] = np.linspace(c1[2], c3[2], gridSize) # BLUE

	# BOTTOM
	colors[gridSize - 1, 0:gridSize, 2] = np.linspace(c3[0], c4[0], gridSize) # RED
	colors[gridSize - 1, 0:gridSize, 1] = np.linspace(c3[1], c4[1], gridSize) # GREEN
	colors[gridSize - 1, 0:gridSize, 0] = np.linspace(c3[2], c4[2], gridSize) # BLUE

	# RIGHT
	colors[0:gridSize, gridSize - 1, 2] = np.linspace(c2[0], c4[0], gridSize) # RED
	colors[0:gridSize, gridSize - 1, 1] = np.linspace(c2[1], c4[1], gridSize) # GREEN
	colors[0:gridSize, gridSize - 1, 0] = np.linspace(c2[2], c4[2], gridSize) # BLUE

	for i in range(1, gridSize - 1):
		color1 = colors[i, 0]
		color2 = colors[i, gridSize - 1]
		
		colors[i, 0:gridSize, 2] = np.linspace(color1[2], color2[2], gridSize) # RED
		colors[i, 0:gridSize, 1] = np.linspace(color1[1], color2[1], gridSize) # GREEN
		colors[i, 0:gridSize, 0] = np.linspace(color1[0], color2[0], gridSize) # BLUE


	#255 -   -   0
	#-   -   -   0
	#-   -   -   0
	#0   0   0   0

	
	colors = colors / 255.0

	image = colors.repeat(TILE_HEIGHT, axis=0).repeat(TILE_WIDTH, axis=1)


	cv2.imshow('Color grid', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# MAIN
if __name__ == '__main__':
	#makeColorGrid([0,0,0], [255,255,255],[0,255,0],[0,0,255], 70)
	makeColorGrid([232, 149, 139], [48, 113, 181],[218, 239, 125],[0, 205, 217], 5)
	makeColorGrid([232, 149, 139], [48, 113, 181],[218, 239, 125],[0, 205, 217], 50)

