import urllib.request

import cv2
import numpy as np

URL = "http://192.168.1.201:8080//shot.jpg"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img.
    cv2.imshow('IPWebcam', img)

    cv2.waitKey(1)
