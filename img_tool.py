import numpy as np
import cv2

#竖直切割图片
def v_cut(img):
    start = -1
    end = -1
    w = img.shape[1]
    h = img.shape[0]
    for i in range(w):
        if np.sum(img[:, i]) < 255 * h:
            start = i
            break
    for i in range(img.shape[1]):
        if np.sum(img[:, w - 1 - i]) < 255 * h:
            end = w - i
            break
    return img[:,start:end]

#水平切割图片
def h_cut(img):
    t1 = -1
    t2 = -1
    t3 = -1
    t4 = -1
    w = img.shape[1]
    for i in range(img.shape[0]):
        if np.sum(img[i, :]) >= w * 255:
            if t1 != -1 and t2 == -1:
                t2 = i
            elif t3 != -1 and t4 == -1:
                t4 = i
        else:
            if t1 == -1:
                t1 = i
            elif t2 != -1 and t3 == -1:
                t3 = i
    return img[t1:t2, :],img[t3:t4, :]