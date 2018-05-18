import os
import cv2
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression


def load_train_data(num):
    """加载训练数据"""
    res = []
    c = []
    for root,dir,file in os.walk('train%d' %num):
        if len(file) != 0:
            _class = root.split(os.path.sep)[-1]
            for f in file:
                img = cv2.imread(os.path.join(root, f), 0)
                if num == 4:
                    resize = (40,20)
                elif num == 5 or num == 6:
                    resize = (20,20)
                elif num == 1:
                    resize = (50,30)
                elif num == 2 or num == 3:
                    resize = (25,30)
                img = cv2.resize(img, resize,interpolation=cv2.INTER_CUBIC)
                res.append(np.array(img).reshape(1,-1).tolist()[0])
                c.append(_class)
    res = np.array(res)
    res[res == 255] = 1
    return res,c


def dumpModel(num):
    """保存模型到lr.pickle文件中"""
    train_data, train_target = load_train_data(num)
    l = LogisticRegression(class_weight='balanced')
    l.fit(train_data,train_target)
    #保存模型
    with open('lr%d.pickle'%num, 'wb') as fw:
        pickle.dump(l, fw)
        print('保存模型完毕')

# 预测
# num 为1预测自己的牌是不是大小王
# num 为2预测自己牌的花色
# num 为3预测自己牌的点数
# num 为4预测他人的牌是不是大小王
# num 为5预测他人牌的花色
# num 为6预测他人牌的点数
def prdect(lr, img, num):
    if num == 4:
        resize = (40, 20)
    elif num == 5 or num == 6:
        resize = (20, 20)
    elif num == 1:
        resize = (50, 30)
    elif num == 2 or num == 3:
        resize = (25, 30)
    img = cv2.resize(img, resize, interpolation=cv2.INTER_CUBIC)
    img = np.array(img).reshape(1, -1)
    img[img == 255] = 1
    y_hat = lr.predict(img)[0]
    return y_hat

#dumpModel(4)

# with open('lr.pickle', 'rb') as f:
#     lr = pickle.load(f)

