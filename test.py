# https://blog.mudatobunka.org/entry/2016/10/03/014520

# 1st img
# https://www.pakutaso.com/20180710190post-16732.html

# 2nd img
# https://www.pakutaso.com/20140259041post-3811.html

import cv2
import glob
import logging

logging.basicConfig(filename='test.log', level=logging.INFO)

# __name__はこのモジュールの名前
logger = logging.getLogger(__name__)

# 評価器を読み込み
# "/xxxxxxxxxxxxxx/openCV_sample/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
#cascade = cv2.CascadeClassifier("opencv/data/haarcascades/haarcascade_frontalcatface.xml")
cascade = cv2.CascadeClassifier("/xxxxxxxxxxxxxx/openCV_sample/opencv/data/haarcascades/haarcascade_frontalface_default.xml")

# 画像の読み込み
try_conts = 1
#img_list.append(glob.glob("/xxxxxxxxxxxxxx/openCV_sample/img/src/*"))
for img in glob.glob("/xxxxxxxxxxxxxx/openCV_sample/img/src/*"):
    _file = cv2.imread(img)
    logging.info(_file)
    # 処理速度を高めるために画像をグレースケールに変換
    gray = cv2.cvtColor(_file, cv2.COLOR_BGR2GRAY)
    # 顔検出
    facerect = cascade.detectMultiScale(
        gray,
        scaleFactor=1.11,
        minNeighbors=3,
        minSize=(30, 30)
    )
    if 0 != len(facerect):
        BORDER_COLOR = (255, 255, 255) # 線色を白に
        for rect in facerect:
            # 顔検出した部分に枠を描画
            cv2.rectangle(
                _file,
                tuple(rect[0:2]),
                tuple(rect[0:2] + rect[2:4]),
                BORDER_COLOR,
                thickness=2
            )
    cv2.imwrite("/xxxxxxxxxxxxxx/openCV_sample/img/dest/detected_" + str(try_conts) + ".jpg", _file)
    try_conts += 1
    logging.info(try_conts)