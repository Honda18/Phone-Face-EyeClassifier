import urllib.request
import cv2


def store_raw_images():
    neg_links="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n14564779"
    #neg_links="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n09618957"
    neg_links_string=urllib.request.urlopen(neg_links).read().decode()



    #pic_num=1
    pic_num=1444
    for i in neg_links_string.split("\n"):
        try:
            urllib.request.urlretrieve(i, "NegativeImgs/"+str(pic_num)+".jpg")
            img=cv2.imread("NegativeImgs/"+str(pic_num)+".jpg", cv2.IMREAD_GRAYSCALE)
            resized_img=cv2.resize(img, (200, 200))
            cv2.imwrite("NegativeImgs/"+str(pic_num)+".jpg", resized_img)
            pic_num+=1
        except Exception:
            print(str(Exception))
store_raw_images()



    
