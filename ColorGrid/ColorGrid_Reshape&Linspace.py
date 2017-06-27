import numpy as np
import cv2
import time

# tpc = top left color. Format (R, G, B)
# trc = top right color. Format (R, G, B)
# blc = bottom left color. Format (R, G, B)
# brc = bottom right color. Format (R, G, B)
def makeColorGrid(tpc, trc, blc, brc, n_lines, n_columns, window_width=500, window_height=650):
    start_time = time.time()
    TILE_WIDTH = window_width / n_columns
    TILE_HEIGHT = window_height / n_lines
    
    colors = np.empty((n_lines, n_columns, 3))
    c = np.linspace(0, 1, n_columns)
    
    # Red
    colors[:, 0, 2] = np.linspace(tpc[0], blc[0], n_lines)
    colors[:, -1, 2] = np.linspace(trc[0], brc[0], n_lines)

    # Green
    colors[:, 0, 1] = np.linspace(tpc[1], blc[1], n_lines)
    colors[:, -1, 1] = np.linspace(trc[1], brc[1], n_lines)

    # Blue
    colors[:, 0, 0] = np.linspace(tpc[2], blc[2], n_lines) 
    colors[:, -1, 0] = np.linspace(trc[2], brc[2], n_lines)

    a = colors[:, 0, :].reshape(-1, 1) # First column
    b = colors[:, -1, :].reshape(-1, 1) # Last column
    
    r = a + (b - a) * c
    colors[:, :, 0] = r[0::3]
    colors[:, :, 1] = r[1::3]
    colors[:, :, 2] = r[2::3]

    colors = colors.astype(np.uint8)

    # Creates the image with the colors
    image = colors.repeat(TILE_HEIGHT, axis=0).repeat(TILE_WIDTH, axis=1)

    print((time.time() - start_time)*1000)

    cv2.imshow('Color grid', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# MAIN
if __name__ == '__main__':
    makeColorGrid((0,0,0), (240,240,240),(120,120,120),(0,0,0), 5, 10)
    #makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 5, 5)
    #makeColorGrid((232, 149, 139), (48, 113, 181), (218, 239, 125), (0, 205, 217), 100, 100)

