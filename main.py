import cv2
import numpy as np
import ml
import pickle

with open('lr1.pickle', 'rb') as f:
    lr1 = pickle.load(f)
with open('lr2.pickle', 'rb') as f:
    lr2 = pickle.load(f)
with open('lr3.pickle', 'rb') as f:
    lr3 = pickle.load(f)

#获取自己手中的牌
def get_my_pokes(img):
    img = img[284:391, :]
    res = []

    ret, thresh1 = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)
    ret2, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    resL = []
    h = img.shape[0]
    for i in range(img.shape[1]):
        if np.sum(thresh1[:, i]) > 0.55 * 255 * h:
            resL.append(i)

    if len(resL) == 1:
        w = int(img.shape[1] * 0.043)
    else:
        w = resL[1] - resL[0]

    for index in range(len(resL)):
        if index == len(resL) - 1:
            img = thresh2[:int(h * 0.5), resL[index]:resL[index] + w]
        else:
            img = thresh2[:int(h * 0.5), resL[index]:resL[index + 1]]
        res1 = ml.prdect1(lr1, img)
        if res1 == '0':
            res.append('ghost')
        else:
            w = img.shape[1]
            t1 = -1
            t2 = -1
            t3 = -1
            t4 = -1
            for i in range(img.shape[0]):
                if np.sum(img[i, :]) >= (w - 1) * 255:
                    if t1 != -1 and t2 == -1:
                        t2 = i
                    elif t3 != -1 and t4 == -1:
                        t4 = i
                else:
                    if t1 == -1:
                        t1 = i
                    elif t2 != -1 and t3 == -1:
                        t3 = i
            res2 = ml.prdect3(lr3, img[t1:t2, :])
            res3 = ml.prdect2(lr2, img[t3:t4, :])
            if res3 == '0':
                res3 = 'S'
            elif res3 == '1':
                res3 = 'R'
            elif res3 == '2':
                res3 = 'P'
            else:
                res3 = 'B'
            res.append(res3 + res2)
    return  res
