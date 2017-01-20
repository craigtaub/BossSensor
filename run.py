# -*- coding:utf-8 -*-
import cv2

from train import Model
from image_show import show_image

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cascade_path = "./cascades/haarcascade_frontalface_default.xml"
    das_model = Model()
    das_model.load()
    craig_model = Model()
    craig_model.load('./store/model2.h5')
    while True:
        _, frame = cap.read()

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cascade = cv2.CascadeClassifier(cascade_path)

        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)
            for rect in facerect:
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                das_result = das_model.predict(image)
                craig_result = craig_model.predict(image)
                if das_result == 0:  # boss
                    print('Das is approaching')
                    show_image()
                elif craig_result == 0:
                    print('Craig is approaching')
                    show_image('./images_to_display/craig_dash.jpg')
                else:
                    print('Someone is approaching')
                    show_image('./images_to_display/nikita_dash.jpg')

        k = cv2.waitKey(100)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
