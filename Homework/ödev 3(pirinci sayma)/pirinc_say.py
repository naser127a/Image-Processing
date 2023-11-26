import cv2
import numpy as np

def say_pirinc(resim):
    foto = cv2.imread(resim)

    gri_foto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gri",gri_foto)
    #cv2.imwrite("gri.png", gri_foto)

    _, esiklenmis = cv2.threshold(gri_foto, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("esikleme", esiklenmis)
    #cv2.imwrite("esikleme.png", esiklenmis)
    # Morfolojik açma iyleştirme
    kernel = np.ones((5, 5), np.uint8)
    acma_iyilestirme = cv2.morphologyEx(esiklenmis, cv2.MORPH_OPEN, kernel)

    # Konturları bul
    konturlar, _ = cv2.findContours(acma_iyilestirme, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Pirinç Sayısı:", len(konturlar))

    # Konturları resimde göster
    for kontur in konturlar:
        cv2.drawContours(foto, [kontur], 0, (0, 0, 255), 3)

    # Resmi göster
    cv2.imshow("Pirinc cizer", foto)
    #cv2.imwrite("Pirinc cizer.png", foto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

resim= 'pirincc.png'

say_pirinc(resim)