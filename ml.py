import os
import cv2
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression


def load_train_data():
    """加载训练数据"""
    res = []
    c = []
    for root,dir,file in os.walk('train6'):
        if len(file) != 0:
            _class = root.split(os.path.sep)[-1]
            for f in file:
                img = cv2.imread(os.path.join(root, f), 0)
                img = cv2.resize(img, (20,20),interpolation=cv2.INTER_CUBIC)
                res.append(np.array(img).reshape(1,-1).tolist()[0])
                c.append(_class)
    res = np.array(res)
    res[res == 255] = 1
    return res,c


def dumpModel():
    """保存模型到lr.pickle文件中"""
    train_data, train_target = load_train_data()
    l = LogisticRegression(class_weight='balanced')
    l.fit(train_data,train_target)
    #保存模型
    with open('lr6.pickle', 'wb') as fw:
        pickle.dump(l, fw)
        print('保存模型完毕')

# 预测是不是王，0代表是王，1代表不是
def prdect1(lr, img):
    img = cv2.resize(img, (50, 30), interpolation=cv2.INTER_CUBIC)
    img = np.array(img).reshape(1, -1)
    img[img == 255] = 1
    y_hat = lr.predict(img)[0]
    return y_hat

#预测花色，0，1，2，3分别代表黑红梅方
def prdect2(lr, img):
    img = cv2.resize(img, (25, 30), interpolation=cv2.INTER_CUBIC)
    img = np.array(img).reshape(1, -1)
    img[img == 255] = 1
    y_hat = lr.predict(img)[0]
    return y_hat

#预测牌面，1-13分别代表A，2，...，Q，K
def prdect3(lr, img):
    img = cv2.resize(img, (25, 30), interpolation=cv2.INTER_CUBIC)
    img = np.array(img).reshape(1, -1)
    img[img == 255] = 1
    y_hat = lr.predict(img)[0]
    return y_hat

def prdect6(lr, img):
    img = cv2.resize(img, (20, 20), interpolation=cv2.INTER_CUBIC)
    img = np.array(img).reshape(1, -1)
    img[img == 255] = 1
    y_hat = lr.predict(img)[0]
    return y_hat

dumpModel()

# with open('lr.pickle', 'rb') as f:
#     lr = pickle.load(f)

