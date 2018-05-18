import cv2
import numpy as np
import ml
import pickle
import img_tool as itool

with open('lr1.pickle', 'rb') as f:
    lr1 = pickle.load(f)
with open('lr2.pickle', 'rb') as f:
    lr2 = pickle.load(f)
with open('lr3.pickle', 'rb') as f:
    lr3 = pickle.load(f)
with open('lr4.pickle', 'rb') as f:
    lr4 = pickle.load(f)
with open('lr5.pickle', 'rb') as f:
    lr5 = pickle.load(f)
with open('lr6.pickle', 'rb') as f:
    lr6 = pickle.load(f)

#获取自己手中的牌
def get_my_pokers(img):
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
        res1 = ml.prdect(lr1, img, 1)
        if res1 == '0':
            res.append('ghost')
        else:
            top_img, bottom_img = itool.h_cut(img)
            res2 = ml.prdect(lr3, itool.v_cut(top_img), 3)
            res3 = ml.prdect(lr2, itool.v_cut(bottom_img), 2)
            if res3 == '0':
                res3 = 'S'
            elif res3 == '1':
                res3 = 'R'
            elif res3 == '2':
                res3 = 'P'
            else:
                res3 = 'B'
            res.append(res3 + res2)
    return res

#获取他人打出的牌
def get_others_pokers(img):
    img = img[129:187, :]
    res = []
    ret, thresh1 = cv2.threshold(img, 242, 255, cv2.THRESH_BINARY)
    ret2, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    resL = []
    h = img.shape[0]
    for i in range(img.shape[1]):
        if np.sum(thresh1[:, i]) > 0.5 * 255 * h:
            if len(resL) != 0:
                if (i - resL[-1]) > 2:
                    resL.append(i)

            else:
                resL.append(i)
    w = int(img.shape[1] * 0.0286)
    for index in range(len(resL)):
        if index == len(resL) - 1:
            img = thresh2[:int(h * 0.7), resL[index]:resL[index] + w]
        else:
            if resL[index + 1] - resL[index] < int(img.shape[1] * 0.03):
                img = thresh2[:int(h * 0.7), resL[index]:resL[index + 1]]
            else:
                img = thresh2[:int(h * 0.7), resL[index]:resL[index] + w]

        res1 = ml.prdect(lr4, img, 4)
        if res1 == '0':
            res.append('ghost')
        else:
            top_img, bottom_img = itool.h_cut(img)
            res2 = ml.prdect(lr6, itool.v_cut(top_img), 6)
            res3 = ml.prdect(lr5, itool.v_cut(bottom_img), 5)
            if res3 == '0':
                res3 = 'S'
            elif res3 == '1':
                res3 = 'R'
            elif res3 == '2':
                res3 = 'P'
            else:
                res3 = 'B'
            res.append(res3 + res2)
    return res
