import numpy as np
import cv2


# Retorna as 3 bandas em uma tupla da forma (Y, Cr, Cb)
def chroma_subsampling(image, type):
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)

    Y = ycrcb[:, :, 0]
    Cr = ycrcb[:, :, 1]
    Cb = ycrcb[:, :, 2]

    if (type == "4:2:2"):
        return (Y, h_downsample(Cr, 2), h_downsample(Cb, 2))
    elif (type == "4:1:1"):
        return (Y, h_downsample(Cr, 4), h_downsample(Cb, 4))
    elif (type == "4:4:0"):
        return (Y, v_downsample(Cr, 2), v_downsample(Cb, 2))
    elif (type == "4:2:0"):
        return (Y, h_downsample(v_downsample(Cr, 2), 2), h_downsample(v_downsample(Cb, 2), 2))
    elif (type == "4:1:0"):
        return (Y, h_downsample(v_downsample(Cr, 2), 4), h_downsample(v_downsample(Cb, 2), 4))
    elif (type == "4:2:1"):
        return (Y, h_downsample(Cr, 2), h_downsample(Cb, 4))
    
    return None


def upsampling(channels, type):
    Y, Cr, Cb = channels
    if (type == "4:2:2"):
        return (Y, h_upsample(Cr, 2), h_upsample(Cb, 2))
    elif (type == "4:1:1"):
        return (Y, h_upsample(Cr, 4), h_upsample(Cb, 4))
    elif (type == "4:4:0"):
        return (Y, v_upsample(Cr, 2), v_upsample(Cb, 2))
    elif (type == "4:2:0"):
        return (Y, h_upsample(v_upsample(Cr, 2), 2), h_upsample(v_upsample(Cb, 2), 2))
    elif (type == "4:1:0"):
        return (Y, h_upsample(v_upsample(Cr, 2), 4), h_upsample(v_upsample(Cb, 2), 4))
    elif (type == "4:2:1"):
        return (Y, h_upsample(Cr, 2), h_upsample(Cb, 4))


def h_downsample(image_channel, n):
    return image_channel[:, ::n]

def v_downsample(image_channel, n):
    return image_channel[::n, :]

def h_upsample(image_channel, n):
    return np.repeat(image_channel, n, axis=1) 

def v_upsample(image_channel, n):
    return np.repeat(image_channel, n, axis=0)



def show_images(channels, type):
    Y, Cr, Cb = channels

    lin, col = Y.shape
    channels_img = np.zeros((lin, col + Cr.shape[1] + Cb.shape[1]), np.uint8)
    channels_img[:, :col] = Y
    channels_img[:Cr.shape[0], col:col+Cr.shape[1]] = Cr
    channels_img[:Cb.shape[0], col+Cr.shape[1]:] = Cb
    

    cv2.imshow('YCrCb subsampled channels - ' + type, channels_img)

    ups_channels = upsampling(channels, type)

    img = np.dstack(ups_channels)
    img = cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)

    cv2.imshow('Chroma subsampling - ' + type, img)

    #cv2.imwrite("chromasample.png", img)



# MAIN
if __name__ == '__main__':

    image = cv2.imread('lenna.png', cv2.IMREAD_COLOR)

    # Tipos disponíveis:
    # "4:2:2"
    # "4:1:1"
    # "4:4:0"
    # "4:2:0"
    # "4:1:0"
    # "4:2:1"
    type = input("Digite o tipo do chroma subsampling (J:a:b) > ")

    channels = chroma_subsampling(image, type)

    if (channels != None):
        cv2.imshow('Original', image)
        show_images(channels, type)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Tipo não suportado.")
    


