import numpy as np
import cv2
import time

# c1 = top left color. Format (R, G, B)
# c2 = top right color. Format (R, G, B)
# c3 = bottom left color. Format (R, G, B)
# c4 = bottom right color. Format (R, G, B)
def makeColorGrid(cae, cad, cbe, cbd, n_lines, n_columns, window_width=500, window_height=650):
    start_time = time.time()
    TILE_WIDTH = window_width / n_columns
    TILE_HEIGHT = window_height / n_lines
    
    colors = np.zeros((n_lines, n_columns, 3))
    c = np.linspace(0, 1, n_columns)
    
    #red
    colors[:, 0, 2] = np.linspace(cae[0], cbe[0], n_lines)
    colors[:, -1, 2] = np.linspace(cad[0], cbd[0], n_lines)

    #green
    colors[:, 0, 1] = np.linspace(cae[1], cbe[1], n_lines)
    colors[:, -1, 1] = np.linspace(cad[1], cbd[1], n_lines)

    #blue
    colors[:, 0, 0] = np.linspace(cae[2], cbe[2], n_lines) 
    colors[:, -1, 0] = np.linspace(cad[2], cbd[2], n_lines)

    a = colors[:, 0, :].reshape(-1, 1)
    b = colors[:, -1, :].reshape(-1, 1)
    
    r = a + (b - a) * c
    colors[:, :, 0] = r[0::3]
    colors[:, :, 1] = r[1::3]
    colors[:, :, 2] = r[2::3]   
           
    # OpenCV uses the 0 to 1 range for RGB color
    colors = colors / 255.0
    # Creates the image with the colors
    image = colors.repeat(TILE_HEIGHT, axis=0).repeat(TILE_WIDTH, axis=1)
    print((time.time() - start_time)*1000)
    cv2.imshow('Color grid', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# MAIN
if __name__ == '__main__':
	makeColorGrid((0,0,0), (240,240,240),(120,120,120),(0,0,0), 5, 4)
	#makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 5, 5)
	#makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 100, 100)

