import cv2
import numpy as np
import pickle
import ml

with open('lr1.pickle', 'rb') as f:
    lr1 = pickle.load(f)
with open('lr2.pickle', 'rb') as f:
    lr2 = pickle.load(f)
with open('lr3.pickle', 'rb') as f:
    lr3 = pickle.load(f)
with open('lr6.pickle', 'rb') as f:
    lr6 = pickle.load(f)


img = cv2.imread('img2/imgScreenshot_20180518-014720.png', 0)
img = cv2.resize(img, (int(img.shape[1] * 0.4), int(img.shape[0] * 0.4)), interpolation=cv2.INTER_CUBIC)
img = img[129:187, :]

ret, thresh1 = cv2.threshold(img, 242, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

resL = []
h = img.shape[0]
for i in range(img.shape[1]):
    if np.sum(thresh1[:, i]) > 0.4 * 255 * h:
        if len(resL) != 0:
            if (i - resL[-1]) > 2:
                resL.append(i)

        else:
            resL.append(i)
print(resL)
w = int(img.shape[1] * 0.0286)
for index in range(len(resL)):
    if index == len(resL) - 1:
        img = thresh2[:int(h * 0.7), resL[index]:resL[index] + w]
    else:
        if resL[index + 1] - resL[index] < int(img.shape[1] * 0.03):
            img = thresh2[:int(h * 0.7), resL[index]:resL[index + 1]]
        else:
            img = thresh2[:int(h * 0.7), resL[index]:resL[index] + w]

    res1 = ml.prdect1(lr1, img)
    if res1 == '0':
        print('ghost', end=' ')
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
        res2 = ml.prdect6(lr6, img[t1:t2, :])
        res3 = ml.prdect2(lr2, img[t3:t4, :])
        if res3 == '0':
            res3 = 'S'
        elif res3 == '1':
            res3 = 'R'
        elif res3 == '2':
            res3 = 'P'
        else:
            res3 = 'B'
        print(res3 + res2, end=' ')
    cv2.imshow(str(index), img)
cv2.waitKey()

import os

# count = 9
# for f in os.listdir('img2'):
#     img = cv2.imread('img2/%s'%f, 0)
#     img = cv2.resize(img, (int(img.shape[1] * 0.4), int(img.shape[0] * 0.4)), interpolation=cv2.INTER_CUBIC)
#     img = img[129:187, :]
#
#     ret, thresh1 = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)
#     ret2, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
#
#     # cv2.imshow('s', thresh2)
#     # cv2.waitKey()
#
#     resL = []
#     h = img.shape[0]
#     for i in range(img.shape[1]):
#         if np.sum(thresh1[:, i]) > 0.55 * 255 * h:
#             resL.append(i)
#
#     w = int(img.shape[1] * 0.0286)
#
#
#     for index in range(len(resL)):
#         if index == len(resL) - 1:
#             img = thresh2[:int(h * 0.7), resL[index]:resL[index] + w]
#         else:
#             if resL[index + 1] - resL[index] < int(img.shape[1] * 0.03):
#                 img = thresh2[:int(h * 0.7), resL[index]:resL[index + 1]]
#             else:
#                 img = thresh2[:int(h * 0.7), resL[index]:resL[index] + w]
#         # cv2.imwrite('cut_img2/%d_%d.png' % (count, index), img)
#
#         res1 = ml.prdect1(lr1, img)
#         if res1 == '0':
#             print('ghost', end=' ')
#         else:
#             w = img.shape[1]
#             t1 = -1
#             t2 = -1
#             t3 = -1
#             t4 = -1
#             for i in range(img.shape[0]):
#                 if np.sum(img[i, :]) >= (w - 1) * 255:
#                     if t1 != -1 and t2 == -1:
#                         t2 = i
#                     elif t3 != -1 and t4 == -1:
#                         t4 = i
#                 else:
#                     if t1 == -1:
#                         t1 = i
#                     elif t2 != -1 and t3 == -1:
#                         t3 = i
#             res2 = ml.prdect3(lr3, img[t1:t2, :])
#             res3 = ml.prdect2(lr2, img[t3:t4, :])
#             if res3 == '0':
#                 res3 = 'S'
#             elif res3 == '1':
#                 res3 = 'R'
#             elif res3 == '2':
#                 res3 = 'P'
#             else:
#                 res3 = 'B'
#             print(res3 + res2, end=' ')
#
#
#     #count += 1
#     print(f)
#     print(resL)
# #
# #


#
#
#
#

# print(np.sum(thresh1, axis=0))

# import os
# for f in os.listdir('cut_img2'):
#     img = cv2.imread('cut_img2/%s'%f, 0)
#     w = img.shape[1]
#     t1 = -1
#     t2 = -1
#     t3 = -1
#     t4 = -1
#     for i in range(img.shape[0]):
#         if np.sum(img[i,:]) >= w * 255:
#             if t1 != -1 and t2 == -1:
#                 t2 = i
#             elif t3 != -1 and t4 == -1:
#                 t4 = i
#         else:
#             if t1 == -1:
#                 t1 = i
#             elif t2 != -1 and t3 == -1:
#                 t3 = i
#     cv2.imwrite('not_0_img/0_%s'%f, img[t1:t2,:])
#     cv2.imwrite('not_0_img/1_%s' % f, img[t3:t4, :])

