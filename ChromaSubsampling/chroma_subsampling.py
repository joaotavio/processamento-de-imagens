import numpy as np
import cv2

def chroma_subsampling(image, n):
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
    
    ycrcb[:,:,1] = horizontal_upsample(horizontal_downsample(ycrcb[:,:,1], n), n)
    ycrcb[:,:,2] = horizontal_upsample(horizontal_downsample(ycrcb[:,:,2], n), n)

    return cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR)
    

def downsample(image, n):
    return image[::n, ::n]

def horizontal_downsample(image, n):
    return image[:, ::n]

def upsample(image, n):
    return np.repeat(np.repeat(image, n, axis=0), n, axis=1)  

def horizontal_upsample(image, n):
    return np.repeat(image, n, axis=1) 



# MAIN
if __name__ == '__main__':

    image = cv2.imread('lenna.png', cv2.IMREAD_COLOR)

    img = chroma_subsampling(image, 16)

    #cv2.imwrite("chromasample.png", img)
    cv2.imshow('Original', image)
    cv2.imshow('Chroma subsampling', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


