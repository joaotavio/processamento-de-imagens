import numpy as np
import cv2
from matplotlib import pyplot as plt
 
def otsu(image):
    nbins = 256
    hist, bins = np.histogram(image.flatten(), nbins, [0, nbins], density=True)
    
    w0 = 0
    sum0 = 0
    ut = np.dot(hist, np.arange(nbins))

    max_sigma = -1 # sigma = variance
    max_sigma_position = -1

    for t in range(1, nbins):
        w0 += hist[t-1]
        w1 = 1.0 - w0

        if (w0 == 0 or w1 == 0):
            continue

        sum0 += (t-1) * hist[t-1]
        u0 = sum0 / w0
        u1 = (ut - (w0 * u0)) / w1

        curr_sigma = w0 * w1 * ((u0 - u1)**2)
        if (curr_sigma > max_sigma):
            max_sigma = curr_sigma
            max_sigma_position = t

    return max_sigma_position


def otsu_hist_equalization(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v_channel = img[:, :, 2]

    threshold = otsu(v_channel)
    print("Threshold =", threshold)

    nbins = 256
    hist, bins = np.histogram(v_channel.flatten(), nbins, [0, nbins])

    hist_acc = hist.cumsum()
    hist_acc_threshold = hist_acc[:threshold]

    LUT = np.arange(256, dtype=np.uint8)
    x = (threshold - 1) / hist_acc_threshold[-1]
    LUT[:threshold] = x * hist_acc_threshold

    v_channel[:] = LUT[v_channel]

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    return img


# MAIN
if __name__ == '__main__':
    image = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

    if (image.shape[0] > 1000 or image.shape[1] > 1000):
       image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 

    equalized_img = otsu_hist_equalization(image)

    # PLOT HISTOGRAM
    # plt.hist(image.flatten(),256,[0,256], alpha=0.5, label='original', color='r')
    # plt.hist(equalized_img.flatten(), 256,[0,256], alpha=0.5, label='equalized')
    # plt.legend(loc='upper left')
    # plt.xlim([0,256])
    # plt.show()

    # cv2.imwrite("equalized.jpg", equalized_img)
    cv2.imshow('Original', image)
    cv2.imshow('Threshold', equalized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
