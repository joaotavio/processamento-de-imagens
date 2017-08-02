import numpy as np
import cv2

# returns a gradient from color 'c1' to color 'c2' with 'size' lines
def getGradient(c1, c2, size):
    a = np.empty((size, 3))
    a[:, 2] = np.linspace(c1[0], c2[0], size) # Red
    a[:, 1] = np.linspace(c1[1], c2[1], size) # Green
    a[:, 0] = np.linspace(c1[2], c2[2], size) # Blue
    return a

# tlc = top left color. Format (R, G, B)
# trc = top right color. Format (R, G, B)
# blc = bottom left color. Format (R, G, B)
# brc = bottom right color. Format (R, G, B)
def makeColorGrid(tlc, trc, blc, brc, n_lines, n_columns, window_width=500, window_height=650):
    TILE_WIDTH = window_width / n_columns
    TILE_HEIGHT = window_height / n_lines
    
    colors = np.empty((n_lines, n_columns, 3))

    weights = np.linspace(0, 1, n_columns)

    left = getGradient(tlc, blc, n_lines).reshape(-1, 1) # First column (left)
    right = getGradient(trc, brc, n_lines).reshape(-1, 1) # Last column (right)
    
    r = left + (right - left) * weights

    colors[:, :, 0] = r[0::3]
    colors[:, :, 1] = r[1::3]
    colors[:, :, 2] = r[2::3]

    colors = colors.astype(np.uint8)

    # Creates the image with the colors
    image = colors.repeat(TILE_HEIGHT, axis=0).repeat(TILE_WIDTH, axis=1)

    cv2.imshow('Color grid', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# MAIN
if __name__ == '__main__':
    #makeColorGrid((0,0,0), (240,240,240),(120,120,120),(0,0,0), 5, 10)
    makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 5, 5)
    #makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 100, 100)

