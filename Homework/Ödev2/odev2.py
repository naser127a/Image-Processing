import cv2
import numpy as np

def Kirmizi_nesne(kenar):
    hsv = cv2.cvtColor(kenar, cv2.COLOR_BGR2HSV)

    min_kirmizi = np.array([0, 100, 100])
    max_kirmizi = np.array([10, 255, 255])


    maske = cv2.inRange(hsv, min_kirmizi, max_kirmizi)
    donus = cv2.bitwise_and(kenar, kenar, mask=maske)

    return donus


cap = cv2.VideoCapture(0)

while True:

    ret, kenar = cap.read()
    kirmizi = Kirmizi_nesne(kenar)
    cv2.imshow('kırmızı ', kirmizi)

    # Çıkış için 'ç' basınız
    if cv2.waitKey(1) & 0xFF == ord('ç'):
        break


cap.release()
cv2.destroyAllWindows()
