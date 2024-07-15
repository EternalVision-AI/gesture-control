import cv2
from utils import CvFpsCalc
from gestures import *
import time

def main():
    # init global vars
    global gesture_buffer
    global gesture_id
    global battery_status


    cap = cv2.VideoCapture(0)
    bg =cv2.imread('./bg.png')

    print()
    gesture_detector = GestureRecognition(use_static_image_mode=False, min_detection_confidence=0.97, min_tracking_confidence=0.97)
    gesture_buffer = GestureBuffer(buffer_len=10)


    # FPS Measurement
    cv_fps_calc = CvFpsCalc(buffer_len=10)

    mode = 0
    number = -1
    count = 0
    cv2.imshow('Gesture Recognition', cv2.resize(bg.copy(), (700, 400)))
    time.sleep(3)

    while True:
        time.sleep(0.02)
        count += 1
        fps = cv_fps_calc.get()

        
        # Camera capture
        rect, image = cap.read()
        if not rect:
            break

        if count%30 == 0:
            debug_image, gesture_id = gesture_detector.recognize(image, number, mode)
            gesture_buffer.add_gesture(gesture_id)
            debug_image = gesture_detector.draw_info(debug_image, fps, mode, number)
            cv2.imshow('Gesture Recognition', cv2.resize(debug_image.copy(), (700, 400)))
        else:
            cv2.imshow('Gesture Recognition', cv2.resize(image.copy(), (700, 400)))
        # Process Key (ESC: end)
        key = cv2.waitKey(1) & 0xff
        if key == 27:  # ESC
            break


    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
