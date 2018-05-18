import poker
import cv2
import adb_tool as atool
import itertools

#定义一副牌
class Cards(object):
    def __init__(self):
        self.init_cards = ['big_ghost', 'small_ghost'] + list(itertools.product(['S','R','P','B'],range(1,14)))
        self.cards = self.init_cards

    def reset(self):
        self.cards = self.init_cards

    def minus_card(self, _cards):
        self.cards = list(set(self.cards) - set(_cards))

    def show_card(self):
        print(len(self.cards))

cards = Cards()

# img = cv2.imread('ScreenShot/0.png', 0)
# img = cv2.resize(img, (int(img.shape[1] * 0.4), int(img.shape[0] * 0.4)), interpolation=cv2.INTER_CUBIC)
# print(poker.get_others_pokers(img))
# cards.minus_card(poker.get_my_pokers(img))
# cards.minus_card(poker.get_others_pokers(img))
# cards.show_card()

c = 0
while True:
    img = atool.getScreenshot()
    cv2.imwrite('ScreenShot/%d.png'%c, img)
    c += 1
    img = cv2.resize(img, (int(img.shape[1] * 0.4), int(img.shape[0] * 0.4)), interpolation=cv2.INTER_CUBIC)
    cards.minus_card(poker.get_my_pokers(img))
    cards.minus_card(poker.get_others_pokers(img))
    cards.show_card()



