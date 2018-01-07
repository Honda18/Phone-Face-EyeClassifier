import cv2
import os
import numpy as np
def clean():
    for img in os.listdir('NegativeImgs'):
        try:
            potential_img=cv2.imread("NegativeImgs/" + str(img))
            false= cv2.imread("FalseImgs/8.jpg")
            if potential_img.shape==false.shape and not (np.bitwise_xor(false, potential_img).any()):
                os.remove("NegativeImgs/"+str(img))
        except Exception as e:
            print( str(e))


clean()

